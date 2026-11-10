# add_to_cart has no data on 18 of 92 days from Nov 1, 2020 to Jan 31, 2021

**Event:** add_to_cart
**Found by:** · **Date found:** · **Severity:** High

## Description
The `add_to_cart` event has no rows on 18 of the 92 days between Nov 1, 2020 and Jan 31, 2021. The empty days fall in two blocks: Nov 2 to Nov 15, 2020 and Nov 21 to Nov 24, 2020. On every one of these days, at least one other event was received.

The check results do not show whether no one added items to a cart on these days or whether the activity happened and was not received. They also do not show why the gap exists.

Two other events also have empty days that overlap with the `add_to_cart` gap: `select_item` and `view_item_list`. Both events also have empty days outside the `add_to_cart` gap. The overlap does not show that these gaps share a cause.

## Evidence (Nov 1, 2020 – Jan 31, 2021)
- Data period: Nov 1, 2020 to Jan 31, 2021 (92 days).
- `add_to_cart` has no data on 18 of 92 days.
- `add_to_cart` had 58543 events in total across the 74 days with data.
- Dates with no `add_to_cart` data:
  - Nov 2, 2020 to Nov 15, 2020
  - Nov 21, 2020 to Nov 24, 2020
- At least one other event was received on every one of these 18 days.
- These events have data on every day of the period: `add_payment_info`, `add_shipping_info`, `begin_checkout`, `click`, `first_visit`, `page_view`, `purchase`, `scroll`, `select_promotion`, `session_start`, `user_engagement`, `view_item`, `view_promotion`, `view_search_results`.
- `select_item` also has no data on 16 of the 18 days: Nov 2, 2020 to Nov 15, 2020, and Nov 21, 2020 to Nov 22, 2020. Across the whole period, `select_item` has no data on 22 days.
- `view_item_list` also has no data on 4 of the 18 days: Nov 12, 2020 to Nov 14, 2020, and Nov 24, 2020. Across the whole period, `view_item_list` has no data on 59 days.
- The check results do not include daily `add_to_cart` counts for the 74 days with data. They do not include an expected daily volume either. Without these, it is not possible to say how unusual the gap is or whether the 58543 total is complete.

## Impact
The tracking plan sets this severity at High. This ticket keeps that rating.

The following uses of `add_to_cart` are affected for Nov 2–15 and Nov 21–24, 2020:
- **Cart counts:** any count of cart additions that includes these dates.
- **Daily trends:** any daily or weekly trend of cart additions that covers these dates.
- **Conversion rates:** any rate built on cart additions for these dates, such as view-to-cart or cart-to-checkout.

The other funnel events `view_item`, `begin_checkout` and `purchase` were received on all of these days. This means that funnel steps before and after `add_to_cart` have rows on dates when `add_to_cart` has none. As a result, any funnel that uses `add_to_cart` for these dates will not be consistent from step to step.

The 58543 total only covers the 74 days with data. The check results do not show whether `add_to_cart` data on those 74 days is complete, so that total should not be treated as confirmed.

## Suggested next steps
- **Find out whether `add_to_cart` should have been sent on these dates.** Check whether the event was live and expected to fire on Nov 2–15 and Nov 21–24, 2020.
- **Look for changes around the gap.** Check for releases, tag changes or tracking configuration changes near the start and end of each block: Nov 2, Nov 15, Nov 21 and Nov 24, 2020. Any link between such a change and the gap is a possible cause only and is not confirmed.
- **Check whether the data can be recovered.** Find out whether `add_to_cart` activity for these dates exists anywhere else and can be re-sent or re-pulled. If it is re-pulled, run the missing-days check again.
- **Get the missing daily counts.** Pull daily `add_to_cart` counts for the full period and compare the days around each gap. This will show whether volume drops or changes before or after the empty days.
- **Investigate `select_item` and `view_item_list` separately.** Each has empty days outside the `add_to_cart` gap: 22 days in total for `select_item` and 59 for `view_item_list`. Look into each one on its own rather than assuming a shared cause.

## Acceptance criteria
- For each of the 18 dates, one of the following is true:
  - `add_to_cart` has rows for that date.
  - It is documented and confirmed that no `add_to_cart` activity was expected on that date.
- Until this is resolved, any count, trend or conversion rate that uses `add_to_cart` either excludes or clearly flags Nov 2–15 and Nov 21–24, 2020.