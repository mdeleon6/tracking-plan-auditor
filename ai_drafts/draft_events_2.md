# No `refund` events received from Nov 1, 2020 to Jan 31, 2021

**Event:** refund
**Found by:** · **Date found:** · **Severity:** High

## Description
The tracking plan lists `refund` as an active event, but the check results show no `refund` rows at all between Nov 1, 2020 and Jan 31, 2021. The automated planned-events check flagged this. It flags any event that the tracking plan marks as active but that never appears in the data.

The check results do not show whether any refunds actually took place in this period. Zero rows could mean refunds happened and were not recorded, or that no refunds happened. The check results do not confirm which one is true, and they do not give a cause.

## Evidence (Nov 1, 2020 – Jan 31, 2021)
- Check: planned events. It flags events that the tracking plan lists as active but that never appear in the data.
- Rows received for `refund` in the whole period: 0.
- Tracking plan status for `refund`: active.
- Tracking plan lists `refund` as used in: refunds, net revenue.
- The check results do not include an expected number of refunds for this period, so it is not possible to say how many, if any, may be missing.
- The check results do not include a query or file reference.

## Impact
According to the tracking plan, `refund` feeds the refunds reporting and net revenue. Net revenue is a key business number. If any refunds took place in this period, they are not in the data, so the refund figures and net revenue for Nov 1, 2020 to Jan 31, 2021 cannot be trusted until someone confirms whether refunds occurred.

The tracking plan sets the severity to High. This matches the severity guidance, because a key business number (net revenue) depends on this event.

## Suggested next steps
- Find out from a source outside this tracking data whether any refunds were issued between Nov 1, 2020 and Jan 31, 2021. This will show whether the zero count reflects missing tracking or a real absence of refunds.
- Confirm whether `refund` tracking was actually built and released before Nov 1, 2020. If it was not, ask the tracking plan owner whether the event should be listed as active for this period.
- Check whether refunds might be recorded under a different event name or inside another event. Treat this as an open question; it has not been confirmed.
- Identify any net revenue or refund reports that cover this period, so their users know the figures may be incomplete.

## Acceptance criteria
- The ticket records whether refunds occurred between Nov 1, 2020 and Jan 31, 2021, based on a source outside this tracking data.
- If refunds occurred, a `refund` event is received for each refund going forward, and its count matches the independent refund record.
- The tracking plan status for `refund` is correct for every date range it covers.
- Net revenue and refund reports that cover Nov 1, 2020 to Jan 31, 2021 are either corrected or clearly marked as possibly incomplete.