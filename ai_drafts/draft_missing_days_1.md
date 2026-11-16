# `add_to_cart` has no data on 18 of 92 days from Nov 1, 2020 to Jan 31, 2021

**Event:** add_to_cart
**Found by:** · **Date found:** · **Severity:** High

## Description
The `add_to_cart` event has no rows on 18 of the 92 days between Nov 1, 2020 and Jan 31, 2021. The empty days fall in two date ranges: Nov 2–15, 2020 and Nov 21–24, 2020. At least one other event was received on every one of these days, so the data set as a whole is not empty on these dates. Several events tied to shopping and checkout, including `view_item`, `begin_checkout`, `add_shipping_info`, `add_payment_info` and `purchase`, were received on every day of the period.

The check results show only that no `add_to_cart` rows were received on these days. They do not show whether people added items to their carts on those days, so it is not known whether this is a tracking gap or a real lack of activity.

Two other events also have empty days that overlap with these dates: `select_item` and `view_item_list`. These events appear together on some dates, but that does not show they have a shared cause.

## Evidence (Nov 1, 2020 – Jan 31, 2021)
- Found by the automated missing-days check, which flags any day in the data period on which an event has no rows.
- `add_to_cart` has no data on 18 of 92 days:
  - Nov 2, 2020 to Nov 15, 2020
  - Nov 21, 2020 to Nov 24, 2020
- Total `add_to_cart` events received on the 74 days with data: 58543. The check results do not include daily counts, so it is not known whether volumes on those 74 days are complete or normal.
- At least one other event was received on every one of the 18 days.
- Events with data on every day of the period: `add_payment_info`, `add_shipping_info`, `begin_checkout`, `click`, `first_visit`, `page_view`, `purchase`, `scroll`, `select_promotion`, `session_start`, `user_engagement`, `view_item`, `view_promotion`, `view_search_results`.
- `select_item` also has no data on 16 of the 18 days: Nov 2, 2020 to Nov 15, 2020, and Nov 21, 2020 to Nov 22, 2020. Across the whole period, `select_item` has no data on 22 days.
- `view_item_list` also has no data on 4 of the 18 days: Nov 12, 2020 to Nov 14, 2020, and Nov 24, 2020. Across the whole period, `view_item_list` has no data on 59 days.
- The tracking plan sets the severity for this check to High.

## Impact
The tracking plan lists `add_to_cart` as an input to the add-to-cart rate, the cart-to-purchase conversion rate and the checkout funnel. These are key business numbers. On the 18 empty days, `view_item`, `begin_checkout` and `purchase` were all received but `add_to_cart` was not. Any of these numbers that covers these dates, whether for a single day or for the full period, cannot be trusted until the reason for the gap is known. The funnel would show people moving from viewing items to checkout and purchase with no add-to-cart step in between.

The severity is High, as set by the tracking plan. This rating fits the impact described above, because conversion rates depend directly on this event.

Rows on the other 74 days do not show that `add_to_cart` data is complete on those days. The total of 58543 events should not be treated as a full count for the period.

## Suggested next steps
- Confirm whether people added items to carts on Nov 2–15 and Nov 21–24, 2020, and whether `add_to_cart` events from those dates exist anywhere upstream and can be re-loaded.
- Check whether the empty days for `select_item` and `view_item_list` are linked to the `add_to_cart` gap or are separate issues. `view_item_list` has empty days well beyond these dates and may need its own ticket.
- Get daily `add_to_cart` counts for the full period to check whether the days around the two empty ranges show unusually low volumes. These counts are not in the check results.
- Until this is resolved, tell owners of the add-to-cart rate, cart-to-purchase conversion rate and checkout funnel reports which dates are affected.

## Acceptance criteria
- `add_to_cart` has rows on every day from Nov 1, 2020 to Jan 31, 2021, or the empty days are confirmed and documented as a real lack of add-to-cart activity.
- Until then, any report of add-to-cart rate, cart-to-purchase conversion rate or the checkout funnel that covers Nov 2–15 or Nov 21–24, 2020 excludes those dates or clearly flags them.