from pathlib import  Path
import anthropic
import pandas as pd
from checks import run_field_check
import re

SYSTEM_PROMPT = """
You write data quality tickets from the results of automated tracking checks. The checks have already run and detected the problem. You do not run anything and you cannot see the underlying data, so you only know what is in the input.

Write for someone outside the immediate team who has no background on this problem. The ticket must make sense on its own.

Never state why a problem happened unless the input confirms the cause. If you mention a possible cause, label it as possible and unconfirmed. Problems that appear together do not prove a shared cause.

Only use numbers exactly as they appear in the input. Do not calculate, convert or round any number. If a number you would want is missing, say it is missing. Never estimate.

Do not invent queries, code, file names, links or people.

Choose severity by what the problem breaks, and give your reason in the Impact section:
- High: totals or key business numbers cannot be trusted, such as revenue, orders or conversion rates.
- Medium: one type of breakdown or analysis is affected, while totals are still correct.
- Low: little effect on any decision.

You will be given an example ticket inside <example_ticket> tags. Copy its sections, order and tone only. Never reuse its events, dates, numbers or references to past experience. Leave "Found by" and "Date found" blank for a person to fill in. Do not carry over any possible cause, impact, next step or acceptance criterion from the example.
"""


client = anthropic.Anthropic()


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


if __name__ == "__main__":
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
