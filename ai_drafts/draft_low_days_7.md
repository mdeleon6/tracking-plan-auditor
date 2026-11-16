# `select_item` received at 16.6% of typical volume on Nov 23, 2020

**Event:** select_item
**Found by:** · **Date found:** · **Severity:** Medium

## Description
On Nov 23, 2020, 59 `select_item` events were received. The typical count for that day is 356, so the day came in at 16.6% of typical. This is the only day flagged for this event in this ticket.

The low-volume check flags a day when an event's count falls below 0.5 of its typical count. The typical count is the median for the same weekday. This check only shows what was received. It cannot show whether fewer item selections actually happened that day or whether events were lost before they reached the data.

## Evidence
- **Flagged day:** Nov 23, 2020 had 59 events, against a typical count of 356 (16.6% of typical).
- **Holiday calendar:** Nov 23, 2020 has no holiday name in the check results, which means it is not on the tracking plan's holiday calendar.
- **No data before this day:** The check results show no `select_item` data at all from Nov 1, 2020 to Nov 22, 2020. Nov 23 is the first day after that range. A separate missing-day ticket covers that range, and it is not part of this ticket. The check results do not show whether the two problems are connected.
- **Other low day:** `select_item` was also below the threshold on 1 other day, Dec 31, 2020 (New Year's Eve: widely observed), when many events dropped together. A separate multi-event ticket covers that day, and it is not part of this ticket.
- **Missing information:** The check results do not include the following:
  - counts for other events on Nov 23, 2020
  - counts for `select_item` on the days after Nov 23
  - the time of day at which events arrived on Nov 23

## Impact
According to the tracking plan, `select_item` is used in:
- product list click-through rate
- item selection reporting

If the low count on Nov 23, 2020 does not reflect real behavior, then both of these are unreliable for that day. Any weekly or monthly figure that includes that day would also be affected. The size of the effect on those longer periods is not in the check results.

**Severity: Medium.** The reasons are:
- Product list click-through rate and item selection reporting are secondary measures. According to the tracking plan, no key business number depends on this event, such as revenue, orders, units sold or overall conversion.
- The problem affects one day only. However, the drop is large: 59 events against a typical 356.
- The tracking plan rates this event Medium even if it stopped arriving entirely. A one-day drop should not be rated higher than that.

**Possible explanations (unconfirmed):**
- Nov 23 directly follows a range with no `select_item` data. One possibility is that tracking was only partly working on its first day back.
- Another possibility is that activity was genuinely low that day.

Neither explanation is supported by the check results.

## Suggested next steps
- Find out whether `select_item` tracking started or was restored on Nov 23, 2020, and at what time. If it resumed partway through the day, that could account for part of the low count. Confirm this before treating it as the cause.
- Compare Nov 23, 2020 with the event used as the denominator of product list click-through rate. The name of that event is not in the check results. If that event was normal on Nov 23 while `select_item` was low, the day's click-through rate will look artificially low.
- Check whether other events were also low on Nov 23, 2020. This will show whether the drop was limited to `select_item`.
- Check the `select_item` counts for the days after Nov 23, 2020 to confirm volume returned to typical levels.
- Find out whether the source system can resend data for Nov 23, 2020. If it can, re-run the low-volume check on the resent data.

## Acceptance criteria
One of the following is true:
- The `select_item` count for Nov 23, 2020 is restored to at least 0.5 of its typical count, and the low-volume check no longer flags the day.
- The low count is confirmed as either real behavior or a known tracking gap, and the finding is recorded in the tracking plan.

In addition, if the day cannot be corrected, any product list click-through rate or item selection report covering Nov 23, 2020 carries a note that `select_item` was at 16.6% of typical on that day.