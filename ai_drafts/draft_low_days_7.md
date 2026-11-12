# `select_item` events dropped to 16.6% of typical volume on Nov 23, 2020

**Event:** select_item
**Found by:** · **Date found:** · **Severity:** Medium

## Description
On Nov 23, 2020, 59 `select_item` events were received, compared with a typical count of 356, which is 16.6% of typical. "Typical" here means the median count for the same weekday. The low-volume check flags a day when an event's count falls below 0.5 of typical, and this day falls well under that line.

Nov 23, 2020 is the only day flagged for this event in this ticket. It is not on the holiday calendar in the tracking plan.

The check results also show that `select_item` has no data at all from Nov 1, 2020 to Nov 22, 2020, so Nov 23 is the first day with data after that gap. A possible, unconfirmed explanation is that data collection for this event resumed partway through Nov 23, which would leave only part of the day recorded. The check results do not confirm this, and the two problems may not share a cause.

## Evidence
- Nov 23, 2020: 59 `select_item` events received, typical 356, 16.6% of typical.
- Flag rule: a day is flagged when the count is below 0.5 of the median for that weekday.
- Number of days flagged for this ticket: 1.
- No queries were included in the check results.

**Covered in separate tickets, not part of this one:**
- Dec 31, 2020 (New Year's Eve, widely observed): `select_item` was also below the threshold on this day, but many events dropped together. This is covered in a separate multi-event ticket.
- Nov 1, 2020 to Nov 22, 2020: no `select_item` data was received on these days. This is covered in a separate missing-day ticket.

## Impact
According to the tracking plan, `select_item` is used for product list click-through rate and item selection reporting.

- **Click-through rate:** for Nov 23, 2020, this rate may be understated if the clicks were not fully received.
- **Item selection reporting:** any weekly or monthly totals that include Nov 23, 2020 may be understated.

The check results only show what was received. They cannot tell us whether fewer item selections actually happened that day or whether events were not captured.

**Why Medium:**
- The affected numbers are a secondary rate and one reporting area.
- None of the key business numbers named in the severity guidelines (revenue, orders, units sold or conversion rates) are listed as depending on this event.
- The tracking plan rates a complete stop of this event as Medium. A drop on a single day should not rank higher than that.
- It is not rated Low, because the drop is large enough to make that day's click-through rate unreliable for anyone reading daily figures.

## Suggested next steps
- Find out when `select_item` tracking started or resumed after the Nov 1–22 gap. Check whether events on Nov 23 arrive across the whole day or only from a certain time onward.
- Check whether other events also show low counts on Nov 23, 2020. The check results do not list this date as a multi-event day, so this is still unknown.
- If events for Nov 23 can be recovered, re-load them and re-run the low-volume check for that date.
- If the events cannot be recovered, agree with the people who own product list click-through rate how to treat Nov 23, 2020 in reporting.

## Acceptance criteria
- The reason for the low count on Nov 23, 2020 is confirmed and written on this ticket. This includes whether it is related to the Nov 1–22 missing-day gap.
- One of the following is true:
  - The Nov 23, 2020 count is no longer flagged by the low-volume check after any re-load.
  - The date is clearly marked or excluded wherever product list click-through rate and item selection reporting are shown.