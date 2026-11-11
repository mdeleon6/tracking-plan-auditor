# add_shipping_info below half its typical daily count on 12 days, Dec 26, 2020 – Jan 15, 2021

**Event:** add_shipping_info
**Found by:** · **Date found:** · **Severity:** Medium

## Description
The `add_shipping_info` event arrived in low volume on 12 days between Dec 26, 2020 and Jan 15, 2021. A low-volume check flags a day when an event's count is below 0.5 of its typical count. Here, "typical" means the median count for that weekday. On the 12 flagged days, the event arrived at between 32.4% and 49.4% of typical.

The event did not stop arriving. It was received on every flagged day, just at lower counts.

The check results also show this event was below the threshold on 7 more days when many events dropped at the same time. Those days are handled in a separate multi-event ticket and are not part of this one: Dec 24, 2020; Dec 25, 2020; Dec 30, 2020; Dec 31, 2020; Jan 1, 2021; Jan 4, 2021; Jan 18, 2021.

The check results do not say why the counts are low. Two explanations are possible:
- Fewer users reached this step.
- Some events were not received.

Neither is confirmed.

## Evidence (Dec 26, 2020 – Jan 15, 2021)
| Date | Events received | Typical | % of typical |
|---|---|---|---|
| Dec 26, 2020 | 48 | 148 | 32.4% |
| Dec 28, 2020 | 101 | 211 | 47.9% |
| Dec 29, 2020 | 80 | 233 | 34.3% |
| Jan 2, 2021 | 48 | 148 | 32.4% |
| Jan 3, 2021 | 51 | 129.5 | 39.4% |
| Jan 5, 2021 | 88 | 233 | 37.8% |
| Jan 6, 2021 | 116 | 248 | 46.8% |
| Jan 8, 2021 | 105 | 269 | 39.0% |
| Jan 9, 2021 | 58 | 148 | 39.2% |
| Jan 10, 2021 | 58 | 129.5 | 44.8% |
| Jan 11, 2021 | 94 | 211 | 44.5% |
| Jan 15, 2021 | 133 | 269 | 49.4% |

**Holiday calendar:**
- None of the 12 flagged days in this ticket has a holiday name in the check results, so none of them is on the tracking plan's holiday calendar.
- Some of the 7 days in the separate ticket do have names: Dec 24, 2020 (Christmas Eve, widely observed), Dec 25, 2020 (Christmas Day, widely observed), Dec 31, 2020 (New Year's Eve, widely observed), Jan 1, 2021 (New Year's Day, widely observed) and Jan 18, 2021 (Martin Luther King Jr. Day, US only).
- It is possible, but unconfirmed, that the flagged days were affected by being close to these holidays. The flagged days themselves are not holidays on the calendar.

**Missing from the check results:**
- Counts for this event outside the flagged days, including whether volume returned to typical after Jan 15, 2021.
- Counts for any other event on the 12 flagged days.

## Impact
`add_shipping_info` records one step in checkout. It does not record orders or revenue. Any analysis that uses this step will show lower counts on the 12 flagged days, for example the share of users moving from one checkout step to the next. If the low counts are caused by events that were not received, those step-to-step rates for these days will be wrong. If the low counts reflect real user behavior, the numbers are correct.

The check results contain no information about orders, revenue or other events on these days. This ticket does not establish whether those numbers are affected.

**Severity reasoning:**
- The tracking plan rates this event High, but only if it stops arriving entirely. It kept arriving on every flagged day, so High is the highest severity allowed here, not the automatic one.
- Based on what is known, the problem affects one type of analysis: checkout analysis that uses the `add_shipping_info` step.
- No key business totals are shown to be affected, so Medium applies.
- If later investigation shows that orders, revenue or overall conversion are affected, the severity should be reassessed under the High rule.

## Suggested next steps
- Compare `add_shipping_info` counts on the 12 flagged days with the checkout steps before and after it. This will show whether only this event dropped or the whole checkout flow dropped.
- Find out whether any changes to the site, app or tracking setup were released between late December 2020 and mid-January 2021 that could affect when this event is sent.
- Check whether the event's daily counts returned to typical after Jan 15, 2021. The check results do not include those days.
- Coordinate with the owner of the separate multi-event ticket. Both tickets cover nearby dates, but sharing nearby dates does not show that they share a cause.

## Acceptance criteria
- Each of the 12 flagged days has a documented explanation. The explanation either confirms real lower user activity or identifies missing events.
- If events were lost, the tracking problem is fixed. Recoverable data is restored, or the affected days are clearly marked as incomplete for any analysis that uses this event.
- If the drop is confirmed as real behavior, the 12 days are noted as expected low-volume days so they are not treated as a tracking failure in future reviews.