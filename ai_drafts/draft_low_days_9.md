# view_item_list received 25.0% of its typical volume on Nov 18, 2020

**Event:** view_item_list
**Found by:** · **Date found:** · **Severity:** Low

## Description
On Nov 18, 2020, the `view_item_list` event had far fewer events than usual. The check results show 1 event that day, while the typical count is 4. That is 25.0% of typical.

The low-volume check flags a day when an event's count is below 0.5 of its typical count. The typical count is the median for the same weekday. This is the only day flagged for this event.

Nov 18, 2020 does not have a holiday name next to it in the check results, so it is not on the tracking plan's holiday calendar.

The check results also list many days with no `view_item_list` data at all. They include Nov 16 to Nov 17, 2020 and Nov 19, 2020, which are next to the flagged day. Those days are covered in a separate missing-day ticket and are not part of this one. Being close together in time does not show that the low day and the missing days share a cause.

## Evidence (Nov 18, 2020)
- Nov 18, 2020: 1 `view_item_list` event, typical 4, 25.0% of typical.
- Flagging threshold: below 0.5 of typical, where typical is the median for that weekday.
- Number of flagged days for this event: 1.
- No holiday is named next to this date in the check results.

## Impact
According to the tracking plan, `view_item_list` is used for:
- product list views
- the list-to-product funnel step

For Nov 18, 2020, product list view counts and the list-to-product funnel step may not reflect actual activity. The check results only show what was received. They do not show whether the low count reflects real user behavior or incomplete data collection.

The tracking plan rates this event High, but that rating applies only if the event stops arriving entirely. Events did arrive on Nov 18, 2020, so High is the most this ticket could be rated, not its automatic rating.

Severity is Low for two reasons:
- The problem affects a single day.
- The check results give a typical count of only 4 events for that day.

Because of that, the effect on decisions made from product list views or the list-to-product funnel is expected to be small. Analyses that look closely at that day should treat its `view_item_list` figures with caution.

## Suggested next steps
- Find out whether the 1 event received on Nov 18, 2020 reflects real activity or whether events were sent but not received or stored.
- Check whether anything changed in how `view_item_list` was collected around Nov 18, 2020. The check results do not provide this information.
- Coordinate with whoever owns the separate missing-day ticket for this event. Investigation of the nearby missing days may help explain Nov 18, 2020, but treat any link as unconfirmed until it is verified.

## Acceptance criteria
- The reason for the low count on Nov 18, 2020 is confirmed and documented. It should be stated as either real user behavior or a data collection problem.
- If the cause is a data collection problem, either the missing events are recovered so the day is no longer flagged, or the day is clearly marked as incomplete for any analysis of product list views or the list-to-product funnel step.