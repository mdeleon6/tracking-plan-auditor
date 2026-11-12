from pathlib import  Path
import anthropic
import pandas as pd
import re
from bq import load_sql, run_query
from checks import find_low_days, find_missing_days, run_field_check


SYSTEM_PROMPT = """
You write data quality tickets from the results of automated tracking checks. The checks have already run and detected the problem. You do not run anything and you cannot see the underlying data, so you only know what is in the input.

Write for someone outside the immediate team who has no background on this problem. The ticket must make sense on its own.

Never state why a problem happened unless the input confirms the cause. If you mention a possible cause, label it as possible and unconfirmed. Problems that appear together do not prove a shared cause.

Only call a date a holiday if the check results name a holiday next to it. A holiday is context, not a cause: mention it only as a possible, unconfirmed explanation, and say where it is observed. Do not use your own knowledge of holidays, seasons or weekdays to describe or explain a date.

A check result only shows what was received. No rows on a day does not prove whether the activity happened, so do not say a gap comes from missing data rather than real behavior. Rows on a day do not prove the data is complete, so do not use them to say that totals are correct or unaffected.

Only use numbers exactly as they appear in the input. Do not calculate, convert or round any number. If a number you would want is missing, say it is missing. Never estimate.

Do not invent queries, code, file names, links or people.

Choose severity by what the problem breaks, and give your reason in the Impact section:
- High: key business numbers cannot be trusted, such as revenue, orders, units sold or conversion rates.
- Medium: a secondary total or one type of breakdown is affected, but no key business number depends on the missing data. A breakdown of a key number, such as conversion by product, is Medium when the overall number is not affected.
- Low: too small to change any decision, such as a few events on a single day, or reporting nobody acts on.

You will be given an example ticket inside <example_ticket> tags. Copy its sections, order and tone only. Never reuse its events, dates, numbers or references to past experience. Leave "Found by" and "Date found" blank for a person to fill in. Do not carry over any possible cause, impact, next step or acceptance criterion from the example. Do not reuse the example's wording or the questions it asks.

In the ticket, call the information you were given "the check results". Never write "the input".
"""

client = anthropic.Anthropic()


def draft_ticket(problem: str) -> str:
    """Ask Claude to draft a ticket for one detected problem."""
    example_path = Path(__file__).parent / "findings" / "003-purchase-missing-shipping-tier.md"
    example = example_path.read_text(encoding="utf-8")
    user_message = (
        f"<example_ticket>\n{example}\n</example_ticket>\n\n"
        f"<detected_problem>\n{problem}\n</detected_problem>"
    )

    response = client.beta.messages.create(
        model="claude-opus-5-5",
        max_tokens=16000,
        betas=["server-side-fallback-2026-07-01"],
        fallbacks="default",
        output_config={"effort": "medium"},
        system=SYSTEM_PROMPT,
        messages=[{"role": "user", "content": user_message}],
    )

    if response.stop_reason == "refusal":
        raise RuntimeError("Claude declined to write this ticket.")
    return next(block.text for block in response.content if block.type == "text")


def group_consecutive_dates(dates: set[str]) -> list[tuple[pd.Timestamp, pd.Timestamp]]:
    """Turn a set of YYYYMMDD dates into (first day, last day) stretches."""
    days = sorted(pd.to_datetime(list(dates), format="%Y%m%d"))
    stretches = []
    start = days[0]
    previous = days[0]

    for day in days[1:]:
        if (day - previous).days != 1:
            stretches.append((start, previous))
            start = day
        previous = day

    stretches.append((start, previous))
    return stretches


def format_day(day: pd.Timestamp) -> str:
    """Write a date like Nov 2, 2020."""
    return f"{day:%b} {day.day}, {day.year}"


def format_stretch(start: pd.Timestamp, end: pd.Timestamp) -> str:
    """Write a stretch of dates, or one date if it starts and ends on the same day."""
    if start == end:
        return format_day(start)
    return f"{format_day(start)} to {format_day(end)}"


