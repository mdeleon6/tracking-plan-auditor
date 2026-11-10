# view_item counts fell below 0.5 of typical on Dec 29, 2020 and Jan 2, 2021

**Event:** view_item
**Found by:** · **Date found:** · **Severity:** Medium

## Description
The `view_item` event was received in lower volume than usual on two days. On each day the count fell below the low-volume threshold, which is 0.5 of the event's typical count. Here, "typical" means the median count for the same weekday.

The check results do not show whether this reflects fewer product views or events that were not received. They also do not give a cause.

The event was also below the threshold on 7 other days, when many events dropped at the same time. Those days are covered in a separate multi-event ticket and are not part of this one.

## Evidence
- Dec 29, 2020: 2308 events received, against a typical count of 5222 (44.2% of typical).
- Jan 2, 2021: 1390 events received, against a typical count of 3113 (44.7% of typical).
- Other below-threshold days, covered in the separate multi-event ticket: Dec 24, 2020, Dec 25, 2020, Dec 30, 2020, Dec 31, 2020, Jan 1, 2021, Jan 4, 2021 and Jan 18, 2021.
- The check results do not include hourly counts, platform breakdowns, counts for other events on the two flagged days, or any query or file references.

## Impact
Any count of `view_item` events that includes Dec 29, 2020 or Jan 2, 2021 may not reflect real product viewing. This also applies to metrics built on that count, such as view-to-cart or view-to-purchase rates. If events went unrecorded, view-based conversion rates for those days would look higher than they really were. If the drop reflects real behavior, the numbers are accurate. The check results cannot tell these two cases apart.

The tracking plan rates this event Medium if it stopped arriving entirely. For a low-volume problem like this one, that rating is the highest severity allowed. Conversion rates are key business numbers, which would normally point to High, so the severity is capped at Medium. The event did not stop arriving on either day.

Both days fall in a period that includes holidays. Lower real activity is a possible explanation, but it has not been confirmed. The two days sit close to the multi-event drop days, but the check results do not show that they share a cause.

## Suggested next steps
- Find out whether traffic or sessions were also lower on Dec 29, 2020 and Jan 2, 2021. This would help show whether fewer people were browsing or whether `view_item` alone was affected.
- Review counts for related events on these two days, such as page views, `add_to_cart` and `purchase`. Check whether they dropped by a similar share.
- Look at hourly `view_item` counts for both days. Check whether volume stopped or fell at a specific time, or was low across the whole day.
- Check whether any site, app or tracking changes were released on or just before either date.
- Compare findings with the separate multi-event ticket, without assuming the same cause applies.

## Acceptance criteria
- The cause of the low `view_item` counts on Dec 29, 2020 and Jan 2, 2021 is confirmed and documented, either as real behavior or as a tracking issue.
- If it is a tracking issue, the issue is fixed. Any recoverable events for these days are restored, and the check is re-run to confirm whether the days are still flagged.
- Until the cause is confirmed, analyses that use `view_item` counts or view-based conversion rates note that these two days may be unreliable.