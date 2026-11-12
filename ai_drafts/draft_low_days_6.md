# Purchase events fell below half of their typical daily count on 7 days between Nov 5, 2020 and Jan 8, 2021

**Event:** purchase
**Found by:** · **Date found:** · **Severity:** High

## Description
An automated low-volume check flagged the `purchase` event on 7 days between Nov 5, 2020 and Jan 8, 2021. On each of these days, the number of `purchase` events received was less than 0.5 of the typical count. "Typical" means the median count for that day of the week.

The check results only show how many events were received. They do not show whether fewer purchases actually happened on these days or whether purchases happened but were not recorded. Both are still possible.

None of the 7 days has a holiday name in the check results. That means none of them is on the tracking plan's holiday calendar.

The flagged days include Jan 5, 6, 7 and 8, 2021. The check results do not say whether these days share a cause with each other or with any other flagged day.

## Evidence (Nov 5, 2020 – Jan 8, 2021)
- Nov 5, 2020: 26 events, typical 54, 48.1% of typical
- Dec 29, 2020: 24 events, typical 60, 40.0% of typical
- Jan 2, 2021: 14 events, typical 31, 45.2% of typical
- Jan 5, 2021: 29 events, typical 60, 48.3% of typical
- Jan 6, 2021: 31 events, typical 67, 46.3% of typical
- Jan 7, 2021: 26 events, typical 54, 48.1% of typical
- Jan 8, 2021: 34 events, typical 79, 43.0% of typical

The check results also show `purchase` below the threshold on 6 more days. On those days, many events dropped at the same time. Those days are covered in a separate multi-event ticket and are not part of this one:
- Dec 24, 2020 (Christmas Eve, widely observed)
- Dec 25, 2020 (Christmas Day, widely observed)
- Dec 31, 2020 (New Year's Eve, widely observed)
- Jan 1, 2021 (New Year's Day, widely observed)
- Jan 4, 2021
- Jan 18, 2021 (Martin Luther King Jr. Day, US only)

For those days, the holidays are a possible, unconfirmed explanation only.

The following are missing from the check results:
- Revenue amounts for the flagged days
- A breakdown by country or platform
- Event counts for the whole period
- Any query or data extract

## Impact
The tracking plan uses `purchase` for:
- orders
- revenue
- conversion rate
- revenue and conversion by country and platform

The tracking plan rates this event as High if it stopped arriving entirely.

If the low counts come from purchases that happened but were not recorded, then orders, revenue and conversion rate are understated on these 7 days. Any totals or trends that include these days would also be affected. If the low counts reflect real behavior, those numbers are correct.

Until this is resolved, we cannot tell which is true. Orders, revenue and conversion rate for these days cannot be trusted. That is why this ticket is High rather than Medium.

## Suggested next steps
- Compare the 7 flagged days against an independent record of orders, if one exists. This will show whether fewer purchases happened or whether purchases were not recorded.
- Break down the flagged days by country and platform. This will show whether the drop is spread evenly or limited to one country or platform.
- Find out whether any site, app or tracking changes were released on or just before Nov 5, 2020, Dec 29, 2020, Jan 2, 2021 or Jan 5, 2021.
- Check whether the drop on Jan 5–8, 2021 has one cause or several separate causes. Do not assume they are linked to each other or to the days in the multi-event ticket.

## Acceptance criteria
- Each of the 7 flagged days is confirmed as either real behavior or missing tracking. The evidence for each decision is recorded in this ticket.
- If any day is confirmed as missing tracking, one of these happens:
  - the missing purchases are recovered, or
  - the day is clearly marked as incomplete in any report on orders, revenue or conversion rate.
- Future runs of the low-volume check do not flag `purchase` for any cause found in this investigation.