def format_day_with_holiday(event_date: str, holidays: dict[str, str]) -> str:
    """Format a YYYYMMDD date, adding the holiday name if the calendar has one."""
    day = pd.to_datetime(event_date, format="%Y%m%d")
    holiday = holidays.get(event_date)
    if holiday:
        return f"{format_day(day)} ({holiday})"
    return format_day(day)


def describe_missing_days(missing: dict[str, set[str]], daily: pd.DataFrame, severities: dict[str, str], uses: dict[str, str]) -> list[str]:
    """Write one problem description per event that has days with no data."""
    days = pd.to_datetime(daily["event_date"], format="%Y%m%d")
    period = format_stretch(days.min(), days.max())
    total_days = days.nunique()

    complete_events = sorted(set(daily["event_name"]) - set(missing.keys()))


    problems = []
    for event_name, gaps in missing.items():
        severity = severities.get(event_name, "not rated").capitalize()
        event_rows = daily[daily["event_name"] == event_name]
        total_events = event_rows["event_count"].astype(int).sum()
        days_with_data = total_days - len(gaps)
        stretches = group_consecutive_dates(gaps)
        lines = [
            "Check: missing days. An event is flagged for any day in the data period when it has no rows.",
            f"Event: {event_name}",
            f"Severity set by the tracking plan: {severity}.",
            f"Used in, according to the tracking plan: {uses.get(event_name, 'not listed')}.",
            f"Data period: {period} ({total_days} days).",
            f"Total events received on the {days_with_data} days with data: {total_events}.",
            f"Days with no data for this event: {len(gaps)} of {total_days}.",
            "At least one other event was received on every one of these days.",
            f"Events with data on every day of the period: {', '.join(complete_events)}.",
            "Dates with no data:",
        ]
        for start, end in stretches:
            lines.append(f"- {format_stretch(start, end)}")
        for other_event, other_gaps in missing.items():
            shared = gaps & other_gaps
            if other_event != event_name and shared:
                shared_stretches = group_consecutive_dates(shared)
                shared_dates = "; ".join(format_stretch(start, end) for start, end in shared_stretches)
                lines.append(
                    f"{other_event} also has no data on {len(shared)} of these days: {shared_dates}. "
                    f"Across the whole period, {other_event} has no data on {len(other_gaps)} days."
                )
        problems.append("\n".join(lines))
    return problems


def describe_field_gaps(gaps: pd.DataFrame, uses: dict[tuple[str, str], str], min_coverage: float = 0.99) -> list[str]:
    """Group field gaps into problem descriptions, one per event and coverage rate."""
    problems = []
    for (event_name, rate), rows in gaps.groupby(["event_name", "coverage_rate"]):
        missing = round((1 - rate) * 100, 4)
        gap = round((min_coverage - rate) * 100, 4)
        lines = [
            f"Check: required field coverage. A field is flagged when coverage is below {min_coverage}.",
            f"Event: {event_name}",
            f"Share of events or products missing each field: {missing}%. Gap to threshold: {gap} percentage points.",
            f"Flagged fields, all with coverage_rate {round(rate, 6)}:",
        ]
        for _, row in rows.iterrows():
            unit = row["measured_per"]
            used = uses.get((event_name, row["field_name"]), "not listed")
            lines.append(f"- {row['field_name']} (location: {row['location']}, measured per {unit}; used in: {used})")
        if ((rows["location"] == "items") & (rows["measured_per"] == "event")).any():
            lines.append("The tracking plan expects these fields on one product per event, the product actually added, so an event counts as covered if at least one of its products has the field.")
        problems.append("\n".join(lines))
    return problems


def find_unsupported_numbers(ticket: str, problem: str) -> set[str]:
    """Return numbers in the ticket that do not appear in the problem text."""
    pattern = r"\d+(?:\.\d+)?"
    ticket_numbers = set(re.findall(pattern, ticket))
    problem_numbers = set(re.findall(pattern, problem))
    return ticket_numbers - problem_numbers


