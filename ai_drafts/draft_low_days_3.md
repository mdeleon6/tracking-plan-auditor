# `add_shipping_info` below half of its typical count on 12 days between Dec 26, 2020 and Jan 15, 2021

**Event:** add_shipping_info
**Found by:** · **Date found:** · **Severity:** High

## Description
The automated low-volume check flagged `add_shipping_info` on 12 days between Dec 26, 2020 and Jan 15, 2021. On each of these days, fewer events were received than half of the event's typical count. The check defines "typical" as the median count for that weekday.

On these 12 days, the counts received ranged from 32.4% to 49.4% of typical. The check results only show how many events were received. They do not show whether fewer shipping steps actually happened or whether events were sent but not received. The cause has not been confirmed.

These 12 days are listed separately from the days when many events dropped together. The event was also below threshold on those days, but they are covered in a separate multi-event ticket and are not part of this ticket.

## Evidence (Dec 26, 2020 – Jan 15, 2021)
- Check: low volume. A day is flagged when the count is below 0.5 of the typical count for that weekday.
- Number of flagged days in this ticket: 12.
- Dec 26, 2020: 48 events, typical 148, 32.4% of typical
- Dec 28, 2020: 101 events, typical 211, 47.9% of typical
- Dec 29, 2020: 80 events, typical 233, 34.3% of typical
- Jan 2, 2021: 48 events, typical 148, 32.4% of typical
- Jan 3, 2021: 51 events, typical 129.5, 39.4% of typical
- Jan 5, 2021: 88 events, typical 233, 37.8% of typical
- Jan 6, 2021: 116 events, typical 248, 46.8% of typical
- Jan 8, 2021: 105 events, typical 269, 39.0% of typical
- Jan 9, 2021: 58 events, typical 148, 39.2% of typical
- Jan 10, 2021: 58 events, typical 129.5, 44.8% of typical
- Jan 11, 2021: 94 events, typical 211, 44.5% of typical
- Jan 15, 2021: 133 events, typical 269, 49.4% of typical
- None of these 12 dates has a holiday name in the tracking plan's holiday calendar.
- Not in this ticket: the event was also below threshold on 7 more days when many events dropped together. These are covered in a separate multi-event ticket: Dec 24, 2020, Dec 25, 2020, Dec 30, 2020, Dec 31, 2020, Jan 1, 2021, Jan 4, 2021 and Jan 18, 2021. The tracking plan's holiday calendar names Christmas Eve (Dec 24, widely observed), Christmas Day (Dec 25, widely observed), New Year's Eve (Dec 31, widely observed), New Year's Day (Jan 1, widely observed) and Martin Luther King Jr. Day (Jan 18, observed in the US only). Dec 30, 2020 and Jan 4, 2021 have no holiday name.
- Missing from the check results:
  - Counts for the days in this range that were not flagged.
  - Total event counts for the period.
  - Counts for the other checkout events on the 12 flagged days.

## Impact
According to the tracking plan, `add_shipping_info` is used in the checkout funnel and in checkout conversion rate by country and platform. Checkout conversion rate is a key business number.

On the 12 flagged days, the event arrived at less than half its usual volume. Until it is confirmed whether this reflects real customer behavior or a tracking problem, the checkout funnel and checkout conversion rate for these days cannot be trusted, either overall or split by country and platform. This is why the severity is High.

The tracking plan also rates this event High if it stopped arriving entirely. The event did not stop here; it arrived at reduced volume. The High rating in this ticket is based on the conversion rate depending on the event, not on the plan's rating.

## Suggested next steps
- Check whether the funnel steps before and after `add_shipping_info` were also low on these 12 days. If the other steps look normal while this one is low, that would point toward a tracking problem. If they are low too, that would point toward real behavior. Either way, it would need to be confirmed.
- Check whether any change to checkout or to the tracking of this event was released between late December 2020 and mid-January 2021.
- Pull the daily counts for the days in this range that were not flagged, to see whether the event was also lower than usual on those days without falling below the threshold.
- Split the flagged days by country and platform to see whether the drop is limited to particular segments.
- Coordinate with the owner of the separate multi-event ticket, so the two tickets do not reach conflicting conclusions about the same event.

## Acceptance criteria
- Each of the 12 flagged days has a documented explanation stating whether the low count reflects real activity or a tracking problem.
- If it is a tracking problem, the cause is fixed. The affected days are then either backfilled or clearly marked so they can be excluded from the checkout funnel and checkout conversion rate reports.
- From the fix onward, `add_shipping_info` stays at or above 0.5 of its typical count on every day, or any flagged day has a documented explanation.