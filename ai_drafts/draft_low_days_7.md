# select_item received at 16.6% of typical volume on Nov 23, 2020

**Event:** select_item
**Found by:** · **Date found:** · **Severity:** Medium

## Description
The low-volume check flagged the `select_item` event on one day, Nov 23, 2020. That day had 59 events against a typical count of 356, or 16.6% of typical. The check flags a day when an event's count is below 0.5 of its typical count. The typical count is the median for that weekday.

The check results also show that `select_item` has no data at all from Nov 1, 2020 to Nov 22, 2020. The flagged day is the first day after that period ends.

`select_item` was also below the threshold on Dec 31, 2020, when many events dropped together. That day is covered in a separate multi-event ticket and is not part of this one.

## Evidence
- Nov 23, 2020: 59 `select_item` events, typical 356, 16.6% of typical.
- Number of flagged days for this ticket: 1.
- No `select_item` data at all from Nov 1, 2020 to Nov 22, 2020.
- Also below threshold on Dec 31, 2020, which is covered in a separate multi-event ticket.
- The check results do not include a daily breakdown for any other days, a time-of-day breakdown for Nov 23, or a total `select_item` count for the period.

## Impact
Any count of item selections that includes Nov 23, 2020 will be lower than a typical day. This also applies to any rate or funnel step built on `select_item`. The check results only show what was received. They do not show whether fewer selections actually happened that day or whether some selections were not recorded.

The days with no data from Nov 1 to Nov 22, 2020 also affect any analysis of `select_item` across the full period. The check results do not show whether selections happened on those days.

One possible explanation is that tracking for `select_item` began partway through Nov 23, 2020, because the low day directly follows the period with no data. This is unconfirmed. The two observations appearing next to each other does not prove they share a cause.

**Severity reasoning:** The tracking plan rates this event Medium if it stopped arriving entirely. That rating is the highest severity allowed for this low-volume problem. The problem affects one type of analysis: item-selection counts and anything built on them. Those counts are unreliable for Nov 23, and they are absent for Nov 1 to Nov 22. The check results do not show any effect on revenue, orders or other key business totals, so this is not rated High. They also do not confirm that those totals are correct. Because missing item-selection data across this period could change conclusions drawn from item-level analysis, this ticket uses Medium rather than Low.

## Suggested next steps
- Confirm when `select_item` tracking was first expected to send data. Was data expected before Nov 23, 2020, or was Nov 23 the planned start?
- Check how `select_item` events on Nov 23, 2020 are spread across the day. A count concentrated late in the day would support a partial-day start, while an even spread would point elsewhere.
- Confirm whether any `select_item` data from Nov 1 to Nov 22, 2020 exists in the source but was not received.
- Check whether the days immediately after Nov 23, 2020 return to typical volume. The check results only flag Nov 23 for this ticket, but they do not list the counts for those days.

## Acceptance criteria
- The reason for the low count on Nov 23, 2020 is confirmed and documented.
- The expected start date for `select_item` tracking is confirmed. Any analysis using `select_item` states which days it covers and how Nov 1 to Nov 23, 2020 is handled.
- If any missing `select_item` data for Nov 1 to Nov 23, 2020 can be recovered, a re-run of the low-volume check no longer flags Nov 23, 2020.