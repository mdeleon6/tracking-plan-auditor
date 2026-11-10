from pathlib import  Path
import anthropic
import pandas as pd
import re
from bq import load_sql, run_query
from checks import find_missing_days, run_field_check


SYSTEM_PROMPT = """
You write data quality tickets from the results of automated tracking checks. The checks have already run and detected the problem. You do not run anything and you cannot see the underlying data, so you only know what is in the input.

Write for someone outside the immediate team who has no background on this problem. The ticket must make sense on its own.

Never state why a problem happened unless the input confirms the cause. If you mention a possible cause, label it as possible and unconfirmed. Problems that appear together do not prove a shared cause.

A check result only shows what was received. No rows on a day does not prove whether the activity happened, so do not say a gap comes from missing data rather than real behavior. Rows on a day do not prove the data is complete, so do not use them to say that totals are correct or unaffected.

Only use numbers exactly as they appear in the input. Do not calculate, convert or round any number. If a number you would want is missing, say it is missing. Never estimate.

Do not invent queries, code, file names, links or people.

Choose severity by what the problem breaks, and give your reason in the Impact section:
- High: totals or key business numbers cannot be trusted, such as revenue, orders or conversion rates.
- Medium: one type of breakdown or analysis is affected, while totals are still correct.
- Low: little effect on any decision.

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


def describe_missing_days(missing: dict[str, set[str]], daily: pd.DataFrame) -> list[str]:
    """Write one problem description per event that has days with no data."""
    days = pd.to_datetime(daily["event_date"], format="%Y%m%d")
    period = format_stretch(days.min(), days.max())
    total_days = days.nunique()

    complete_events = sorted(set(daily["event_name"]) - set(missing.keys()))


    problems = []
    for event_name, gaps in missing.items():
        event_rows = daily[daily["event_name"] == event_name]
        total_events = event_rows["event_count"].astype(int).sum()
        days_with_data = total_days - len(gaps)
        stretches = group_consecutive_dates(gaps)
        lines = [
            "Check: missing days. An event is flagged for any day in the data period when it has no rows.",
            f"Event: {event_name}",
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


def describe_field_gaps(gaps: pd.DataFrame, min_coverage: float = 0.99) -> list[str]:
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
            unit = "product" if row["location"] == "items" else "event"
            lines.append(f"- {row['field_name']} (location: {row['location']}, measured per {unit})")
        problems.append("\n".join(lines))
    return problems


def find_unsupported_numbers(ticket: str, problem: str) -> set[str]:
    """Return numbers in the ticket that do not appear in the problem text."""
    pattern = r"\d+(?:\.\d+)?"
    ticket_numbers = set(re.findall(pattern, ticket))
    problem_numbers = set(re.findall(pattern, problem))
    return ticket_numbers - problem_numbers


def draft_field_gap_tickets() -> None:
    gaps = run_field_check()
    problems = describe_field_gaps(gaps)
    output_folder = Path(__file__).parent / "ai_drafts"
    output_folder.mkdir(exist_ok=True)

    for number, problem in enumerate(problems, start=1):
        if "shipping_tier" in problem:
            continue
        ticket = draft_ticket(problem)
        (output_folder / f"draft_{number}.md").write_text(ticket, encoding="utf-8")
        print(number, find_unsupported_numbers(ticket, problem))


def draft_missing_day_tickets() -> None:
    sql_path = Path(__file__).parent / "queries" / "16_daily_event_counts.sql"
    daily = run_query(load_sql(sql_path))
    missing = find_missing_days(daily)
    problems = describe_missing_days(missing, daily)
    output_folder = Path(__file__).parent / "ai_drafts"
    output_folder.mkdir(exist_ok=True)

    for number, problem in enumerate(problems, start=1):
        ticket = draft_ticket(problem)
        (output_folder / f"draft_missing_days_{number}.md").write_text(ticket, encoding="utf-8")
        print(number, find_unsupported_numbers(ticket, problem))


if __name__ == "__main__":
    draft_missing_day_tickets()
