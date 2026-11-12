import pandas as pd
from pathlib import Path
from bq import load_sql, run_query, load_settings
from itertools import combinations


def compare_events(planned: set[str], observed: set[str]) -> dict[str, set[str]]:
    """Compare planned and observed events and return a dictionary with the differences."""
    return {
        "missing_in_data": planned - observed,
        "not_in_plan": observed - planned,
    }


def find_deprecated_events(deprecated: set[str], observed: set[str]) -> set[str]:
    """Return deprecated events that are still appearing in the data."""
    return deprecated.intersection(observed)


def find_field_gaps(
    required: pd.DataFrame,
    coverage: pd.DataFrame,
    min_coverage: float = 0.99,
) -> pd.DataFrame:
    """Return required fields whose coverage is below min_coverage."""
    merged = required.merge(coverage, on=["event_name", "field_name", "measured_per"], how="left")
    merged["coverage_rate"] = merged["coverage_rate"].fillna(0)
    return merged[merged["coverage_rate"] <min_coverage]


def find_co_missing(records: pd.DataFrame, fields: list[str]) -> pd.DataFrame:
    """For each pair of fields, count records missing one, the other, and both."""
    missing = pd.DataFrame({
        field: records["keys"].apply(lambda keys: field not in keys)
        for field in fields
    })
    rows = []
    for a, b in combinations(fields, 2):
        rows.append({
            "field_a": a,
            "field_b": b,
            "missing_a": int(missing[a].sum()),
            "missing_b": int(missing[b].sum()),
            "missing_both": int((missing[a] & missing[b]).sum()),
        })
    return pd.DataFrame(rows)


def daily_field_coverage(records: pd.DataFrame, field: str) -> pd.DataFrame:
    """Return each day's count of records with the field, total records, and coverage."""
    has_field = records["keys"].apply(lambda keys: field in keys)
    daily = has_field.groupby(records["event_date"]).agg(present="sum", total="count")
    daily["coverage"] = daily["present"] / daily["total"]
    return daily.reset_index()


def find_coverage_drops(records: pd.DataFrame, fields: list[str], max_drop: float = 0.10, min_records: int = 1) -> pd.DataFrame:
    """Return days when a field's coverage is more than max_drop below its typical daily coverage."""
    drops = []
    for field in fields:
        daily = daily_field_coverage(records, field)
        typical = daily["coverage"].median()
        low = daily[(daily["total"] >= min_records) & (daily["coverage"] < typical - max_drop)]
        drops.append(low.assign(field_name=field, typical=typical))
    return pd.concat(drops, ignore_index=True)


def find_dependency_breaks(daily: pd.DataFrame, dependencies: pd.DataFrame) -> pd.DataFrame:
    """Return pairs where an event fired more often than the event it requires."""
    totals = daily.assign(event_count=daily["event_count"].astype(int)).groupby("event_name")["event_count"].sum()
    result = dependencies.assign(
        event_count=dependencies["event_name"].map(totals).fillna(0).astype(int),
        required_count=dependencies["requires"].map(totals).fillna(0).astype(int),
    )
    return result[result["event_count"] > result["required_count"]]


def find_missing_days(daily: pd.DataFrame) -> dict[str, set[str]]:
    """Return the dates each event did not appear on."""
    all_dates = set(daily["event_date"].tolist())
    missing = {}
    for event_name, rows in daily.groupby("event_name"):
        event_dates = set(rows["event_date"].tolist())
        gaps = all_dates - event_dates
        if gaps:
            missing[event_name] = gaps
    return missing


def find_low_days(daily: pd.DataFrame, min_ratio: float = 0.5) -> pd.DataFrame:
    """Return days where an event was far below its typical count for that weekday."""
    result = daily.copy()
    dates = pd.to_datetime(result["event_date"], format="%Y%m%d")
    result["weekday"] = dates.dt.day_name()
    result["typical"] = result.groupby(["weekday", "event_name"])["event_count"].transform("median")
    result["ratio"] = result["event_count"] / result["typical"]
    return result[result["ratio"] < min_ratio]



def audit_events(plan: pd.DataFrame, observed: set[str]) -> dict[str, set[str]]:
    """Check observed events against the tracking plan."""
    active = plan[plan["status"] == "active"]
    planned_events = set(active["event_name"].tolist())
    deprecated = plan[plan["status"] == "deprecated"]
    deprecated_events = set(deprecated["event_name"].tolist())

    results = compare_events(planned_events, observed - deprecated_events)
    results["deprecated_still_firing"] = find_deprecated_events(deprecated_events, observed)
    return results


