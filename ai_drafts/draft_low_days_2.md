# add_payment_info below half of its typical daily count on 10 days between Dec 26, 2020 and Jan 13, 2021

**Event:** add_payment_info
**Found by:** · **Date found:** · **Severity:** High

## Description
An automated low-volume check flagged the `add_payment_info` event on 10 days between Dec 26, 2020 and Jan 13, 2021. On each of these days, fewer `add_payment_info` events were received than usual. The check flags a day when the count falls below 0.5 of the event's typical count. "Typical" means the median count for that weekday.

On the flagged days, the count ranged from 31.5% to 49.3% of typical. The lowest was Jan 2, 2021, at 28 events against a typical 89.

None of these 10 dates is on the holiday calendar in the tracking plan.

The check results show only how many events were received. They cannot show whether fewer people actually added payment information on these days, or whether events were sent but not received. The cause is not known.

## Evidence (Dec 26, 2020 – Jan 13, 2021)
- Dec 26, 2020: 40 events, typical 89, 44.9% of typical
- Dec 29, 2020: 67 events, typical 168, 39.9% of typical
- Jan 2, 2021: 28 events, typical 89, 31.5% of typical
- Jan 3, 2021: 33 events, typical 73.5, 44.9% of typical
- Jan 5, 2021: 58 events, typical 168, 34.5% of typical
- Jan 6, 2021: 93 events, typical 193, 48.2% of typical
- Jan 7, 2021: 67 events, typical 136, 49.3% of typical
- Jan 8, 2021: 81 events, typical 189, 42.9% of typical
- Jan 9, 2021: 42 events, typical 89, 47.2% of typical
- Jan 13, 2021: 92 events, typical 193, 47.7% of typical

The check results do not include the following:
- the weeks used to calculate each typical value
- whether other events were also low on these 10 days
- totals across all 10 days

**Related days handled elsewhere:** The event was also below the threshold on 7 more days, when many events dropped together. A separate multi-event ticket covers those days:
- Dec 24, 2020 (Christmas Eve: widely observed)
- Dec 25, 2020 (Christmas Day: widely observed)
- Dec 30, 2020
- Dec 31, 2020 (New Year's Eve: widely observed)
- Jan 1, 2021 (New Year's Day: widely observed)
- Jan 4, 2021
- Jan 18, 2021 (Martin Luther King Jr. Day: US only)

Those 7 days are not part of this ticket. The check results do not show that they share a cause with the 10 days above.

## Impact
`add_payment_info` records when a user adds payment details. It is likely to feed checkout funnels and conversion rates. Until the cause of the low counts is known, the following cannot be trusted for these 10 days:
- daily `add_payment_info` counts
- any conversion or drop-off rate that uses this event, whether at the add-payment step or between it and later steps

If events were lost, these numbers would understate real activity. If the drop reflects real behavior, the numbers are accurate. The check results cannot tell these two cases apart.

**Why High:** The tracking plan rates this event High if it stops arriving entirely. The event did not stop: events were received on every flagged day. That rating is therefore used only as the highest severity allowed here, not as the severity itself. Using the general rules, this ticket is rated High because key business numbers that depend on this event cannot be trusted for these days. This is not above the tracking plan's limit.

## Suggested next steps
- **Find out whether the drop was real.** Check whether fewer users actually reached the payment step on these 10 days, or whether the events were sent but not received. Use any independent record of checkout or payment activity available to the team.
- **Compare with other events.** Check whether other events on these same dates show similar drops. The check results do not say either way.
- **Look for changes around these dates.** Check whether anything changed in how `add_payment_info` is sent or collected around Dec 26, 2020, and again around Jan 13, 2021.
- **Get the baseline weeks.** Confirm which weeks were used to calculate each typical value, so the baseline itself can be reviewed.

## Acceptance criteria
- Each of the 10 flagged days has a documented explanation. Each is classed as either real lower activity or a data collection problem.
- For any day classed as a data collection problem, missing events are recovered where possible, and the low-volume check is re-run for that day. If events cannot be recovered, the day is clearly marked as incomplete for any funnel or conversion reporting.
- For any day classed as real lower activity, this is recorded so future checks and analyses do not treat it as a data error.