# `select_item` received 59 events on Nov 23 2020, 16.6% of its typical count

**Event:** select_item
**Found by:** · **Date found:** · **Severity:** Medium

## Description
The low-volume check flagged one day for `select_item`. On Nov 23, 2020, 59 events were received. The typical count for that day is 356, so the day reached 16.6% of typical. The check flags a day when an event's count is below 0.5 of its typical count. The typical count is the median for that weekday.

No `select_item` data at all was received from Nov 1, 2020 to Nov 22, 2020. That makes Nov 23, 2020 the first day in the check results with any `select_item` events.

## Evidence
- Nov 1, 2020 – Nov 22, 2020: no `select_item` data received.
- Nov 23, 2020: 59 `select_item` events, typical 356, 16.6% of typical.
- Number of flagged days in this ticket: 1.
- Nov 23, 2020 has no holiday name next to it, so it is not on the tracking plan's holiday calendar.
- `select_item` was also below the threshold on Dec 31, 2020 (New Year's Eve, widely observed as a day off), when many events dropped together. That day is covered in a separate multi-event ticket and is not part of this one.
- The check results do not say which dates were used to calculate the typical count of 356.

## Impact
Any analysis built on `select_item` that includes Nov 23, 2020 will understate item selections for that day. Examples include how often items in lists are selected, or which items are selected most. Across November 2020, `select_item` analysis is limited further, because no data was received from Nov 1 to Nov 22. Trends that start in November will appear to begin on Nov 23 at a low level.

Severity is Medium because this affects one type of analysis, based on item selections. The check results do not show an effect on revenue, orders or conversion totals. The tracking plan rates this event Medium if it stopped arriving entirely, so Medium is also the highest severity allowed for this low-volume problem.

The 59 events received on Nov 23 do not show whether the day's data is complete. The gap from Nov 1 to Nov 22 also does not show whether item selections happened during that period.

## Suggested next steps
- Confirm whether `select_item` tracking started on Nov 23, 2020. If it did, Nov 23 may be a partial first day of tracking. This is a possible explanation only and has not been confirmed.
- Find out whether `select_item` should have been sent from Nov 1 to Nov 22, 2020, and whether any data from that period can be recovered.
- Confirm which dates were used for the typical count of 356. With no data before Nov 23, it is unclear what that median is based on.
- If Nov 23 is confirmed as a partial or incomplete day, decide whether to exclude it from `select_item` analysis.

## Acceptance criteria
- The cause of the low count on Nov 23, 2020 is confirmed and documented. If the low count was a tracking problem, it is fixed.
- The status of Nov 1 to Nov 22, 2020 is documented: either tracking had not started yet, or data was lost, and if lost, whether it was recovered.
- Anyone using `select_item` data is told which dates in November 2020 can be relied on.