def run_event_check() -> dict[str, set[str]]:
    """Compare the tracking plan's active events with the events in BigQuery"""
    sql_path = Path(__file__).parent / "queries" / "01_event_counts.sql"
    sql = load_sql(sql_path)
    df = run_query(sql)

    plan_path = Path(__file__).parent / "tracking_plan" / "events.csv"
    plan = pd.read_csv(plan_path)
    observed_events = set(df["event_name"].tolist())

    return audit_events(plan, observed_events)


def run_field_check() -> pd.DataFrame:
    """Compare the field plan with field coverage in BigQuery."""
    params_sql = Path(__file__).parent / "queries" / "07_field_coverage.sql"
    items_sql = Path(__file__).parent / "queries" / "17_items_field_coverage.sql"
    ecommerce_sql = Path(__file__).parent / "queries" / "18_ecommerce_field_coverage.sql"
    per_event_sql = Path(__file__).parent / "queries" / "19_items_field_coverage_per_event.sql"
    context_sql = Path(__file__).parent / "queries" / "20_country_platform_coverage.sql"
    coverage = pd.concat([
        run_query(load_sql(params_sql)).assign(measured_per="event"),
        run_query(load_sql(items_sql)).assign(measured_per="product"),
        run_query(load_sql(ecommerce_sql)).assign(measured_per="event"),
        run_query(load_sql(per_event_sql)).assign(measured_per="event"),
        run_query(load_sql(context_sql)).assign(measured_per="event"),
    ])
    plan_path = Path(__file__).parent / "tracking_plan" / "event_fields.csv"
    plan = pd.read_csv(plan_path)
    required = plan[
        (plan["required"] == "yes")
        & (plan["location"].isin(["event_params", "items", "ecommerce","geo", "device", "top_level"]))
        & (plan["status"] == "active")
    ][["event_name", "field_name","location", "measured_per"]]

    return find_field_gaps(required, coverage)


def run_co_missing_check() -> pd.DataFrame:
    """Count purchases missing each pair of required event_params fields."""
    sql_path = Path(__file__).parent / "queries" / "21_purchase_param_keys.sql"
    records = run_query(load_sql(sql_path))
    plan = pd.read_csv(Path(__file__).parent / "tracking_plan" / "event_fields.csv")
    fields = plan[
        (plan["event_name"] == "purchase")
        & (plan["location"] == "event_params")
        & (plan["required"] == "yes")
        & (plan["status"] == "active")
    ]["field_name"].tolist()
    return find_co_missing(records, fields).assign(event_name="purchase")


def run_coverage_drop_check() -> pd.DataFrame:
    """Find days when a required purchase field's coverage dropped well below normal."""
    sql_path = Path(__file__).parent / "queries" / "21_purchase_param_keys.sql"
    records = run_query(load_sql(sql_path))
    plan = pd.read_csv(Path(__file__).parent / "tracking_plan" / "event_fields.csv")
    fields = plan[
        (plan["event_name"] == "purchase")
        & (plan["location"] == "event_params")
        & (plan["required"] == "yes")
        & (plan["status"] == "active")
    ]["field_name"].tolist()
    min_records = load_settings()["min_records_per_day"]
    return find_coverage_drops(records, fields, min_records=min_records).assign(event_name="purchase")


def run_dependency_check() -> pd.DataFrame:
    """Find events that fired more often than the event they require."""
    deps_path = Path(__file__).parent / "tracking_plan" / "event_dependencies.csv"
    if not deps_path.exists():
        return pd.DataFrame(columns=["event_name", "requires", "reason", "event_count", "required_count"])
    sql_path = Path(__file__).parent / "queries" / "16_daily_event_counts.sql"
    daily = run_query(load_sql(sql_path))
    return find_dependency_breaks(daily, pd.read_csv(deps_path))


def run_volume_check() -> dict[str, set[str]]:
    """Find the days each event did not appear on in BigQuery."""
    sql_path = Path(__file__).parent / "queries" / "16_daily_event_counts.sql"
    daily = run_query(load_sql(sql_path))
    return find_missing_days(daily)


def run_low_day_check() -> pd.DataFrame:
    """Find days each event was far below its typical weekday count in BigQuery."""
    sql_path = Path(__file__).parent / "queries" / "16_daily_event_counts.sql"
    daily = run_query(load_sql(sql_path))
    return find_low_days(daily)


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

