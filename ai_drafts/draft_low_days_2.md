# add_payment_info fell below half its typical daily count on 10 days between Dec 26, 2020 and Jan 13, 2021

**Event:** add_payment_info
**Found by:** · **Date found:** · **Severity:** Medium

## Description
An automated low volume check flagged the `add_payment_info` event on 10 days between Dec 26, 2020 and Jan 13, 2021. The check flags a day when an event's count falls below 0.5 of its typical count. "Typical" means the median count for that day of the week.

The event still arrived on every flagged day, but in much smaller numbers than usual. The lowest day was Jan 2, 2021, at 31.5% of typical. The check results only show how many events were received. They cannot tell us whether fewer customers added payment info on these days or whether some events were lost in tracking.

`add_payment_info` was also below the threshold on 7 more days when many events dropped at the same time. Those days are covered in a separate multi-event ticket and are not part of this ticket.

## Evidence (Dec 26, 2020 – Jan 13, 2021)
- Check: low volume. A day is flagged when the count is below 0.5 of the median count for that weekday.
- Number of flagged days: 10.
- Dec 26, 2020: 40 events, typical 89, 44.9% of typical.
- Dec 29, 2020: 67 events, typical 168, 39.9% of typical.
- Jan 2, 2021: 28 events, typical 89, 31.5% of typical.
- Jan 3, 2021: 33 events, typical 73.5, 44.9% of typical.
- Jan 5, 2021: 58 events, typical 168, 34.5% of typical.
- Jan 6, 2021: 93 events, typical 193, 48.2% of typical.
- Jan 7, 2021: 67 events, typical 136, 49.3% of typical.
- Jan 8, 2021: 81 events, typical 189, 42.9% of typical.
- Jan 9, 2021: 42 events, typical 89, 47.2% of typical.
- Jan 13, 2021: 92 events, typical 193, 47.7% of typical.
- These days are excluded here because they are covered in the separate multi-event ticket: Dec 24, 2020, Dec 25, 2020, Dec 30, 2020, Dec 31, 2020, Jan 1, 2021, Jan 4, 2021 and Jan 18, 2021.

## Impact
Any analysis that uses `add_payment_info` counts for these dates may be wrong. This includes checkout funnel steps that move into or out of adding payment info. If the low counts come from lost events, these funnel steps will look weaker than they really were on these days. If the low counts reflect real customer behavior, the numbers are accurate. The check results do not show which is true.

Most flagged days fall in the late December and early January holiday period. A seasonal drop in shopping is one possible explanation, but it is unconfirmed. A tracking problem is also possible and is also unconfirmed. The overlap with the separate multi-event ticket does not prove that the two problems share a cause.

The tracking plan rates this event High if it stops arriving entirely. The event did not stop arriving on any flagged day, so that rating sets the upper limit for this ticket but does not apply directly. This ticket is Medium because the problem affects one type of analysis, the checkout funnel at the payment info step. Revenue and order counts are not taken from this event. However, these check results do not show whether purchase or other events were complete on these days.

## Suggested next steps
- Compare `add_payment_info` on the flagged days with the checkout steps just before and after it. This shows whether only this event dropped or the whole checkout flow dropped. This check did not provide those counts.
- Review whether any release, configuration change or outage affecting the payment step happened between Dec 26, 2020 and Jan 13, 2021.
- Check whether the same weeks in an earlier year show a similar holiday dip. That would support or rule out a seasonal explanation.
- Coordinate with the owner of the separate multi-event ticket so the two investigations do not repeat the same work. Keep the two cases separate until a shared cause is confirmed.

## Acceptance criteria
- The reason for the low `add_payment_info` counts on the 10 flagged days is found and documented as either a tracking problem or real customer behavior.
- If it is a tracking problem, the fix is in place. Daily `add_payment_info` counts after the fix stay at or above 0.5 of the typical count for that weekday, except on days already explained.
- If it is real behavior, the 10 flagged days are labeled so that funnel analyses covering this period can account for them.