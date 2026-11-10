# select_item has no data on 22 of 92 days, from Nov 1 to Nov 22, 2020

**Event:** select_item
**Found by:** · **Date found:** · **Severity:** Medium

## Description
An automated check flags any day in the data period when an event has no rows. The `select_item` event has no rows on any day from Nov 1, 2020 to Nov 22, 2020. That is 22 of the 92 days in the period from Nov 1, 2020 to Jan 31, 2021. Rows appear on the other 70 days.

The check results do not show whether item selections happened on these days and were not recorded, or did not happen at all. However, at least one other event was received on every one of these 22 days, so data was still arriving for this property during this time.

Two other events, `add_to_cart` and `view_item_list`, also have no data on some of these same dates. Because the gaps happen on some of the same dates, it is possible that the three gaps have a shared cause. This is unconfirmed. The check results do not show any cause for any of the gaps.

## Evidence (Nov 1, 2020 – Jan 31, 2021)
- Data period: Nov 1, 2020 to Jan 31, 2021 (92 days).
- `select_item` has no data on 22 of 92 days, covering Nov 1, 2020 to Nov 22, 2020.
- `select_item` total events received on the 70 days with data: 31007.
- At least one other event was received on every day that `select_item` has no data.
- These events have data on every day of the period: `add_payment_info`, `add_shipping_info`, `begin_checkout`, `click`, `first_visit`, `page_view`, `purchase`, `scroll`, `select_promotion`, `session_start`, `user_engagement`, `view_item`, `view_promotion`, `view_search_results`.
- `add_to_cart` also has no data on 16 of the 22 dates: Nov 2, 2020 to Nov 15, 2020, and Nov 21, 2020 to Nov 22, 2020. Across the whole period, `add_to_cart` has no data on 18 days. The check results do not list its other missing dates.
- `view_item_list` also has no data on 6 of the 22 dates: Nov 12, 2020 to Nov 14, 2020, Nov 16, 2020 to Nov 17, 2020, and Nov 19, 2020. Across the whole period, `view_item_list` has no data on 59 days. The check results do not list its other missing dates.

## Impact
Any analysis of `select_item` over the full period will be misleading. Item selections will appear to start on Nov 23, 2020. Counts, trends, or comparisons that include Nov 1–22, 2020 will show zero for those days. Funnel rates that use `select_item` as a step will also be affected for those dates. This includes rates that measure how often item selections lead to later steps.

The severity is Medium because the affected event is used for item selection and funnel step analysis. It does not directly feed revenue or order counts. The `purchase` event has rows on every day of the period. This only shows that purchases were received on each day. It does not show that purchase totals are complete or correct, and this check does not test that.

The gaps in `add_to_cart` and `view_item_list` may affect cart and item list analysis in the same way. Those gaps are listed here for context and may need their own review.

## Suggested next steps
- Confirm when `select_item` tracking started sending data. Find out whether it was introduced or changed around Nov 23, 2020, or whether it was expected to send data from Nov 1, 2020.
- Review the `add_to_cart` and `view_item_list` gaps alongside this one. Determine whether all three share a cause or are separate problems. Get the full list of missing dates for both events, since the check results only show the dates that fall within Nov 1–22, 2020.
- If the gap turns out to be a recording problem, check whether the Nov 1–22, 2020 data can be recovered.

## Acceptance criteria
- The cause of the `select_item` gap from Nov 1, 2020 to Nov 22, 2020 is confirmed and documented. The documentation states whether it was a tracking problem or the expected start date of the event.
- Re-running the missing days check on `select_item` for Nov 1, 2020 to Jan 31, 2021 shows no flagged days. If the data cannot be recovered, the gap is documented so that analyses using `select_item` start from Nov 23, 2020.