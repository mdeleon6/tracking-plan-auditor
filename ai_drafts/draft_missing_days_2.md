# `select_item` has no data from Nov 1, 2020 to Nov 22, 2020

**Event:** select_item
**Found by:** · **Date found:** · **Severity:** Medium

## Description
The automated missing-days check found no `select_item` rows on 22 of the 92 days in the data period (Nov 1, 2020 to Jan 31, 2021). All 22 days fall in one unbroken stretch, Nov 1, 2020 to Nov 22, 2020.

The check results only show what was received. They do not show whether users selected items on these days. They also do not show that the data on the other 70 days is complete.

Two other events also have days with no data inside this stretch: `add_to_cart` and `view_item_list`. These gaps happened at the same time, but the check results do not show that they share a cause.

## Evidence (Nov 1, 2020 – Jan 31, 2021)
- Data period: Nov 1, 2020 to Jan 31, 2021 (92 days).
- `select_item` has no data on 22 of 92 days: Nov 1, 2020 to Nov 22, 2020.
- `select_item` has 31007 events in total across the 70 days that have data.
- At least one other event was received on every one of the 22 days. Data was still arriving for other events on these days.
- These events have data on every day of the period: add_payment_info, add_shipping_info, begin_checkout, click, first_visit, page_view, purchase, scroll, select_promotion, session_start, user_engagement, view_item, view_promotion, view_search_results.
- `add_to_cart` also has no data on 16 of the 22 days:
  - Nov 2, 2020 to Nov 15, 2020
  - Nov 21, 2020 to Nov 22, 2020
  - Across the whole period, `add_to_cart` has no data on 18 days. The check results do not list the dates outside this stretch.
- `view_item_list` also has no data on 6 of the 22 days:
  - Nov 12, 2020 to Nov 14, 2020
  - Nov 16, 2020 to Nov 17, 2020
  - Nov 19, 2020
  - Across the whole period, `view_item_list` has no data on 59 days. The check results do not list the dates outside this stretch.
- The check results do not include daily event counts. They do not include any queries or code.

## Impact
The tracking plan says `select_item` is used for two things:
- the product list click-through rate
- item selection reporting

Both will show nothing for Nov 1, 2020 to Nov 22, 2020. This could look like users made no item selections in that time, when the check results only show that no events were received. Comparisons across the full period, and trends that start before Nov 23, 2020, will be misleading.

The product list click-through rate may also be affected by the `view_item_list` gaps if that event is used in the calculation. That event has no data on 59 days. The check results do not say how the rate is calculated.

The severity is Medium as set by the tracking plan. This is consistent with what the problem breaks. `select_item` feeds an engagement rate and item selection reporting. According to the check results, it does not feed revenue, orders or units sold. `purchase` has data on every day of the period.

A possible explanation is that `select_item` was not yet being sent before late November 2020. This is possible and unconfirmed.

## Suggested next steps
- Confirm with the team that owns the tracking setup when `select_item` started being sent. Find out whether Nov 1, 2020 to Nov 22, 2020 was before a planned launch or a period when tracking was broken.
- Check whether `select_item` data for Nov 1, 2020 to Nov 22, 2020 exists anywhere upstream and could be re-loaded.
- Investigate the `add_to_cart` gaps (18 days) and the `view_item_list` gaps (59 days) in separate tickets. Do not assume they share a cause with this gap.
- Confirm how the product list click-through rate is calculated. Find out whether it depends on `view_item_list` as well as `select_item`.

## Acceptance criteria
One of the following is true:
- `select_item` has rows on every day of Nov 1, 2020 to Jan 31, 2021.
- The Nov 1, 2020 to Nov 22, 2020 gap is confirmed and documented as a known gap. The documentation records whether this was before tracking started or was lost data.

In addition, until the gap is resolved, product list click-through rate and item selection reporting exclude or clearly flag Nov 1, 2020 to Nov 22, 2020.