# add_shipping_info arrived below half its typical volume on 12 days from Dec 26, 2020 to Jan 15, 2021

**Event:** add_shipping_info
**Found by:** · **Date found:** · **Severity:** Medium

## Description
The `add_shipping_info` event was received at less than half its typical daily volume on 12 days between Dec 26, 2020 and Jan 15, 2021. The check calls a day "typical" based on the median count for that weekday, and it flags a day when the count falls below 0.5 of that median. On these 12 days, the event arrived at between 32.4% and 49.4% of typical.

The event did not stop arriving. Events were received on every flagged day, just in lower numbers than usual.

The check results do not say why the counts were low. The period overlaps the end-of-year holidays, so the drop **could possibly** reflect real changes in shopper behavior. This is unconfirmed. A tracking problem is also possible and also unconfirmed. Low counts alone do not show which one it is.

This event was also below the threshold on 7 more days: Dec 24, 2020, Dec 25, 2020, Dec 30, 2020, Dec 31, 2020, Jan 1, 2021, Jan 4, 2021 and Jan 18, 2021. On those days, many events dropped together, so they are covered in a separate multi-event ticket and not here. The fact that these days fall in the same window does not show that they share a cause with the 12 days in this ticket.

## Evidence (Dec 26, 2020 – Jan 15, 2021)
- Check used: low volume. A day is flagged when the count is below 0.5 of the median for that weekday.
- Number of flagged days: 12.
- Dec 26, 2020: 48 events, typical 148, 32.4% of typical.
- Dec 28, 2020: 101 events, typical 211, 47.9% of typical.
- Dec 29, 2020: 80 events, typical 233, 34.3% of typical.
- Jan 2, 2021: 48 events, typical 148, 32.4% of typical.
- Jan 3, 2021: 51 events, typical 129.5, 39.4% of typical.
- Jan 5, 2021: 88 events, typical 233, 37.8% of typical.
- Jan 6, 2021: 116 events, typical 248, 46.8% of typical.
- Jan 8, 2021: 105 events, typical 269, 39.0% of typical.
- Jan 9, 2021: 58 events, typical 148, 39.2% of typical.
- Jan 10, 2021: 58 events, typical 129.5, 44.8% of typical.
- Jan 11, 2021: 94 events, typical 211, 44.5% of typical.
- Jan 15, 2021: 133 events, typical 269, 49.4% of typical.
- **Not included in the check results:**
  - Total `add_shipping_info` counts for the period.
  - Counts for the days that were not flagged.
  - Counts for related events, such as checkout starts or purchases, on these days.

## Impact
`add_shipping_info` marks a step in the checkout process. Any analysis that relies on this step cannot be trusted for the 12 flagged days until the reason for the low counts is known. This includes checkout funnel reports and the share of shoppers moving through the shipping step.

The tracking plan rates this event High if it stops arriving entirely. That did not happen here, because the event was still received on every flagged day. For that reason, High is the highest severity this problem can have. It is not automatically the severity of this ticket.

This ticket is rated **Medium** because the problem affects one type of analysis: the checkout steps that use `add_shipping_info`. The check results cover only this event. They do not show a drop in purchase or revenue events on these days, so there is no evidence here that those totals are affected. They also do not show that those totals are correct, because data for those events is not part of the check results.

If later checks find that purchase or revenue events also dropped on these same days, the severity should be reviewed against the High rule.

## Suggested next steps
- **Compare with nearby checkout events.** Look at checkout start and purchase counts on the 12 flagged days. If those events stayed at normal levels while `add_shipping_info` dropped, a tracking problem becomes more likely. If they dropped by a similar amount, real shopper behavior becomes more likely. Neither result confirms the cause alone.
- **Look for changes around Dec 26, 2020.** Check whether any site, app or tracking changes went live near the first flagged day that could affect how `add_shipping_info` is sent.
- **Break down the flagged days.** Split the counts by platform, browser or app version to see whether the drop is limited to one group.
- **Review the separate multi-event ticket.** Keep the 7 days covered in that ticket separate from this one unless a shared cause is confirmed.

## Acceptance criteria
- Each of the 12 flagged days has a confirmed explanation, labeled as either real shopper behavior or a tracking problem.
- If a tracking problem is confirmed:
  - It is fixed.
  - Later `add_shipping_info` counts no longer fall below 0.5 of the weekday median for reasons tied to that problem.
  - Analysts are told which of the 12 days to leave out of checkout funnel analysis.
- If real behavior is confirmed, the days are documented as expected seasonal lows so future low-volume checks can be read in that context.