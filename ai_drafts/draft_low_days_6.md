# Purchase events fell below half of their typical count on 7 days between Nov 5, 2020 and Jan 8, 2021

**Event:** purchase
**Found by:** · **Date found:** · **Severity:** High

## Description
An automated low-volume check flagged 7 days on which fewer `purchase` events were received than usual. The check flags a day when an event's count is below 0.5 of its typical count. The typical count is the median for that weekday. On every flagged day, the number of purchase events received was between 40.0% and 48.3% of typical.

Four of the flagged days fall on consecutive dates, Jan 5 to Jan 8, 2021. The other three are single dates spread across the period: Nov 5, 2020, Dec 29, 2020 and Jan 2, 2021. None of these 7 dates has a holiday name in the tracking plan's holiday calendar.

The check results only show what was received. They do not show whether fewer purchases actually happened on these days or whether purchases happened but were not recorded.

## Evidence
- Nov 5, 2020: 26 events, typical 54, 48.1% of typical
- Dec 29, 2020: 24 events, typical 60, 40.0% of typical
- Jan 2, 2021: 14 events, typical 31, 45.2% of typical
- Jan 5, 2021: 29 events, typical 60, 48.3% of typical
- Jan 6, 2021: 31 events, typical 67, 46.3% of typical
- Jan 7, 2021: 26 events, typical 54, 48.1% of typical
- Jan 8, 2021: 34 events, typical 79, 43.0% of typical
- The check results do not state the full date range that was checked, and they do not give purchase totals for that range.
- The check results do not include a query or other reference for reproducing these numbers.

**Related days covered elsewhere:** `purchase` was also below the threshold on 6 more days when many events dropped together. A separate multi-event ticket covers those days, so they are not part of this ticket:
- Dec 24, 2020 (Christmas Eve: widely observed)
- Dec 25, 2020 (Christmas Day: widely observed)
- Dec 31, 2020 (New Year's Eve: widely observed)
- Jan 1, 2021 (New Year's Day: widely observed)
- Jan 4, 2021
- Jan 18, 2021 (Martin Luther King Jr. Day: US only)

Taken together with this ticket, `purchase` was below the threshold on every date from Jan 4 to Jan 8, 2021. Jan 2, 2021 is also close to the multi-event days of Dec 31 and Jan 1. Being close in time does not show that these drops share a cause, and none has been confirmed.

## Impact
`purchase` is the event that counts orders. On the 7 flagged days, the number of orders received was below half of typical. Until someone confirms whether this reflects real customer behavior or lost tracking, purchase counts for these days cannot be trusted. Any revenue, order or conversion figures built from these events also cannot be trusted for these days, and neither can any weekly, monthly or period totals that include them.

The tracking plan rates this event High if it stops arriving entirely. The event did not stop arriving, because purchase events were received on every flagged day. That rating therefore sets the highest severity allowed for this ticket. Within that limit, the severity is High because order totals, a key business number, may be affected. It is not Medium, because Medium requires totals to still be correct, and that cannot be shown here.

## Suggested next steps
- For each of the 7 days, compare the purchase counts with an independent record of orders, if one exists, to find out whether purchases really were lower or were not tracked.
- Find out whether any site, app or tracking changes were released on or just before Nov 5, Dec 29, Jan 2 or Jan 5–8. Treat any match as a possible lead, not a confirmed cause.
- Check whether the drop on these days appears in only some parts of the traffic, such as certain platforms or regions, or across all of it. This check depends on what breakdowns are available.
- Coordinate with the owner of the multi-event ticket on Jan 4, 2021, since `purchase` was also low from Jan 5 to Jan 8. Do not assume the two tickets share a cause unless that is confirmed.

## Acceptance criteria
- Each of the 7 flagged days has a documented finding: either the low count matches real order activity, or it is confirmed as a tracking loss.
- For any day confirmed as a tracking loss, the missing purchases are recovered in the data, or the day is clearly marked as incomplete so that reports and analyses can exclude or annotate it.
- If a tracking cause is found, it is fixed, and `purchase` counts on later days are no longer flagged by the low-volume check for that same cause.