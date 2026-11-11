# 13 events fell below 0.5 of their typical count on 7 days between Dec 24, 2020 and Jan 18, 2021

**Event:** multiple events (13)
**Found by:** · **Date found:** · **Severity:** High

## Description
An automated check flags any day when at least 5 events each arrive at less than 0.5 of their typical count. The typical count is the median for that weekday. The check flagged 7 days between Dec 24, 2020 and Jan 18, 2021, involving 13 different events.

The affected events are add_payment_info, add_shipping_info, begin_checkout, click, page_view, purchase, scroll, select_item, select_promotion, user_engagement, view_item, view_promotion and view_search_results.

Four of these events are rated High in the tracking plan if they stop arriving entirely: add_payment_info, add_shipping_info, begin_checkout and purchase.

- add_payment_info and add_shipping_info are below threshold on all 7 listed days.
- purchase is below threshold on every listed day except Dec 30, 2020.
- begin_checkout is below threshold only on Jan 1, 2021.

Five of the 7 days have a holiday name next to them from the tracking plan's holiday calendar. Dec 30, 2020 and Jan 4, 2021 are not on that calendar. A holiday is a possible explanation for lower activity, but it has not been confirmed for any of these days. The check results also do not show whether the low counts reflect real lower activity or data that was not received.

## Evidence (Dec 24, 2020 – Jan 18, 2021)
Each figure is the event's count on that day as a percentage of its typical count.

- **Dec 24, 2020** (Christmas Eve: widely observed). 8 events below threshold:
  - add_payment_info 34.6%
  - add_shipping_info 32.3%
  - click 27.3%
  - page_view 45.3%
  - purchase 42.6%
  - user_engagement 43.0%
  - view_item 46.1%
  - view_promotion 46.4%
- **Dec 25, 2020** (Christmas Day: widely observed). 9 events below threshold:
  - add_payment_info 24.9%
  - add_shipping_info 25.3%
  - click 46.7%
  - page_view 37.9%
  - purchase 21.5%
  - scroll 37.2%
  - user_engagement 35.0%
  - view_item 31.4%
  - view_promotion 37.7%
- **Dec 30, 2020** (not on the holiday calendar). 5 events below threshold:
  - add_payment_info 32.1%
  - add_shipping_info 37.5%
  - user_engagement 42.8%
  - view_item 35.0%
  - view_promotion 45.7%
- **Dec 31, 2020** (New Year's Eve: widely observed). 9 events below threshold:
  - add_payment_info 44.1%
  - add_shipping_info 43.1%
  - purchase 46.3%
  - scroll 41.1%
  - select_item 39.9%
  - select_promotion 46.7%
  - user_engagement 36.5%
  - view_item 33.3%
  - view_promotion 39.6%
- **Jan 1, 2021** (New Year's Day: widely observed). 10 events below threshold:
  - add_payment_info 17.5%
  - add_shipping_info 20.1%
  - begin_checkout 42.3%
  - click 13.3%
  - purchase 17.7%
  - scroll 35.4%
  - user_engagement 34.3%
  - view_item 28.7%
  - view_promotion 38.5%
  - view_search_results 49.7%
- **Jan 4, 2021** (not on the holiday calendar). 5 events below threshold:
  - add_payment_info 36.2%
  - add_shipping_info 28.9%
  - click 20.0%
  - purchase 30.2%
  - view_item 44.8%
- **Jan 18, 2021** (Martin Luther King Jr. Day: US only). 5 events below threshold:
  - add_payment_info 31.9%
  - add_shipping_info 35.5%
  - click 40.0%
  - purchase 35.8%
  - view_item 41.3%

**Missing from the check results:**
- The actual event counts and typical counts. Only percentages are given.
- A breakdown by country or platform.
- Whether any affected event was close to the threshold on days that were not flagged.

## Impact
The tracking plan uses the four High-rated events as follows:
- **purchase:** orders, revenue, conversion rate, and revenue and conversion by country and platform.
- **add_payment_info, add_shipping_info and begin_checkout:** the checkout funnel, and checkout conversion rate by country and platform.

The tracking plan's High rating applies only if an event stops arriving entirely. On these days the events did not stop; each one still arrived at some level. So High is the highest severity allowed here, not an automatic rating.

The severity is High under the general rules. The check results cannot tell us whether the low counts reflect real activity or data that was not received. Until that is known, these key numbers cannot be trusted for the listed days, or for any period that includes them:
- daily orders
- revenue
- conversion rate
- checkout funnel figures

Purchase is below threshold on 6 of the 7 days, and add_payment_info and add_shipping_info are below threshold on all 7. If data was not received, totals for these periods would be understated.

The holidays named next to five of the days are possible, unconfirmed explanations. Martin Luther King Jr. Day is observed in the US only. The check results do not say which countries the data covers, so it is unknown how much that holiday could explain the drop on Jan 18, 2021. No holiday is named for Dec 30, 2020 or Jan 4, 2021.

## Suggested next steps
- Get the actual counts and typical counts for each flagged event and day, so the size of each drop is known.
- Split the flagged days by country and platform. This would show whether the drops are spread evenly or concentrated in one place. It is especially important for Jan 18, 2021, where the named holiday is US only.
- Check whether there were any known tracking, release or data pipeline incidents on the 7 listed days, particularly Dec 30, 2020 and Jan 4, 2021, which have no holiday named.
- Compare these days with the same dates in other years, if that data exists, to see whether similar drops occurred.
- Confirm with the people who own the purchase and checkout events whether the drops match other sources of order or revenue data for the same days.

## Acceptance criteria
Each of the 7 listed days is marked with one of these outcomes:
- **Confirmed as real lower activity,** with the evidence used.
- **Confirmed as data not received,** with the gap either recovered or documented so that reports covering these days can flag it.

Orders, revenue, conversion and checkout funnel reporting that covers Dec 24, 2020 – Jan 18, 2021 includes a note on any day whose status is still unconfirmed.