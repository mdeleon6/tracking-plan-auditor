# `purchase` events below 0.5 of typical volume on 7 days between Nov 5, 2020 and Jan 8, 2021

**Event:** purchase
**Found by:** · **Date found:** · **Severity:** High

## Description
On 7 days, the number of `purchase` events received was below 0.5 of the typical count for that day. The automated low-volume check flagged these days. The typical count is the median count for the same weekday.

Four of the 7 days fall in a row, from Jan 5 to Jan 8, 2021. The other three are single days: Nov 5, 2020, Dec 29, 2020 and Jan 2, 2021. None of the 7 dates appears on the holiday calendar in the tracking plan.

The check results show only how many events were received. They do not show whether fewer purchases actually happened on these days or whether purchases happened but were not recorded. The cause is not known.

## Evidence (Nov 5, 2020 – Jan 8, 2021)
- Check: low volume. A day is flagged when an event's count is below 0.5 of its typical count, which is the median for that weekday.
- Flagged days for `purchase`:
  - Nov 5, 2020: 26 events, typical 54, 48.1% of typical
  - Dec 29, 2020: 24 events, typical 60, 40.0% of typical
  - Jan 2, 2021: 14 events, typical 31, 45.2% of typical
  - Jan 5, 2021: 29 events, typical 60, 48.3% of typical
  - Jan 6, 2021: 31 events, typical 67, 46.3% of typical
  - Jan 7, 2021: 26 events, typical 54, 48.1% of typical
  - Jan 8, 2021: 34 events, typical 79, 43.0% of typical
- `purchase` was also below the threshold on 6 more days. On those days many events dropped together, so they are covered in a separate multi-event ticket, not this one:
  - Dec 24, 2020 (Christmas Eve, widely observed)
  - Dec 25, 2020 (Christmas Day, widely observed)
  - Dec 31, 2020 (New Year's Eve, widely observed)
  - Jan 1, 2021 (New Year's Day, widely observed)
  - Jan 4, 2021
  - Jan 18, 2021 (Martin Luther King Jr. Day, US only)
- Jan 4, 2021 is in the multi-event ticket and comes just before the Jan 5–8 run in this ticket. The check results do not show whether the two are related.
- The check results do not include:
  - the full date range the check covered
  - counts broken down by country or platform
  - revenue amounts for the flagged days
  - whether other events were also low on these 7 days

## Impact
According to the tracking plan, `purchase` is used for orders, revenue, conversion rate, and revenue and conversion by country and platform. On the 7 flagged days, orders, revenue and conversion rate built from `purchase` events cannot be trusted until it is known whether the low counts reflect real activity. Any weekly, monthly or period total that includes these days may be affected as well.

The severity is High because orders, revenue and conversion rate are key business numbers and they depend directly on this event. The tracking plan also rates `purchase` as High if it stopped arriving entirely. The problem here is a partial drop on 7 days rather than a full stop. Even so, the affected numbers are the key ones, so High still applies.

## Suggested next steps
- Compare the `purchase` counts for the 7 flagged days against an independent record of orders, if one exists, to find out whether purchases are missing from tracking or whether fewer purchases happened.
- Break down the flagged days by country and platform to see whether the drop is limited to one segment.
- Check whether any tracking, site or app changes were released around Nov 5, Dec 29 and Jan 2–8. Treat any match as a lead to confirm, not as the cause.
- Review the Jan 5–8 run alongside the multi-event ticket for Jan 4, 2021. Do not assume a shared cause until one is confirmed.
- Agree how reports of orders, revenue and conversion should handle these days until the cause is known, for example by flagging them in dashboards.

## Acceptance criteria
- Each of the 7 flagged days is either:
  - confirmed as real lower purchase activity, using a source outside this tracking, with the finding documented, or
  - corrected, with the low-volume check re-run and the day no longer flagged.
- If a tracking fault is found, the fault is fixed and `purchase` volume stays at or above 0.5 of typical on later days, outside days covered by multi-event tickets.
- A documented decision exists on how orders, revenue and conversion reporting treats any of the 7 days that cannot be corrected.