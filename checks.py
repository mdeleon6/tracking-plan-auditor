import pandas as pd
from pathlib import Path
from bq import load_sql, run_query


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
    merged = required.merge(coverage, on=["event_name", "field_name"], how="left")
    merged["coverage_rate"] = merged["coverage_rate"].fillna(0)
    return merged[merged["coverage_rate"] <min_coverage]


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
    coverage = pd.concat([
        run_query(load_sql(params_sql)),
        run_query(load_sql(items_sql)),
        run_query(load_sql(ecommerce_sql)),
    ])
    plan_path = Path(__file__).parent / "tracking_plan" / "event_fields.csv"
    plan = pd.read_csv(plan_path)
    required = plan[
        (plan["required"] == "yes")
        & (plan["location"].isin(["event_params", "items", "ecommerce"]))
        & (plan["status"] == "active")
    ][["event_name", "field_name"]]

    return find_field_gaps(required, coverage)


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


if __name__ == "__main__":
    real = run_event_check()
    print(real)
    assert real["missing_in_data"] == {"add_to_wishlist", "remove_from_cart", "view_cart", "refund"}
    assert real["not_in_plan"] == {"add_shipping_info"}
    assert real["deprecated_still_firing"] == set()
    
    
    gaps = run_field_check()
    print(gaps)
    missing_days = run_volume_check()
    for event_name, days in missing_days.items():
        print(event_name, len(days), sorted(days))
    low = run_low_day_check()
    print(low.groupby("event_name").size())
    print(low[low["event_name"] == "add_to_cart"].to_string())
