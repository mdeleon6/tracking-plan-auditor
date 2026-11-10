import pandas as pd
from pathlib import Path
from checks import find_missing_days, find_low_days


def plant_outage(daily: pd.DataFrame, event_name:str, dates: set[str]) -> pd.DataFrame:
    """Delete an event's rows on the given dates."""
    to_delete =(daily["event_name"] == event_name) & (daily["event_date"].isin(dates))
    return daily[~to_delete]


def plant_drop(daily: pd.DataFrame, event_name: str, date: str, fraction: float) -> pd.DataFrame:
    """Cut an event's count on one date down to a fraction of what it was."""
    result = daily.copy()
    to_cut = (result["event_name"] == event_name) & (result["event_date"] == date)
    result.loc[to_cut, "event_count"] = (result.loc[to_cut, "event_count"] * fraction).astype(int)
    return result


def score(planted: set[tuple[str, str]], flagged: set[tuple[str, str]]) -> dict[str, float]:
    """Compare the planted problems with what the check flagged."""
    caught = planted & flagged
    false_alarms = flagged - planted
    return {
        "catch_rate": len(caught) / len(planted),
        "false_alarms": len(false_alarms),
    }


CLEAN_EVENTS = ["session_start", "first_visit", "page_view"]
DROP_DATES = ["20201202", "20201210", "20210112"]

if __name__ == "__main__":
    path = Path(__file__).parent / "findings" / "data" / "daily_event_counts.csv"
    daily = pd.read_csv(path, dtype={"event_date": str})

    for fraction in [0.1, 0.3, 0.45, 0.6, 0.8]:
        broken = daily
        for event in CLEAN_EVENTS:
            for date in DROP_DATES:
                broken = plant_drop(broken, event, date, fraction)

        low = find_low_days(broken)
        clean_low = low[low["event_name"].isin(CLEAN_EVENTS)]

        flagged = set(zip(clean_low["event_name"], clean_low["event_date"]))
        planted = {(event, date) for event in CLEAN_EVENTS for date in DROP_DATES}
        print(fraction, score(planted, flagged))

