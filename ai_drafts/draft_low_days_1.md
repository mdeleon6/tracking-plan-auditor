# Low volume in 13 events, including `purchase` and checkout steps, on 7 days from Dec 24, 2020 to Jan 18, 2021

**Event:** multiple events (13)
**Found by:** · **Date found:** · **Severity:** High

## Description
On 7 days between Dec 24, 2020 and Jan 18, 2021, at least 5 events each arrived at less than 0.5 of their typical count. The typical count is the median for that weekday. In total, 13 different events were affected.

Four of the affected events are rated High in the tracking plan: `purchase`, `add_payment_info`, `add_shipping_info` and `begin_checkout`. `purchase` was below threshold on 6 of the 7 days. `add_payment_info` and `add_shipping_info` were below threshold on all 7 days.

The check results only show how many events were received. They do not show whether these drops reflect real lower activity or events that were not recorded. The cause has not been confirmed.

## Evidence (Dec 24, 2020 – Jan 18, 2021)
Rule: a day is listed when at least 5 events are each below 0.5 of their typical count (the median for that weekday). The figures below are each event's count as a percentage of its typical count.

**Days below threshold for each event, out of the 7 days listed:**
- 7 days: add_payment_info, add_shipping_info, view_item
- 6 days: purchase
- 5 days: click, user_engagement, view_promotion
- 3 days: scroll
- 2 days: page_view
- 1 day: begin_checkout, select_item, select_promotion, view_search_results

**Each day:**
- **Dec 24, 2020** (Christmas Eve on the tracking plan's holiday calendar, widely observed): 8 events below threshold. add_payment_info 34.6%, add_shipping_info 32.3%, click 27.3%, page_view 45.3%, purchase 42.6%, user_engagement 43.0%, view_item 46.1%, view_promotion 46.4%.
- **Dec 25, 2020** (Christmas Day on the calendar, widely observed): 9 events below threshold. add_payment_info 24.9%, add_shipping_info 25.3%, click 46.7%, page_view 37.9%, purchase 21.5%, scroll 37.2%, user_engagement 35.0%, view_item 31.4%, view_promotion 37.7%.
- **Dec 30, 2020** (not on the calendar): 5 events below threshold. add_payment_info 32.1%, add_shipping_info 37.5%, user_engagement 42.8%, view_item 35.0%, view_promotion 45.7%. `purchase` is not listed for this day.
- **Dec 31, 2020** (New Year's Eve on the calendar, widely observed): 9 events below threshold. add_payment_info 44.1%, add_shipping_info 43.1%, purchase 46.3%, scroll 41.1%, select_item 39.9%, select_promotion 46.7%, user_engagement 36.5%, view_item 33.3%, view_promotion 39.6%.
- **Jan 1, 2021** (New Year's Day on the calendar, widely observed): 10 events below threshold. add_payment_info 17.5%, add_shipping_info 20.1%, begin_checkout 42.3%, click 13.3%, purchase 17.7%, scroll 35.4%, user_engagement 34.3%, view_item 28.7%, view_promotion 38.5%, view_search_results 49.7%.
- **Jan 4, 2021** (not on the calendar): 5 events below threshold. add_payment_info 36.2%, add_shipping_info 28.9%, click 20.0%, purchase 30.2%, view_item 44.8%.
- **Jan 18, 2021** (Martin Luther King Jr. Day on the calendar, observed in the US only): 5 events below threshold. add_payment_info 31.9%, add_shipping_info 35.5%, click 40.0%, purchase 35.8%, view_item 41.3%.

**Not in the check results:**
- The actual event counts and the typical counts behind these percentages.
- Any split by country or platform.

## Impact
According to the tracking plan, `purchase` is used for orders, revenue, conversion rate, and revenue and conversion by country and platform. `add_payment_info`, `add_shipping_info` and `begin_checkout` are used for the checkout funnel and for checkout conversion rate by country and platform.

On the listed days, these key numbers cannot be trusted until it is confirmed whether the low counts reflect real activity. The same applies to any total that includes these days. This is why the severity is High. If events were not recorded, orders, revenue and conversion would be understated for those days.

The checkout steps did not always drop together, so funnel conversion rates on these days may also be distorted. For example, on Dec 30, 2020, `add_payment_info` and `add_shipping_info` were below threshold, but `purchase` and `begin_checkout` are not listed. The check results do not show whether this pattern reflects real behavior or missing data.

Five of the days have a holiday next to them on the tracking plan's calendar. Lower activity on those holidays is a possible explanation, but it is unconfirmed. Dec 30, 2020 and Jan 4, 2021 have no holiday on the calendar, so the check results offer no possible explanation for those two days.

These problems appear on several days and across many events. That does not show they share a cause.

## Suggested next steps
- For each of the 7 days, compare `purchase` counts with a record of orders kept outside this tracking data, if one exists. This would show whether the low counts reflect fewer orders or orders that were not tracked.
- Pull the actual counts and typical counts for each affected event and day. These numbers are not in the check results.
- Split the affected events by country and platform for each listed day. This would show whether the drops are limited to one segment.
- For Jan 18, 2021, check whether the drop is concentrated in US traffic. The calendar lists Martin Luther King Jr. Day as observed in the US only.
- Investigate Dec 30, 2020 and Jan 4, 2021 first, because the calendar has no holiday on those days. Look for tracking changes, releases or outages on or around those dates.
- Check why the checkout steps dropped by different amounts on the same days. For example, on Dec 30, 2020, `add_payment_info` and `add_shipping_info` were below threshold, but `purchase` and `begin_checkout` are not listed.

## Acceptance criteria
- For each of the 7 days, the low counts are either:
  - confirmed as real lower activity, with the supporting evidence recorded, or
  - identified as missing data, with the affected events recovered or the days clearly flagged for anyone reporting orders, revenue, conversion or the checkout funnel.
- The actual and typical counts for every affected event and day are documented alongside this ticket.
- Dec 30, 2020 and Jan 4, 2021 each have a confirmed explanation.