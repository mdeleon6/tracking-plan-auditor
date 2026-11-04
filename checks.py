import pandas as pd
from pathlib import Path
from bq import load_sql, run_query


def compare_events(planned: set[str], observed: set[str]) -> dict[str, set[str]]:
    """Compare planned and observed events and return a dictionary with the differences."""
    return {
        "missing_in_data": planned - observed,
        "not_in_plan": observed - planned,
    }


def run_event_check() -> dict[str, set[str]]:
    """Compare the tracking plan's active events with the events in BigQuery"""
    sql_path = Path(__file__).parent / "queries" / "01_event_counts.sql"
    sql = load_sql(sql_path)
    df = run_query(sql)

    plan_path = Path(__file__).parent / "tracking_plan" / "events.csv"
    plan = pd.read_csv(plan_path)
    active = plan[plan["status"] == "active"]
    planned_events = set(active["event_name"].tolist())
    observed_events = set(df["event_name"].tolist())

    return compare_events(planned_events, observed_events)


if __name__ == "__main__":
    real = run_event_check()
    print(real)
    assert real["missing_in_data"] == {"add_to_wishlist", "remove_from_cart", "view_cart", "refund"}
    assert real["not_in_plan"] == {"add_shipping_info"}