def split_low_days(low: pd.DataFrame, min_events: int = 5) -> tuple[pd.DataFrame, pd.DataFrame]:
    """Separate days when many events dropped together from drops on just a few events."""
    events_per_day = low.groupby("event_date")["event_name"].transform("nunique")
    together = low[events_per_day >= min_events]
    separate = low[events_per_day < min_events]
    return together, separate


def describe_low_days_by_event(
    separate: pd.DataFrame,
    together: pd.DataFrame,
    missing: dict[str, set[str]],
    severities: dict[str, str],
    holidays: dict[str, str],
    uses: dict[str, str],
    min_ratio: float = 0.5,
) -> list[str]:
    """Write one problem description per event with low days."""
    problems = []
    for event_name, rows in separate.groupby("event_name"):
        rating = severities.get(event_name, "not rated").capitalize()
        lines = [
            f"Check: low volume. A day is flagged when an event's count is below {min_ratio} of its typical count, meaning the median for that weekday.",
            f"Event: {event_name}",
            f"Tracking plan rating if this event stopped arriving entirely: {rating}.",
            f"Used in, according to the tracking plan: {uses.get(event_name, 'not listed')}.",
            f"Number of flagged days: {len(rows)}.",
            "Holiday names next to dates come from the holiday calendar in the tracking plan, followed by where each holiday is observed as a day off. A single date without a name is not on that calendar. Date ranges are not checked against the calendar.",
            "Flagged days:",
        ]
        for _, row in rows.sort_values("event_date").iterrows():
            percent = round(row["ratio"] * 100, 1)
            lines.append(f"- {format_day_with_holiday(row['event_date'], holidays)}: {row['event_count']} events, typical {row['typical']:g}, {percent}% of typical")
        
        grouped_days = sorted(together[together["event_name"] == event_name]["event_date"])
        if grouped_days:
            days = ", ".join(format_day_with_holiday(d, holidays) for d in grouped_days)
            lines.append(
                f"This event was also below threshold on {len(grouped_days)} more days when many events dropped together. "
                f"Those days are covered in a separate multi-event ticket: {days}."
            )

        if event_name in missing:
            stretches = group_consecutive_dates(missing[event_name])
            dates = "; ".join(format_stretch(start, end) for start, end in stretches)
            lines.append(
                f"This event also has days with no data at all: {dates}. "
                "Those days are covered in a separate missing-day ticket and are not part of this one."
            )

        problems.append("\n".join(lines))
    return problems


def describe_low_days_together(
    together: pd.DataFrame,
    severities: dict[str, str],
    holidays: dict[str, str],
    uses: dict[str, str],
    min_events: int = 5,
    min_ratio: float = 0.5,
) -> list[str]:
    """Write one problem description for days when many events dropped together."""
    if together.empty:
        return []

    events = sorted(together["event_name"].unique())
    high_events = [event for event in events if severities.get(event) == "high"]
    high_uses = "; ".join(f"{event}: {uses[event]}" for event in high_events if event in uses)
    lines = [
        f"Check: low volume across many events. A day is listed when at least {min_events} events are each below {min_ratio} of their typical count, meaning the median for that weekday.",
        "Event: multiple events",
        f"Days listed: {together['event_date'].nunique()}. Different events affected: {len(events)}.",
        f"Affected events rated High in the tracking plan if they stopped arriving entirely: {', '.join(high_events) or 'none'}.",
        f"What the High-rated events are used in, according to the tracking plan: {high_uses or 'none'}.",
        "Holiday names next to dates come from the holiday calendar in the tracking plan, followed by where each holiday is observed as a day off. A single date without a name is not on that calendar. Date ranges are not checked against the calendar.",
        "Days listed, with each affected event's count as a percentage of its typical count:",
    ]
    for event_date, rows in together.groupby("event_date"):
        drops = ", ".join(
            f"{row['event_name']} {round(row['ratio'] * 100, 1)}%"
            for _, row in rows.sort_values("event_name").iterrows()
        )
        lines.append(f"- {format_day_with_holiday(event_date, holidays)}: {len(rows)} events below threshold: {drops}")

    return ["\n".join(lines)]


