"""Draft tickets with Claude from the problem descriptions, and check the numbers in each draft."""
from pathlib import Path
from typing import Callable
import re

import anthropic
import pandas as pd

from bq import load_settings
from checks import find_missing_days, find_low_days, split_low_days
from describe import (
    describe_field_gaps, describe_missing_days, describe_dependency_breaks,
    describe_low_days_by_event, describe_low_days_together, describe_repeated_item_counts, format_stretch
)
from plan import load_event_severities, load_event_uses, load_field_uses, load_holidays
from run_checks import (
    daily_event_counts, run_field_check, run_co_missing_check,
    run_coverage_drop_check, run_dependency_check, run_item_count_check
)


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
    ticket_numbers = set(re.findall(pattern, ticket))
    problem_numbers = set(re.findall(pattern, problem))
    return ticket_numbers - problem_numbers


def save_drafts(problems: list[str], prefix: str, skip: Callable[[str], bool] = lambda problem: False) -> None:
    """Draft a ticket for each problem, save it, and print any numbers not in the check results."""
    OUTPUT_FOLDER.mkdir(exist_ok=True)
    for number, problem in enumerate(problems, start=1):
        if skip(problem):
            continue
        ticket = draft_ticket(problem)
        (OUTPUT_FOLDER / f"{prefix}{number}.md").write_text(ticket, encoding="utf-8")
        print(number, find_unsupported_numbers(ticket, problem))


def draft_field_gap_tickets() -> None:
    problems = describe_field_gaps(run_field_check(), load_field_uses(), run_co_missing_check(), run_coverage_drop_check())
    # The shipping_tier problem is skipped because finding 003 is the example ticket.
    save_drafts(problems, "draft_", skip=lambda problem: "- shipping_tier (" in problem)


def draft_missing_day_tickets() -> None:
    daily = daily_event_counts()
    problems = describe_missing_days(find_missing_days(daily), daily, load_event_severities(), load_event_uses())
    save_drafts(problems, "draft_missing_days_")


def draft_low_day_tickets() -> None:
    daily = daily_event_counts()
    severities = load_event_severities()
    holidays = load_holidays()
    uses = load_event_uses()
    together, separate = split_low_days(find_low_days(daily))
    problems = (
        describe_low_days_together(together, severities, holidays, uses)
        + describe_low_days_by_event(separate, together, find_missing_days(daily), severities, holidays, uses)
    )
    save_drafts(problems, "draft_low_days_")


def draft_dependency_tickets() -> None:
    problems = describe_dependency_breaks(run_dependency_check(), load_event_uses())
    save_drafts(problems, "draft_dependency_")


def data_period() -> str:
    """Write the period set in settings.toml, like Nov 1, 2020 to Jan 31, 2021."""
    settings = load_settings()
    start = pd.to_datetime(settings["start_date"], format="%Y%m%d")
    end = pd.to_datetime(settings["end_date"], format="%Y%m%d")
    return format_stretch(start, end)


def draft_item_count_tickets() -> None:
    repeated, checked = run_item_count_check()
    problems = describe_repeated_item_counts(repeated, load_event_uses(), checked, data_period())
    save_drafts(problems, "draft_item_count_")


if __name__ == "__main__":
    draft_item_count_tickets()
