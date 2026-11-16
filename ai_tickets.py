"""Draft tickets with Claude from the problem descriptions, and check the numbers in each draft."""
import re
from collections.abc import Callable
from pathlib import Path

import anthropic
import pandas as pd

from bq import load_settings
from checks import split_low_days
from describe import (
    describe_dependency_breaks,
    describe_event_audit,
    describe_field_gaps,
    describe_low_days_by_event,
    describe_low_days_together,
    describe_missing_days,
    describe_repeated_item_counts,
    describe_type_mismatches,
    format_stretch,
)
from plan import load_event_severities, load_event_uses, load_field_uses, load_holidays
from run_checks import run_all_checks

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
If the check results say "Severity set by the tracking plan", use that severity exactly. If you think it should be different, keep the plan's severity and add a next step asking the plan owner to review the rating.

You will be given an example ticket inside <example_ticket> tags. Copy its sections, order and tone only. Never reuse its events, dates, numbers or references to past experience. Leave "Found by" and "Date found" blank for a person to fill in. Do not carry over any possible cause, impact, next step or acceptance criterion from the example. Do not reuse the example's wording or the questions it asks.

In the ticket, call the information you were given "the check results". Never write "the input".
"""

client = anthropic.Anthropic()
OUTPUT_FOLDER = Path(__file__).parent / "ai_drafts"


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


def find_unsupported_numbers(ticket: str, problem: str) -> set[str]:
    """Return numbers in the ticket that do not appear in the problem text."""
    pattern = r"\d+(?:\.\d+)?"
    ticket = re.sub(r"(?<=\d),(?=\d{3})", "", ticket)
    ticket_numbers = set(re.findall(pattern, ticket))
    problem_numbers = set(re.findall(pattern, problem))
    return ticket_numbers - problem_numbers


def find_severity(ticket: str) -> str | None:
    """Return the severity from the ticket header, or None if it is not High, Medium or Low."""
    match = re.search(r"\*\*Severity:\*\* (High|Medium|Low)\s*$", ticket, re.MULTILINE)
    return match.group(1) if match else None


def save_drafts(problems: list[str], prefix: str, skip: Callable[[str], bool] = lambda problem: False) -> None:
    """Draft a ticket for each problem, save it, and print its severity and any numbers not in the check results."""
    OUTPUT_FOLDER.mkdir(exist_ok=True)
    for number, problem in enumerate(problems, start=1):
        if skip(problem):
            continue
        ticket = draft_ticket(problem)
        (OUTPUT_FOLDER / f"{prefix}{number}.md").write_text(ticket, encoding="utf-8")
        severity = find_severity(ticket) or "SEVERITY MISSING"
        print(f"{prefix}{number}", severity, find_unsupported_numbers(ticket, problem))


def data_period() -> str:
    """Write the period set in settings.toml, like Nov 1, 2020 to Jan 31, 2021."""
    settings = load_settings()
    start = pd.to_datetime(settings["start_date"], format="%Y%m%d")
    end = pd.to_datetime(settings["end_date"], format="%Y%m%d")
    return format_stretch(start, end)


def describe_all(results: dict) -> dict[str, list[str]]:
    """Turn every check's results into problem descriptions, grouped by check, without querying BigQuery again."""
    severities = load_event_severities()
    event_uses = load_event_uses()
    field_uses = load_field_uses()
    holidays = load_holidays()
    period = data_period()
    together, separate = split_low_days(results["low_days"])
    return {
        "events": describe_event_audit(results["events"], severities, event_uses, period),
        "field_gaps": describe_field_gaps(
            results["field_gaps"], field_uses, results["co_missing"],
            results["coverage_drops"], results["coverage_shifts"], period,
        ),
        "type_mismatches": describe_type_mismatches(results["type_mismatches"], field_uses, period),
        "missing_days": describe_missing_days(results["missing_days"], results["daily_event_counts"], severities, event_uses),
        "low_days": (
            describe_low_days_together(together, severities, holidays, event_uses)
            + describe_low_days_by_event(separate, together, results["missing_days"], severities, holidays, event_uses)
        ),
        "dependency_breaks": describe_dependency_breaks(results["dependency_breaks"], event_uses),
        "repeated_item_counts": describe_repeated_item_counts(
            results["repeated_item_counts"], event_uses, results["item_count_events_checked"], period,
        ),
    }

PREFIXES = {
    "events": "draft_events_",
    "field_gaps": "draft_",
    "type_mismatches": "draft_type_",
    "missing_days": "draft_missing_days_",
    "low_days": "draft_low_days_",
    "dependency_breaks": "draft_dependency_",
    "repeated_item_counts": "draft_item_count_",
}


def is_example_ticket(problem: str) -> bool:
    """Skip the shipping_tier problem, because finding 003 is the example ticket for it."""
    return "- shipping_tier (" in problem


def draft_all_tickets() -> None:
    """Clear old drafts, run every check once, then draft a ticket for every problem found."""
    for old in OUTPUT_FOLDER.glob("*.md"):
        old.unlink()
    for check, problems in describe_all(run_all_checks()).items():
        skip = is_example_ticket if check == "field_gaps" else (lambda problem: False)
        save_drafts(problems, PREFIXES[check], skip=skip)



if __name__ == "__main__":
    draft_all_tickets()
