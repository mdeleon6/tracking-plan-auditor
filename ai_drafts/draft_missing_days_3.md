# `view_item_list` has no data on 59 of 92 days from Nov 1, 2020 to Jan 31, 2021

**Event:** view_item_list
**Found by:** · **Date found:** · **Severity:** High

## Description
The `view_item_list` event records when a user sees a list of products. According to the tracking plan, it feeds product list view reporting and the list-to-product step of the funnel.

An automated check flags any day in the data period when an event has no rows. From Nov 1, 2020 to Jan 31, 2021 (92 days), `view_item_list` has no rows on 59 days. Only 71 events were received across the 33 days that do have data. At least one other event was received on each of the 59 empty days, so these are not days when no data arrived at all.

The check results only show what was received. They cannot tell us whether users saw product lists on the empty days and the events were not recorded, or whether no product lists were viewed. The cause has not been confirmed.

## Evidence (Nov 1, 2020 – Jan 31, 2021)
- Days with no `view_item_list` data: 59 of 92.
- Total `view_item_list` events received on the 33 days with data: 71.
- Dates with no data:
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
- The first date with no data in the check results is Nov 12, 2020.
- At least one other event was received on every one of these dates.
- These events have data on every day of the period: add_payment_info, add_shipping_info, begin_checkout, click, first_visit, page_view, purchase, scroll, select_promotion, session_start, user_engagement, view_item, view_promotion, view_search_results.
- Two other events also have empty days that overlap with `view_item_list`:
  - **add_to_cart:** no data on Nov 12, 2020 to Nov 14, 2020 and on Nov 24, 2020. These are 4 of the `view_item_list` empty days. Across the whole period, add_to_cart has no data on 18 days. The check results do not list its other empty dates.
  - **select_item:** no data on Nov 12, 2020 to Nov 14, 2020, Nov 16, 2020 to Nov 17, 2020, and Nov 19, 2020. These are 6 of the `view_item_list` empty days. Across the whole period, select_item has no data on 22 days. The check results do not list its other empty dates.
- These events having empty days on the same dates does not prove they share a cause.

## Impact
The tracking plan uses `view_item_list` for product list views and for the list-to-product funnel step.

- **Empty days:** Product list views and the list-to-product step cannot be reported for the 59 empty days.
- **Days with data:** Receiving rows on the other 33 days does not show that those days are complete. No expected daily volume is included in the check results, so the 71 events received cannot be compared with anything.
- **Trends:** Any trend, total or conversion rate built on this event over this period is unreliable.

The severity is High, as set by the tracking plan. This rating fits because the list-to-product funnel step is a conversion rate, and that rate cannot be trusted for this period.

The check results do not say which other events, if any, make up the list-to-product funnel step. If select_item or add_to_cart is part of that step, it would also be affected on the overlapping days. This is possible but has not been confirmed.

## Suggested next steps
- **Expected behavior:** Confirm whether `view_item_list` should be sent on every day that users can see a product list. Find out whether product lists were available on the empty dates.
- **Tracking setup:** Review the event's tracking setup from Nov 12, 2020 onward. Check whether anything changed around the start of the gaps or on the dates where data comes and goes.
- **Expected volume:** Get an expected daily volume for `view_item_list`, which is missing from the check results. Use it to judge whether the 71 events on the 33 days with data are complete.
- **Re-pull:** Check whether data for the empty dates can be re-pulled or recovered.
- **Funnel definition:** Confirm which events make up the list-to-product funnel step, so it is clear whether select_item or add_to_cart gaps also affect it.
- **Other events:** List all empty dates for add_to_cart (18 days) and select_item (22 days), since the check results do not give them all. Investigate each event on its own rather than assuming one cause.

## Acceptance criteria
- `view_item_list` has rows on every day that users can view product lists, or each empty day is confirmed as having no product list views.
- The missing-days check no longer flags `view_item_list` for days when product lists were available.
- Until this is resolved, any report or analysis of product list views or the list-to-product funnel step for Nov 1, 2020 to Jan 31, 2021 clearly flags the 59 empty days and does not treat the days with data as complete.