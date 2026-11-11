# add_to_cart arrived at low volume on 6 days and not at all on two date ranges between Nov 1, 2020 and Jan 3, 2021

**Event:** add_to_cart
**Found by:** · **Date found:** · **Severity:** High

## Description
The low-volume check flagged 6 days where `add_to_cart` arrived at less than half its usual count. The usual count is the median count for the same weekday. On 2 of these days, Nov 1 and Nov 20, 2020, the count was under 3% of typical.

The check results also show two date ranges with no `add_to_cart` data at all: Nov 2 to Nov 15, 2020, and Nov 21 to Nov 24, 2020. Several flagged days sit right next to these ranges:
- Nov 1 is the day before the first range.
- Nov 16 is the day after the first range ends.
- Nov 20 is the day before the second range.
- Nov 25 is the day after the second range ends.

The check results do not explain the low counts or the missing days. They only show what was received. They do not show whether customers stopped adding items to their carts on these days or whether the events were not recorded or delivered.

## Evidence (Nov 1, 2020 – Jan 3, 2021)
- Check rule: a day is flagged when its count is below 0.5 of the median count for that weekday.
- Nov 1, 2020: 4 events, typical 473 (0.8% of typical).
- Nov 2 – Nov 15, 2020: no data.
- Nov 16, 2020: 85 events, typical 585 (14.5% of typical).
- Nov 19, 2020: 187 events, typical 642 (29.1% of typical).
- Nov 20, 2020: 15 events, typical 572 (2.6% of typical).
- Nov 21 – Nov 24, 2020: no data.
- Nov 25, 2020: 297 events, typical 665 (44.7% of typical).
- Jan 3, 2021: 229 events, typical 473 (48.4% of typical).
- Holidays: the check results do not name a holiday next to any of the 6 flagged dates, so none of them is on the tracking plan's holiday calendar. The two date ranges with no data were not checked against the calendar.

## Impact
`add_to_cart` counts cannot be trusted for the flagged days or the days with no data. Any total covering part of Nov 1, 2020 – Jan 3, 2021 may also be affected. This includes:
- Daily, weekly or monthly add-to-cart totals.
- Funnel and conversion rates that use `add_to_cart` as a step, such as visit-to-cart or cart-to-purchase rates.

These rates could look unusually low or high depending on which step is missing events. The check results do not show whether the days that were not flagged are complete, so this ticket makes no claim that totals outside these dates are correct.

The tracking plan rates this event High if it stops arriving entirely. The check results show stretches where no `add_to_cart` data arrived at all, so that rating applies. The severity rules lead to the same result: conversion rates are key business numbers, and they cannot be trusted while `add_to_cart` volume is this incomplete. This ticket is therefore High.

## Suggested next steps
- Find out whether `add_to_cart` was being sent between Nov 2 and Nov 15, 2020, and between Nov 21 and Nov 24, 2020.
- Check whether the very low counts on Nov 1, Nov 16, Nov 20 and Nov 25 are partial days at the edges of the no-data ranges. This is a possible explanation and has not been confirmed.
- Check whether any tracking, release or pipeline change happened around these dates. No cause has been confirmed.
- Compare other events on the same dates to see whether the drop is limited to `add_to_cart`. The check results only cover `add_to_cart`, so whether other events are affected is unknown.
- Find out whether the missing or low-volume days can be re-pulled or backfilled.
- Look into Nov 19 and Jan 3 separately. These days are not next to a no-data range, and nothing in the check results explains them.

## Acceptance criteria
- Each of the 6 flagged days either rises to at least 0.5 of its typical count after any re-pull or backfill, or has a documented explanation.
- Nov 2 – Nov 15, 2020 and Nov 21 – Nov 24, 2020 are either backfilled or documented as unrecoverable.
- Any add-to-cart totals or conversion rates for Nov 1, 2020 – Jan 3, 2021 exclude or clearly flag the affected days until the issue is resolved.
- Re-running the low-volume check on `add_to_cart` for this period leaves no flagged or no-data days without an explanation.