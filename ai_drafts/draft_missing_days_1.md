# `add_to_cart` has no data on 18 of 92 days from Nov 1, 2020 to Jan 31, 2021

**Event:** add_to_cart
**Found by:** · **Date found:** · **Severity:** High

## Description
The `add_to_cart` event has no rows on 18 of the 92 days in the data period. The empty days fall in two blocks: Nov 2–15, 2020 and Nov 21–24, 2020. Other events were received on every one of those days, so the dataset as a whole was not empty on those dates.

Two other events, `select_item` and `view_item_list`, also have no rows on some of the same days.

The check results only show which days have rows. They do not show whether customers added items to their carts on the empty days. The cause of the gaps is unknown.

## Evidence (Nov 1, 2020 – Jan 31, 2021)
- `add_to_cart` has no data on 18 of 92 days.
- Dates with no `add_to_cart` data:
  - Nov 2, 2020 to Nov 15, 2020
  - Nov 21, 2020 to Nov 24, 2020
- On the 74 days with data, 58543 `add_to_cart` events were received.
- At least one other event was received on every day that `add_to_cart` has no data.
- These events have data on every day of the period: `add_payment_info`, `add_shipping_info`, `begin_checkout`, `click`, `first_visit`, `page_view`, `purchase`, `scroll`, `select_promotion`, `session_start`, `user_engagement`, `view_item`, `view_promotion`, `view_search_results`.
- `select_item` also has no data on 16 of the 18 empty days: Nov 2, 2020 to Nov 15, 2020 and Nov 21, 2020 to Nov 22, 2020. Across the whole period, `select_item` has no data on 22 days.
- `view_item_list` also has no data on 4 of the 18 empty days: Nov 12, 2020 to Nov 14, 2020 and Nov 24, 2020. Across the whole period, `view_item_list` has no data on 59 days.
- No query or source reference was included in the check results.

## Impact
Until the empty days are explained, `add_to_cart` totals for this period cannot be trusted. Any conversion rate that uses `add_to_cart` cannot be trusted either. Examples are the share of product views that lead to an add to cart, or the share of carts that lead to a checkout or purchase. If the empty days come from a recording problem, these rates would be wrong for the affected dates. If they reflect real behavior, the rates would be correct. The check results cannot tell these apart.

This is **High** severity because it affects a key funnel conversion step. Trends over time are also affected. Any daily or weekly chart of `add_to_cart` will show drops to zero in early and late November. Nobody can yet say whether those drops are real.

The 74 days that do have data are not confirmed complete. Having rows on a day does not show that every event on that day was recorded.

`select_item` and `view_item_list` have gaps on some of the same days. This overlap does not prove that the three events share a cause. `select_item` and `view_item_list` also have empty days outside these 18 dates, so their gaps may need separate investigation.

## Suggested next steps
- Find out whether customers could add items to their cart on Nov 2–15, 2020 and Nov 21–24, 2020. For example, check whether the cart feature was unavailable, changed or under maintenance on those dates.
- Check for any tracking or site releases around the start and end of each empty block, especially near Nov 2, Nov 16, Nov 21 and Nov 25, 2020. A tracking change is a possible cause, but this is unconfirmed.
- Find out whether `add_to_cart` events for the empty days still exist anywhere, such as in the original collection system, and could be reloaded.
- Investigate whether the gaps in `select_item` and `view_item_list` are related to the `add_to_cart` gaps or separate. Include the `select_item` and `view_item_list` empty days that fall outside these 18 dates.
- Check whether the 74 days with `add_to_cart` data are complete, especially the days just before and after each empty block.

## Acceptance criteria
- Each of the 18 empty days is either explained as a real absence of add-to-cart activity, with that explanation documented, or filled in with recovered `add_to_cart` data.
- Until then, any analysis or report using `add_to_cart` for Nov 1, 2020 to Jan 31, 2021 either excludes Nov 2–15, 2020 and Nov 21–24, 2020 or clearly marks those dates as missing data.
- The relationship between the `add_to_cart`, `select_item` and `view_item_list` gaps is confirmed and recorded, whether they share a cause or not.