def draft_field_gap_tickets() -> None:
    gaps = run_field_check()
    problems = describe_field_gaps(gaps, load_field_uses())
    output_folder = Path(__file__).parent / "ai_drafts"
    output_folder.mkdir(exist_ok=True)

    for number, problem in enumerate(problems, start=1):
        if "shipping_tier" in problem:
            continue
        ticket = draft_ticket(problem)
        (output_folder / f"draft_{number}.md").write_text(ticket, encoding="utf-8")
        print(number, find_unsupported_numbers(ticket, problem))


def load_event_severities() -> dict[str, str]:
    """Read each event's severity_if_missing rating from the tracking plan."""
    plan_path = Path(__file__).parent / "tracking_plan" / "events.csv"
    plan = pd.read_csv(plan_path)
    rated = plan.dropna(subset=["severity_if_missing"])
    return dict(zip(rated["event_name"], rated["severity_if_missing"]))


def load_event_uses() -> dict[str, str]:
    """Read what each event is used in from the tracking plan."""
    plan_path = Path(__file__).parent / "tracking_plan" / "events.csv"
    plan = pd.read_csv(plan_path)
    used = plan.dropna(subset=["used_in"])
    return dict(zip(used["event_name"], used["used_in"]))


def load_field_uses() -> dict[tuple[str, str], str]:
    """Read what each field is used in, keyed by (event, field)."""
    plan_path = Path(__file__).parent / "tracking_plan" / "event_fields.csv"
    plan = pd.read_csv(plan_path)
    return dict(zip(zip(plan["event_name"], plan["field_name"]), plan["used_in"]))


def load_holidays() -> dict[str, str]:
    """Read the holiday calendar, keyed by date in YYYYMMDD format."""
    calendar_path = Path(__file__).parent / "tracking_plan" / "calendar.csv"
    calendar = pd.read_csv(calendar_path, dtype={"date": str})
    return dict(zip(calendar["date"], calendar["name"] + ": " + calendar["observed"]))


def draft_missing_day_tickets() -> None:
    sql_path = Path(__file__).parent / "queries" / "16_daily_event_counts.sql"
    daily = run_query(load_sql(sql_path))
    missing = find_missing_days(daily)
    severities = load_event_severities()
    uses = load_event_uses()
    problems = describe_missing_days(missing, daily, severities, uses)
    output_folder = Path(__file__).parent / "ai_drafts"
    output_folder.mkdir(exist_ok=True)

    for number, problem in enumerate(problems, start=1):
        ticket = draft_ticket(problem)
        (output_folder / f"draft_missing_days_{number}.md").write_text(ticket, encoding="utf-8")
        print(number, find_unsupported_numbers(ticket, problem))


def draft_low_day_tickets() -> None:
    sql_path = Path(__file__).parent / "queries" / "16_daily_event_counts.sql"
    daily = run_query(load_sql(sql_path))
    severities = load_event_severities()
    holidays = load_holidays()
    uses = load_event_uses()
    together, separate = split_low_days(find_low_days(daily))
    problems = (
        describe_low_days_together(together, severities, holidays, uses)
        + describe_low_days_by_event(separate, together, find_missing_days(daily), severities, holidays, uses)
    )
    output_folder = Path(__file__).parent / "ai_drafts"
    output_folder.mkdir(exist_ok=True)

    for number, problem in enumerate(problems, start=1):
        ticket = draft_ticket(problem)
        (output_folder / f"draft_low_days_{number}.md").write_text(ticket, encoding="utf-8")
        print(number, find_unsupported_numbers(ticket, problem))


if __name__ == "__main__":
    draft_field_gap_tickets()
