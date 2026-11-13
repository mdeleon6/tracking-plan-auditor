"""The checks themselves: pure functions on data that is already loaded. No BigQuery here."""
from itertools import combinations
import pandas as pd


def compare_events(planned: set[str], observed: set[str]) -> dict[str, set[str]]:
    """Compare planned and observed events and return a dictionary with the differences."""
    return {
        "missing_in_data": planned - observed,
        "not_in_plan": observed - planned,
    }


def find_deprecated_events(deprecated: set[str], observed: set[str]) -> set[str]:
    """Return deprecated events that are still appearing in the data."""
    return deprecated.intersection(observed)


def audit_events(plan: pd.DataFrame, observed: set[str]) -> dict[str, set[str]]:
    """Check observed events against the tracking plan."""
    active = plan[plan["status"] == "active"]
    planned_events = set(active["event_name"].tolist())
    deprecated = plan[plan["status"] == "deprecated"]
    deprecated_events = set(deprecated["event_name"].tolist())

    results = compare_events(planned_events, observed - deprecated_events)
    results["deprecated_still_firing"] = find_deprecated_events(deprecated_events, observed)
    return results


def find_field_gaps(
    required: pd.DataFrame,
    coverage: pd.DataFrame,
    min_coverage: float = 0.99,
) -> pd.DataFrame:
    """Return required fields whose coverage is below min_coverage."""
    merged = required.merge(coverage, on=["event_name", "field_name", "measured_per"], how="left")
    merged["coverage_rate"] = merged["coverage_rate"].fillna(0)
    return merged[merged["coverage_rate"] < min_coverage]


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


def find_coverage_shifts(records: pd.DataFrame, fields: list[str], window: int = 7, max_drop: float = 0.10, min_records: int = 1) -> pd.DataFrame:
    """Return days when a field's coverage is more than max_drop below its median over the previous window days."""
    shifts = []
    for field in fields:
        daily = daily_field_coverage(records, field)
        daily["before"] = daily["coverage"].shift(1).rolling(window, min_periods=window).median()
        daily["after"] = daily["coverage"].shift(-1)
        low = daily[(daily["total"] >= min_records) & (daily["coverage"] < daily["before"] - max_drop)]
        shifts.append(low.assign(field_name=field))
    return pd.concat(shifts, ignore_index=True)


def find_repeated_item_counts(counts: pd.DataFrame, min_share: float = 0.5) -> pd.DataFrame:
    """Return events where most records carry the same number of products, above 1."""
    counts = counts.assign(total=counts.groupby("event_name")["events"].transform("sum"))
    counts = counts.assign(share=counts["events"] / counts["total"])
    counts = counts.assign(max_items=counts.groupby("event_name")["items_in_event"].transform("max"))
    return counts[(counts["items_in_event"] > 1) & (counts["share"] >= min_share)]


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


def split_low_days(low: pd.DataFrame, min_events: int = 5) -> tuple[pd.DataFrame, pd.DataFrame]:
    """Separate days when many events dropped together from drops on just a few events."""
    events_per_day = low.groupby("event_date")["event_name"].transform("nunique")
    together = low[events_per_day >= min_events]
    separate = low[events_per_day < min_events]
    return together, separate
