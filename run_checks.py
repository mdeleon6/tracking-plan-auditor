"""Run the checks against BigQuery. This is the only part that reads the data, so a new data source replaces this file."""
from pathlib import Path
import pandas as pd
from bq import fill_settings, load_sql, run_query, load_settings
from build_sql import items_coverage_per_product_sql, items_coverage_per_event_sql
from checks import (
    audit_events, find_field_gaps, find_co_missing, find_coverage_drops,
    find_dependency_breaks, find_missing_days, find_low_days, find_repeated_item_counts,
    find_coverage_shifts
)
from plan import load_events_plan, load_field_plan, required_fields, load_dependencies

QUERIES = Path(__file__).parent / "queries" / "checks"


def query(name: str) -> pd.DataFrame:
    """Run one of the SQL files in queries/checks/."""
    return run_query(load_sql(QUERIES / name))


def daily_event_counts() -> pd.DataFrame:
    """Return how many times each event fired on each day."""
    return query("daily_event_counts.sql")


def run_event_check() -> dict[str, set[str]]:
    """Compare the tracking plan's active events with the events in BigQuery."""
    observed_events = set(query("event_counts.sql")["event_name"].tolist())
    return audit_events(load_events_plan(), observed_events)


def items_coverage(plan: pd.DataFrame, measured_per: str) -> pd.DataFrame:
    """Measure the plan's required items fields, either per product or per event."""
    rows = plan[
        (plan["location"] == "items") & (plan["required"] == "yes")
        & (plan["status"] == "active") & (plan["measured_per"] == measured_per)
    ]
    fields = sorted(set(zip(rows["field_name"], rows["type"])))
    if not fields:
        return pd.DataFrame(columns=["event_name", "field_name", "coverage_rate", "measured_per"])
    build = items_coverage_per_product_sql if measured_per == "product" else items_coverage_per_event_sql
    return run_query(fill_settings(build(fields))).assign(measured_per=measured_per)


def run_field_check() -> pd.DataFrame:
    """Compare the field plan with field coverage in BigQuery."""
    plan = load_field_plan()
    coverage = pd.concat([
        query("event_params_coverage.sql").assign(measured_per="event"),
        items_coverage(plan, "product"),
        query("ecommerce_coverage.sql").assign(measured_per="event"),
        items_coverage(plan, "event"),
        query("country_device_platform_coverage.sql").assign(measured_per="event"),
    ])
    required = plan[
        (plan["required"] == "yes")
        & (plan["location"].isin(["event_params", "items", "ecommerce", "geo", "device", "top_level"]))
        & (plan["status"] == "active")
    ][["event_name", "field_name", "location", "measured_per"]]
    return find_field_gaps(required, coverage)


def run_co_missing_check() -> pd.DataFrame:
    """Count purchases missing each pair of required event_params fields."""
    records = query("purchase_field_keys.sql")
    fields = required_fields("purchase", "event_params") + required_fields("purchase", "ecommerce")
    return find_co_missing(records, fields).assign(event_name="purchase")


def run_coverage_drop_check() -> pd.DataFrame:
    """Find days when a required purchase field's coverage dropped well below normal."""
    records = query("purchase_field_keys.sql")
    fields = required_fields("purchase", "event_params") + required_fields("purchase", "ecommerce")
    min_records = load_settings()["min_records_per_day"]
    return find_coverage_drops(records, fields, min_records=min_records).assign(event_name="purchase")


def run_coverage_shift_check() -> pd.DataFrame:
    """Find days when add_to_cart quantity coverage fell well below the week before."""
    records = query("items_quantity_keys.sql")
    min_records = load_settings()["min_records_per_day"]
    return find_coverage_shifts(records, ["quantity"], min_records=min_records).assign(event_name="add_to_cart")


def run_dependency_check() -> pd.DataFrame:
    """Find events that fired more often than the event they require."""
    dependencies = load_dependencies()
    if dependencies is None:
        return pd.DataFrame(columns=["event_name", "requires", "reason", "event_count", "required_count"])
    return find_dependency_breaks(daily_event_counts(), dependencies)


def run_item_count_check() -> tuple[pd.DataFrame, set[str]]:
    """Find events where most records carry the same number of products, and return every event checked."""
    counts = query("items_per_event.sql")
    return find_repeated_item_counts(counts), set(counts["event_name"])


def run_volume_check() -> dict[str, set[str]]:
    """Find the days each event did not appear on in BigQuery."""
    return find_missing_days(daily_event_counts())


def run_low_day_check() -> pd.DataFrame:
    """Find days each event was far below its typical weekday count in BigQuery."""
    return find_low_days(daily_event_counts())


def run_all_checks() -> dict:
    """Run every check and return the results together."""
    repeated, checked = run_item_count_check()
    return {
        "events": run_event_check(),
        "field_gaps": run_field_check(),
        "co_missing": run_co_missing_check(),
        "coverage_drops": run_coverage_drop_check(),
        "coverage_shifts": run_coverage_shift_check(),
        "dependency_breaks": run_dependency_check(),
        "repeated_item_counts": repeated,
        "item_count_events_checked": checked,
        "missing_days": run_volume_check(),
        "low_days": run_low_day_check(),
    }


if __name__ == "__main__":
    results = run_all_checks()
    print("Planned events never received:", sorted(results["events"]["missing_in_data"]))
    print("Events not in the plan:", sorted(results["events"]["not_in_plan"]))
    print("Deprecated events still firing:", sorted(results["events"]["deprecated_still_firing"]))
    print("Field gaps:", len(results["field_gaps"]))
    print("Field pairs missing together:", int((results["co_missing"]["missing_both"] > 0).sum()))
    print("Coverage drop days:", len(results["coverage_drops"]))
    print("Coverage shift days:", len(results["coverage_shifts"]))
    print("Dependency breaks:", len(results["dependency_breaks"]))
    print("Events with repeated product counts:", sorted(results["repeated_item_counts"]["event_name"]))
    print("Missing days:", {event: len(days) for event, days in results["missing_days"].items()})
    print("Low days:", len(results["low_days"]))
