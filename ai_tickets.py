from pathlib import  Path
import anthropic


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


if __name__ == "__main__":
    problem = """
Check: required field coverage. A field is flagged when coverage is below 0.99.
Event: purchase
Share of purchase events missing each field: 7.9058%. Gap to threshold: 6.9058 percentage points.
Flagged fields, all with coverage_rate 0.920942:
- transaction_id (location: event_params)
- value (location: event_params)
- purchase_revenue (location: ecommerce)
- tax (location: event_params)
- payment_type (location: event_params)
"""
    print(draft_ticket(problem))
