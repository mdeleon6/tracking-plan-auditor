# 13 events below 0.5 of their typical count on 7 days between Dec 24, 2020 and Jan 18, 2021, including purchase and checkout events

**Event:** multiple events (13)
**Found by:** · **Date found:** · **Severity:** High

## Description
An automated check found 7 days where at least 5 events each arrived at below 0.5 of their typical count. The typical count is the median for that weekday. 13 different events are affected across these days. They include `purchase`, `begin_checkout`, `add_shipping_info` and `add_payment_info`, which the tracking plan rates High.

The affected events are `add_payment_info`, `add_shipping_info`, `begin_checkout`, `click`, `page_view`, `purchase`, `scroll`, `select_item`, `select_promotion`, `user_engagement`, `view_item`, `view_promotion` and `view_search_results`.

`add_payment_info` and `add_shipping_info` are below the threshold on every listed day. `purchase` is below the threshold on every listed day except Dec 30, 2020.

The check results only show how many events were received. They do not show whether the low counts reflect lower real activity or events that were not collected. The cause has not been confirmed.

## Evidence (Dec 24, 2020 – Jan 18, 2021, listed days only)
Each value is the event's count on that day as a percentage of its typical count.

- **Dec 24, 2020** (on the tracking plan's holiday calendar as Christmas Eve, widely observed): 8 events below threshold. `add_payment_info` 34.6%, `add_shipping_info` 32.3%, `click` 27.3%, `page_view` 45.3%, `purchase` 42.6%, `user_engagement` 43.0%, `view_item` 46.1%, `view_promotion` 46.4%.
- **Dec 25, 2020** (Christmas Day, widely observed): 9 events below threshold. `add_payment_info` 24.9%, `add_shipping_info` 25.3%, `click` 46.7%, `page_view` 37.9%, `purchase` 21.5%, `scroll` 37.2%, `user_engagement` 35.0%, `view_item` 31.4%, `view_promotion` 37.7%.
- **Dec 30, 2020** (not on the holiday calendar): 5 events below threshold. `add_payment_info` 32.1%, `add_shipping_info` 37.5%, `user_engagement` 42.8%, `view_item` 35.0%, `view_promotion` 45.7%.
- **Dec 31, 2020** (New Year's Eve, widely observed): 9 events below threshold. `add_payment_info` 44.1%, `add_shipping_info` 43.1%, `purchase` 46.3%, `scroll` 41.1%, `select_item` 39.9%, `select_promotion` 46.7%, `user_engagement` 36.5%, `view_item` 33.3%, `view_promotion` 39.6%.
- **Jan 1, 2021** (New Year's Day, widely observed): 10 events below threshold. `add_payment_info` 17.5%, `add_shipping_info` 20.1%, `begin_checkout` 42.3%, `click` 13.3%, `purchase` 17.7%, `scroll` 35.4%, `user_engagement` 34.3%, `view_item` 28.7%, `view_promotion` 38.5%, `view_search_results` 49.7%.
- **Jan 4, 2021** (not on the holiday calendar): 5 events below threshold. `add_payment_info` 36.2%, `add_shipping_info` 28.9%, `click` 20.0%, `purchase` 30.2%, `view_item` 44.8%.
- **Jan 18, 2021** (Martin Luther King Jr. Day, observed as a day off in the US only): 5 events below threshold. `add_payment_info` 31.9%, `add_shipping_info` 35.5%, `click` 40.0%, `purchase` 35.8%, `view_item` 41.3%.

**Missing from the check results:**
- The raw event counts and the typical (median) counts behind these percentages.
- Counts for events that stayed above the threshold on these days.
- Any breakdown by country or platform.
- Tracking plan ratings for the 9 affected events that are not rated High.

## Impact
Severity is High because `purchase` is below the threshold on 6 of the 7 listed days. According to the tracking plan, `purchase` feeds orders, revenue, conversion rate, and revenue and conversion by country and platform. `begin_checkout`, `add_shipping_info` and `add_payment_info` feed the checkout funnel and checkout conversion rate by country and platform. Until the low counts are explained, these key numbers cannot be trusted for the listed days, or for any period or comparison that includes them.

Five of the listed days are on the tracking plan's holiday calendar. Lower activity on those days is a possible explanation, but it has not been confirmed. Jan 18, 2021 is observed as a day off in the US only. The check results have no country breakdown, so it is unknown whether the low counts on that day are limited to the US.

Dec 30, 2020 and Jan 4, 2021 are not on the holiday calendar, and the check results give no explanation for them.

The events appearing together on the same days does not show that they share a cause.

## Suggested next steps
- Get the raw counts and typical (median) counts for each affected event on each listed day, so the size of the drop can be seen in real numbers rather than only percentages.
- Compare `purchase` counts on the listed days against a record of orders kept outside the tracking data, if one exists. This would show whether orders really dropped or were not tracked.
- Prioritise Dec 30, 2020 and Jan 4, 2021, since neither is on the holiday calendar. Check whether any tracking or site changes were made around those dates.
- Break down Jan 18, 2021 by country to see whether the low counts are limited to the US, where the holiday is observed.
- On Dec 30, 2020, `add_payment_info` and `add_shipping_info` are below the threshold but `purchase` is not listed. Check whether the checkout events and `purchase` move together on that day.
- Confirm the tracking plan ratings for the 9 affected events that are not rated High.

## Acceptance criteria
- For each of the 7 listed days, the low counts are either confirmed as real lower activity, with the supporting evidence documented, or identified as a tracking gap with a documented cause.
- Any tracking gap that is found has been fixed or backfilled, or the affected days are flagged as incomplete for every report that uses `purchase`, `begin_checkout`, `add_shipping_info` or `add_payment_info`.
- Raw and typical counts for every affected event on every listed day are recorded with this ticket.