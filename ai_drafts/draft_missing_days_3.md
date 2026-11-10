# view_item_list has no data on 59 of 92 days from Nov 1 2020 to Jan 31 2021

**Event:** view_item_list
**Found by:** · **Date found:** · **Severity:** Medium

## Description
The `view_item_list` event has no rows on 59 of the 92 days between Nov 1, 2020 and Jan 31, 2021. On the 33 days that do have data, only 71 `view_item_list` events were received in total.

The dataset was not empty on these days. At least one other event was received on every one of the 59 days. Fourteen other events have data on every day of the period, including `view_item`, `page_view`, `session_start` and `purchase`.

Two other events, `add_to_cart` and `select_item`, also have no data on some of the same days. This overlap does not show that the gaps share a cause.

The check results show only what was received. They cannot tell us whether people viewed item lists on the 59 days with no data.

## Evidence (Nov 1, 2020 – Jan 31, 2021)
- `view_item_list` has no data on 59 of 92 days.
- `view_item_list` has 71 events in total across the 33 days with data.
- On every day with no `view_item_list` data, at least one other event was received.
- These events have data on every day of the period: `add_payment_info`, `add_shipping_info`, `begin_checkout`, `click`, `first_visit`, `page_view`, `purchase`, `scroll`, `select_promotion`, `session_start`, `user_engagement`, `view_item`, `view_promotion`, `view_search_results`.
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
- No date before Nov 12, 2020 appears in the list of missing dates. From that date on, the missing dates become frequent and include one unbroken run from Dec 13, 2020 to Jan 2, 2021.
- `add_to_cart` also has no data on 4 of these days: Nov 12, 2020 to Nov 14, 2020, and Nov 24, 2020. Across the whole period, `add_to_cart` has no data on 18 days. The check results do not list its other missing dates.
- `select_item` also has no data on 6 of these days: Nov 12, 2020 to Nov 14, 2020, Nov 16, 2020 to Nov 17, 2020, and Nov 19, 2020. Across the whole period, `select_item` has no data on 22 days. The check results do not list its other missing dates.

## Impact
Any analysis built on `view_item_list` cannot be trusted for this period. This includes:
- counts of item list views
- comparisons of item lists
- any funnel step that starts from an item list view

A day with no data will look like a day with no list views, and the check results cannot confirm whether that is true. The check results also give no expected daily volume for this event, so we cannot tell whether 71 events on the days with data is a normal amount or a low one.

The severity is Medium because `view_item_list` is a browsing event and does not directly feed totals such as revenue or orders. This check found no missing days for `purchase`. However, having rows on every day does not show that purchase data is complete, so this ticket makes no claim that those totals are correct.

If any reported conversion rate uses `view_item_list` as its starting point, that rate is unreliable for this period. In that case, the severity should be raised to High.

The partial overlap with `add_to_cart` and `select_item` means that analysis of the steps between browsing a list and adding to cart may be affected beyond `view_item_list` alone. It is possible but unconfirmed that these gaps are related.

## Suggested next steps
- Confirm whether `view_item_list` is expected to be received every day, and roughly how many events per day would be normal.
- Find out whether anything changed in how `view_item_list` was sent around Nov 12, 2020, the first missing date. Then check whether the same change applies to the run from Dec 13, 2020 to Jan 2, 2021.
- Check whether the pages or screens that show item lists were available on the days with no data. This would help separate a tracking problem from a real absence of list views.
- Get the full list of missing dates for `add_to_cart` (18 days) and `select_item` (22 days). Compare them with the `view_item_list` gaps to see whether the overlap goes beyond the days listed here.
- Decide whether the `add_to_cart` and `select_item` gaps need their own tickets.

## Acceptance criteria
- For every day in the period, `view_item_list` either has data or the team has written confirmation of why no item list views were expected that day.
- An expected daily volume for `view_item_list` is documented, and the received counts are checked against it.
- The missing dates for `add_to_cart` and `select_item` are listed in full and either explained or tracked in separate tickets.
- Until this is resolved, any analysis or conversion rate that uses `view_item_list` for Nov 1, 2020 to Jan 31, 2021 is labeled as based on incomplete data.