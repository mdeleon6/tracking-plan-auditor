"""Run the checks against BigQuery. This is the only part that reads the data, so a new data source replaces this file."""
from pathlib import Path
import pandas as pd
from bq import load_sql, run_query, load_settings
from checks import (
    audit_events, find_field_gaps, find_co_missing, find_coverage_drops,
    find_dependency_breaks, find_missing_days, find_low_days, find_repeated_item_counts
)
from plan import load_events_plan, load_field_plan, required_fields, load_dependencies

QUERIES = Path(__file__).parent / "queries"


def query(name: str) -> pd.DataFrame:
    """Run one of the SQL files in queries/."""
    return run_query(load_sql(QUERIES / name))


def daily_event_counts() -> pd.DataFrame:
    """Return how many times each event fired on each day."""
    return query("16_daily_event_counts.sql")


def run_event_check() -> dict[str, set[str]]:
    """Compare the tracking plan's active events with the events in BigQuery."""
    observed_events = set(query("01_event_counts.sql")["event_name"].tolist())
    return audit_events(load_events_plan(), observed_events)


def run_field_check() -> pd.DataFrame:
    """Compare the field plan with field coverage in BigQuery."""
    coverage = pd.concat([
        query("07_field_coverage.sql").assign(measured_per="event"),
        query("17_items_field_coverage.sql").assign(measured_per="product"),
        query("18_ecommerce_field_coverage.sql").assign(measured_per="event"),
        query("19_items_field_coverage_per_event.sql").assign(measured_per="event"),
        query("20_country_platform_coverage.sql").assign(measured_per="event"),
    ])
    plan = load_field_plan()
    required = plan[
        (plan["required"] == "yes")
        & (plan["location"].isin(["event_params", "items", "ecommerce", "geo", "device", "top_level"]))
        & (plan["status"] == "active")
    ][["event_name", "field_name", "location", "measured_per"]]
    return find_field_gaps(required, coverage)


def run_co_missing_check() -> pd.DataFrame:
    """Count purchases missing each pair of required event_params fields."""
    records = query("21_purchase_param_keys.sql")
    fields = required_fields("purchase", "event_params") + required_fields("purchase", "ecommerce")
    return find_co_missing(records, fields).assign(event_name="purchase")


def run_coverage_drop_check() -> pd.DataFrame:
    """Find days when a required purchase field's coverage dropped well below normal."""
    records = query("21_purchase_param_keys.sql")
    fields = required_fields("purchase", "event_params") + required_fields("purchase", "ecommerce")
    min_records = load_settings()["min_records_per_day"]
    return find_coverage_drops(records, fields, min_records=min_records).assign(event_name="purchase")


def run_dependency_check() -> pd.DataFrame:
    """Find events that fired more often than the event they require."""
    dependencies = load_dependencies()
    if dependencies is None:
        return pd.DataFrame(columns=["event_name", "requires", "reason", "event_count", "required_count"])
    return find_dependency_breaks(daily_event_counts(), dependencies)


def run_item_count_check() -> tuple[pd.DataFrame, set[str]]:
    """Find events where most records carry the same number of products, and return every event checked."""
    counts = query("22_items_per_event.sql")
    return find_repeated_item_counts(counts), set(counts["event_name"])


def run_volume_check() -> dict[str, set[str]]:
    """Find the days each event did not appear on in BigQuery."""
    return find_missing_days(daily_event_counts())


def run_low_day_check() -> pd.DataFrame:
    """Find days each event was far below its typical weekday count in BigQuery."""
    return find_low_days(daily_event_counts())


def run_all_checks() -> dict:
    """Run every check and return the results together."""
    return {
        "events": run_event_check(),
        "field_gaps": run_field_check(),
        "missing_days": run_volume_check(),
        "low_days": run_low_day_check(),
    }


if __name__ == "__main__":
    results = run_all_checks()
    print(results["events"])
    print(results["field_gaps"].to_string())
    print({event: len(days) for event, days in results["missing_days"].items()})
    print(len(results["low_days"]))
