# `purchase` events fell below half their typical daily count on 7 days between Nov 5, 2020 and Jan 8, 2021

**Event:** purchase
**Found by:** · **Date found:** · **Severity:** High

## Description
An automated low-volume check flagged 7 days on which far fewer `purchase` events arrived than usual. The check flags a day when an event's count is below 0.5 of its typical count. "Typical" means the median count for that weekday. On every flagged day, the `purchase` count was under half of typical.

Four of the flagged days are consecutive, from Jan 5 to Jan 8, 2021. The other flagged days are Nov 5, 2020, Dec 29, 2020 and Jan 2, 2021.

The check results do not show whether fewer purchases actually happened on these days or whether purchases happened but were not received. Either is possible.

`purchase` was also below the threshold on 6 more days. On those days, many events dropped together. A separate multi-event ticket covers those days, so this ticket does not.

## Evidence (Nov 5, 2020 – Jan 8, 2021)
- Check: low volume. A day is flagged when the count is below 0.5 of the median for that weekday.
- Nov 5, 2020: 26 events against a typical 54 (48.1% of typical).
- Dec 29, 2020: 24 events against a typical 60 (40.0% of typical).
- Jan 2, 2021: 14 events against a typical 31 (45.2% of typical).
- Jan 5, 2021: 29 events against a typical 60 (48.3% of typical).
- Jan 6, 2021: 31 events against a typical 67 (46.3% of typical).
- Jan 7, 2021: 26 events against a typical 54 (48.1% of typical).
- Jan 8, 2021: 34 events against a typical 79 (43.0% of typical).
- These days are excluded from this ticket because they are in the separate multi-event ticket: Dec 24, 2020, Dec 25, 2020, Dec 31, 2020, Jan 1, 2021, Jan 4, 2021 and Jan 18, 2021.

## Impact
`purchase` is the event behind order counts, and probably behind revenue and conversion rates, though the check results do not confirm this. For these 7 days, the check results cannot tell us whether the low counts show real customer behavior or purchases that were not recorded. Until that is known, order totals and any numbers built on them cannot be trusted for these days. This includes daily and weekly order totals, revenue and purchase conversion rates. The four-day run from Jan 5 to Jan 8, 2021 affects a full working week, so weekly reporting is also at risk.

The severity is High because the affected numbers are key business totals. The tracking plan rates `purchase` as High only if the event stops arriving entirely. This event did not stop arriving, because events were received on every flagged day. High is therefore the maximum severity allowed here. It is also the level that the severity rules give, because order totals are the numbers in question.

Several flagged days fall in the late-December and early-January period. A possible explanation is a seasonal drop in real purchasing, but this is unconfirmed. The check results contain nothing that shows the cause of the drops.

## Suggested next steps
- Compare `purchase` counts for each flagged day with an independent record of orders, such as the order or payment system. This will show whether the purchases happened and were not tracked, or did not happen.
- Find out whether any tracking, website or app releases, outages or configuration changes happened around Nov 5, 2020, Dec 29, 2020, Jan 2, 2021 and Jan 5–8, 2021.
- For Jan 5–8, 2021, check whether the drop was spread evenly across platforms, browsers or regions, or limited to one segment.
- Check whether the drop on these days is limited to `purchase` or also shows up in earlier steps such as checkout. This will help separate fewer shoppers from purchases that were not recorded.
- Coordinate with whoever owns the separate multi-event ticket. Do not assume the two tickets share a cause unless that is confirmed.

## Acceptance criteria
- Each of the 7 flagged days is labeled with a confirmed explanation: either a real drop in purchases, or a tracking loss. If it was a tracking loss, the label states the scope of the loss.
- If any day turns out to be a tracking loss, the missing purchases are either backfilled or clearly marked as incomplete in reporting, and the fix is documented.
- After the fix, `purchase` counts on comparable days stay at or above 0.5 of the typical count for the same weekday, unless a confirmed real-world reason explains the drop.