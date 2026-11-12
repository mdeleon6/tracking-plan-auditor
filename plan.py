"""Read the tracking plan files in tracking_plan/."""
from pathlib import Path
import pandas as pd

PLAN_DIR = Path(__file__).parent / "tracking_plan"


def load_events_plan() -> pd.DataFrame:
    """Read the event plan."""
    return pd.read_csv(PLAN_DIR / "events.csv")


def load_field_plan() -> pd.DataFrame:
    """Read the field plan."""
    return pd.read_csv(PLAN_DIR / "event_fields.csv")


def required_fields(event_name: str, location: str) -> list[str]:
    """Return the active required fields the plan lists for one event and location."""
    plan = load_field_plan()
    return plan[
        (plan["event_name"] == event_name)
        & (plan["location"] == location)
        & (plan["required"] == "yes")
        & (plan["status"] == "active")
    ]["field_name"].tolist()


def load_dependencies() -> pd.DataFrame | None:
    """Read the event dependencies, or return None if the plan has none."""
    path = PLAN_DIR / "event_dependencies.csv"
    if not path.exists():
        return None
    return pd.read_csv(path)


def load_event_severities() -> dict[str, str]:
    """Read each event's severity_if_missing rating from the tracking plan."""
    plan = load_events_plan()
    rated = plan.dropna(subset=["severity_if_missing"])
    return dict(zip(rated["event_name"], rated["severity_if_missing"]))


def load_event_uses() -> dict[str, str]:
    """Read what each event is used in from the tracking plan."""
    plan = load_events_plan()
    used = plan.dropna(subset=["used_in"])
    return dict(zip(used["event_name"], used["used_in"]))


def load_field_uses() -> dict[tuple[str, str], str]:
    """Read what each field is used in, keyed by (event, field)."""
    plan = load_field_plan()
    return dict(zip(zip(plan["event_name"], plan["field_name"]), plan["used_in"]))


def load_holidays() -> dict[str, str]:
    """Read the holiday calendar, keyed by date in YYYYMMDD format."""
    calendar = pd.read_csv(PLAN_DIR / "calendar.csv", dtype={"date": str})
    return dict(zip(calendar["date"], calendar["name"] + ": " + calendar["observed"]))
