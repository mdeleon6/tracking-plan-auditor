# view_item events below half of typical volume on Dec 29, 2020 and Jan 2, 2021

**Event:** view_item
**Found by:** · **Date found:** · **Severity:** Medium

## Description
The low-volume check flagged 2 days on which the `view_item` event arrived at under half of its usual count. The check compares each day with the median count for that weekday and flags any day below 0.5 of that median. On Dec 29, 2020 and Jan 2, 2021, `view_item` was at 44.2% and 44.7% of typical.

These 2 days are handled in this ticket on their own because they were not among the days when many events dropped together. Neither date is on the holiday calendar in the tracking plan.

The check results only show how many events were received. They do not show whether fewer product views actually happened on these days or whether some views were not recorded. The cause is not known.

## Evidence (Dec 29, 2020 – Jan 2, 2021)
- Dec 29, 2020: 2308 `view_item` events against a typical 5222 (44.2% of typical).
- Jan 2, 2021: 1390 `view_item` events against a typical 3113 (44.7% of typical).
- Threshold: a day is flagged when the count is below 0.5 of the median for that weekday.
- `view_item` was also below threshold on 7 other days, which are covered in a separate multi-event ticket:
  - Dec 24, 2020 (Christmas Eve, widely observed)
  - Dec 25, 2020 (Christmas Day, widely observed)
  - Dec 30, 2020
  - Dec 31, 2020 (New Year's Eve, widely observed)
  - Jan 1, 2021 (New Year's Day, widely observed)
  - Jan 4, 2021
  - Jan 18, 2021 (Martin Luther King Jr. Day, US only)
- The check results do not include:
  - a query
  - counts for other events on Dec 29, 2020 or Jan 2, 2021
  - a breakdown of the drop by country or platform

## Impact
According to the tracking plan, `view_item` feeds these reports:
- product views
- view-to-cart rate
- product performance by country and platform

Product view totals for Dec 29, 2020 and Jan 2, 2021 may be undercounted if the low counts do not reflect real activity. The same applies to any weekly or period total that includes these days. View-to-cart rate for these days would also be overstated if views were undercounted but add-to-cart events were not. The check results do not show whether add-to-cart events dropped on these days.

Both flagged dates fall between Dec 24, 2020 and Jan 4, 2021, the same span as most of the multi-event days. One possible, unconfirmed explanation is that these days belong to the same pattern. Falling in the same span does not prove a shared cause. These two dates are not on the holiday calendar and were not flagged as multi-event days.

**Why Medium:** The tracking plan rates the complete loss of `view_item` as Medium. The affected numbers are product views and a funnel rate. Revenue, orders and units sold are not among the uses the tracking plan lists for this event. View-to-cart rate is a funnel measure, but the drop affects 2 days, so it could only distort results for those days or periods that include them. This is not rated Low because product performance reporting by country and platform could be misread for these dates.

## Suggested next steps
- Pull counts for related events, especially add-to-cart, on Dec 29, 2020 and Jan 2, 2021. This shows whether the drop is limited to `view_item` and whether view-to-cart rate is affected.
- Break down `view_item` on both days by country and platform. This shows whether the drop is concentrated in one segment, such as a single platform.
- Check for any site, app or tracking changes deployed shortly before or on these two dates.
- Compare findings with the separate multi-event ticket. Record whether these 2 days turn out to share a cause with the 7 multi-event days, or not.

## Acceptance criteria
- For each of Dec 29, 2020 and Jan 2, 2021, there is a documented finding that the low count reflects either real activity or a tracking problem.
- If a tracking problem is confirmed, the affected data is either restored or clearly annotated in product views, view-to-cart rate and product performance reporting for these dates.
- If the cause is a tracking problem that can recur, it is fixed, and later days no longer fall below 0.5 of typical for the same reason.