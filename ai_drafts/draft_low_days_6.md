# `purchase` events below half their typical daily volume on 7 days between Nov 5, 2020 and Jan 8, 2021

**Event:** purchase
**Found by:** · **Date found:** · **Severity:** High

## Description
The `purchase` event was received at less than half its usual daily volume on 7 days between Nov 5, 2020 and Jan 8, 2021. Jan 5, 6, 7 and 8, 2021 were flagged in a row. The other flagged days are Nov 5, 2020, Dec 29, 2020 and Jan 2, 2021.

The check flags a day when an event's count falls below 0.5 of its typical count. The typical count is the median count for that weekday.

The check results only show how many events were received. They do not show whether fewer purchases actually happened on these days or whether purchases happened but were not recorded. The cause is not known.

None of the 7 flagged dates has a holiday name in the check results. That means none of them is on the tracking plan's holiday calendar.

## Evidence
- Nov 5, 2020: 26 events, typical 54, 48.1% of typical
- Dec 29, 2020: 24 events, typical 60, 40.0% of typical
- Jan 2, 2021: 14 events, typical 31, 45.2% of typical
- Jan 5, 2021: 29 events, typical 60, 48.3% of typical
- Jan 6, 2021: 31 events, typical 67, 46.3% of typical
- Jan 7, 2021: 26 events, typical 54, 48.1% of typical
- Jan 8, 2021: 34 events, typical 79, 43.0% of typical

**Related days handled in a separate ticket:** `purchase` was also below the threshold on 6 more days when many events dropped together. A separate multi-event ticket covers these days:
- Dec 24, 2020 (Christmas Eve: widely observed)
- Dec 25, 2020 (Christmas Day: widely observed)
- Dec 31, 2020 (New Year's Eve: widely observed)
- Jan 1, 2021 (New Year's Day: widely observed)
- Jan 4, 2021
- Jan 18, 2021 (Martin Luther King Jr. Day: US only)

Some of these days fall close to the flagged days in this ticket. However, the check results do not show whether the two sets of days share a cause.

## Impact
According to the tracking plan, `purchase` is used for:
- orders
- revenue
- conversion rate
- revenue and conversion by country and platform

The tracking plan rates this event High if it stopped arriving entirely. That did not happen here, because events were received on every flagged day. For this low-volume problem, High is therefore the highest severity allowed, and severity is set by what the problem breaks.

Severity is **High** because it is not known whether these drops reflect real behavior or missing data. Until that is confirmed, the following key business numbers cannot be trusted for these 7 days, or for any period that includes them:
- order counts
- revenue
- conversion rate

Breakdowns by country and platform for these days are also affected.

The check results do not include revenue values or overall totals for the period, so the size of any effect on revenue is missing.

## Suggested next steps
- For each flagged day, compare the received `purchase` count with an order record kept outside of tracking. This confirms whether purchases were actually lower or were not recorded.
- Look at Jan 5–8, 2021 as a group, since they were flagged on consecutive days. Check whether any tracking, site or app changes were made around that time. Any link to those changes is possible but unconfirmed.
- Check whether the drop on each flagged day affected some countries or platforms more than others. This can show whether the problem is limited to one area.
- Check the outcome of the separate multi-event ticket. Review whether anything found there also applies to these 7 days, without assuming a shared cause.

## Acceptance criteria
- Each of the 7 flagged days is documented as either:
  - a confirmed real drop in purchases, or
  - confirmed missing data, with the cause noted.
- If data is missing, the missing purchases are recovered. If they cannot be recovered, the affected days are clearly marked in any reporting on orders, revenue and conversion.
- If a tracking fault is found and fixed, later days are not flagged by the low-volume check for `purchase` unless the drop is confirmed as real behavior.