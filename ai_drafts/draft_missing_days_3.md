# view_item_list has no data on 59 of 92 days from Nov 1 2020 to Jan 31 2021

**Event:** view_item_list
**Found by:** · **Date found:** · **Severity:** High

## Description
The `view_item_list` event has no rows on 59 of the 92 days between Nov 1, 2020 and Jan 31, 2021. On the 33 days that do have data, only 71 `view_item_list` events were received in total.

Other events were received on every one of the 59 days. Fourteen events have data on every day of the period, including `view_item`, `purchase` and `page_view`. This means the data feed was not empty on those days. However, the check results do not show why `view_item_list` has no rows. They also do not show whether item lists were actually viewed on those days.

Two other events also have no data on some of the same days. `add_to_cart` has no data on 4 of them, and `select_item` has no data on 6 of them. Each of these events also has gaps on other days. These overlaps do not show that the gaps share a cause.

## Evidence (Nov 1, 2020 – Jan 31, 2021)
- Data period: 92 days.
- `view_item_list` has no data on 59 of 92 days.
- 71 `view_item_list` events were received in total, across the 33 days with data.
- At least one other event was received on every day that has no `view_item_list` data.
- Events with data on every day of the period: `add_payment_info`, `add_shipping_info`, `begin_checkout`, `click`, `first_visit`, `page_view`, `purchase`, `scroll`, `select_promotion`, `session_start`, `user_engagement`, `view_item`, `view_promotion`, `view_search_results`.
- Dates with no `view_item_list` data:
  - Nov 12, 2020 to Nov 14, 2020
  - Nov 16, 2020 to Nov 17, 2020
  - Nov 19, 2020
  - Nov 24, 2020 to Nov 25, 2020
  - Nov 29, 2020
  - Dec 2, 2020 to Dec 3, 2020
  - Dec 5, 2020 to Dec 6, 2020
  - Dec 8, 2020 to Dec 9, 2020
  - Dec 13, 2020 to Jan 2, 2021
  - Jan 4, 2021 to Jan 8, 2021
  - Jan 11, 2021 to Jan 15, 2021
  - Jan 17, 2021 to Jan 22, 2021
  - Jan 24, 2021 to Jan 27, 2021
  - Jan 29, 2021 to Jan 31, 2021
- `add_to_cart` also has no data on 4 of these days:
  - Nov 12, 2020 to Nov 14, 2020
  - Nov 24, 2020
- `add_to_cart` has no data on 18 days across the whole period.
- `select_item` also has no data on 6 of these days:
  - Nov 12, 2020 to Nov 14, 2020
  - Nov 16, 2020 to Nov 17, 2020
  - Nov 19, 2020
- `select_item` has no data on 22 days across the whole period.
- The check results do not include a daily event count for `view_item_list`. They also do not include an expected daily volume for comparison.

## Impact
The tracking plan sets the severity as High.

This affects any count of item list views for the period. It also affects any measure that uses `view_item_list` as a step, such as:
- the rate at which list views lead to `select_item`, `view_item` or `add_to_cart`
- comparisons of list views across days or weeks

The longest gap runs from Dec 13, 2020 to Jan 2, 2021. Any comparison that includes that stretch is especially exposed.

The check results cannot tell whether no list views happened on those days or whether list views happened but were not received. Until that is known, `view_item_list` figures for this period should not be treated as complete. This also applies to the 33 days that have data, because rows on a day do not prove that day is complete.

One possible explanation is that `view_item_list` is only sent from certain pages or list types. Another is that the dataset contains only part of the full traffic. Neither has been confirmed.

## Suggested next steps
- Confirm where `view_item_list` is meant to be sent from, and whether it should appear on every day that item lists are shown.
- Find out whether item lists were shown to users on the 59 days with no data. One way is to check whether any other source records list views on those days.
- Check whether tracking for `view_item_list` was changed, added or removed at any point between Nov 1, 2020 and Jan 31, 2021.
- Look at the gaps in `add_to_cart` and `select_item` separately. Do not assume they share a cause with the `view_item_list` gaps, even where the dates overlap.
- Get the daily count of `view_item_list` events for the 33 days with data, and confirm whether those counts match what is expected.

## Acceptance criteria
- For every day in the period, `view_item_list` either has rows, or there is a confirmed and documented reason why no item list views occurred that day.
- The tracking plan states where `view_item_list` is expected to be sent from. This lets future gaps be judged against a clear expectation.
- Any analysis using `view_item_list` for Nov 1, 2020 to Jan 31, 2021 notes the 59 days with no data until those days are resolved.