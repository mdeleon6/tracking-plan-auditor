# select_item events at 16.6% of typical volume on Nov 23, 2020

**Event:** select_item
**Found by:** · **Date found:** · **Severity:** Medium

## Description
On Nov 23, 2020, 59 `select_item` events were received, which is 16.6% of the typical 356 for that day. An automated low-volume check flags any day where an event's count is below 0.5 of its typical count. The typical count is the median for that weekday. Nov 23, 2020 is the only flagged day covered by this ticket.

Nov 23, 2020 is the first day after a period with no `select_item` data at all (Nov 1, 2020 to Nov 22, 2020). That gap is covered in a separate missing-day ticket. The check results do not say whether the two problems are related.

## Evidence (Nov 23, 2020)
- Nov 23, 2020: 59 `select_item` events received, typical 356, 16.6% of typical.
- Check threshold: a day is flagged when the count is below 0.5 of the median for that weekday.
- Nov 23, 2020 does not appear on the tracking plan's holiday calendar.
- Not part of this ticket:
  - Nov 1, 2020 to Nov 22, 2020 had no `select_item` data at all. This is covered in a separate missing-day ticket.
  - Dec 31, 2020 (New Year's Eve, widely observed) was also below threshold. On that day many events dropped together. It is covered in a separate multi-event ticket.
- Missing from the check results:
  - Counts for the days after Nov 23, 2020.
  - Hourly counts within Nov 23, 2020.
  - How many weeks of data went into the typical value of 356.

## Impact
According to the tracking plan, `select_item` is used for product list click-through rate and item selection reporting. Both will understate selections on Nov 23, 2020. Any weekly or monthly figure that includes that day will also be affected.

The check results only show what was received. They do not show whether the low count reflects real user behavior or events that were not captured.

This is Medium. The tracking plan rates this event Medium if it stopped arriving entirely, and a partial drop cannot be rated higher than that. Medium fits because one area of analysis is affected: product list click-through and item selection. The tracking plan does not list revenue, orders or conversion rates among this event's uses.

## Suggested next steps
- Find out whether `select_item` tracking started or restarted partway through Nov 23, 2020. One possible, unconfirmed explanation is that the day holds only part of a day's events because it directly follows the Nov 1–22 gap. Hourly counts for Nov 23 would help confirm or rule this out.
- Check whether related events, such as product list views, were also low on Nov 23, 2020. A low count of selections alone would distort click-through rate.
- Review counts for Nov 24, 2020 onward to confirm whether volume returned to typical levels.
- Find out how many weeks of data went into the typical value of 356. No data was received for the weeks before Nov 23.
- If the data is re-pulled for Nov 23, 2020, rerun the low-volume check to see whether the day is still flagged.

## Acceptance criteria
- The reason for the low count on Nov 23, 2020 is confirmed and recorded.
- One of the following is true:
  - The day's data is corrected so that it is no longer flagged by the low-volume check.
  - The low count is documented as real behavior.
- Until the issue is resolved, product list click-through rate and item selection reports that include Nov 23, 2020 either exclude that day or carry a note about the low count.