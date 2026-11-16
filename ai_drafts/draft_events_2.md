# No `refund` events received from Nov 1, 2020 to Jan 31, 2021

**Event:** refund
**Found by:** · **Date found:** · **Severity:** High

## Description
The tracking plan lists `refund` as an active event, but the check results show no `refund` rows were received at any point between Nov 1, 2020 and Jan 31, 2021. The automated planned-events check flagged this. That check flags any event that the tracking plan lists as active but that never appears in the data.

The check results only show what was received. They do not show whether any refunds actually took place in this period. The cause is not confirmed. Possible explanations include:
- the event was never sent
- the event was sent under a different name
- no refunds occurred

## Evidence (Nov 1, 2020 – Jan 31, 2021)
- Rows received for `refund` in the whole period: 0.
- The tracking plan lists `refund` as active.
- According to the tracking plan, `refund` is used in refunds and net revenue reporting.
- Source: automated planned-events check.

## Impact
The tracking plan sets the severity to High.

The tracking plan says `refund` feeds both refunds and net revenue. With no `refund` rows in the period, neither number can be trusted for Nov 1, 2020 to Jan 31, 2021:
- **Refunds:** any refund total for this period will show nothing. The check results cannot tell us whether that reflects real activity or missing tracking.
- **Net revenue:** if refunds did occur and were not recorded, net revenue for this period would not account for them.

Net revenue is a key business number, which supports the High rating.

The check results do not include any refund counts or amounts from another source. The size of any gap is therefore unknown.

## Suggested next steps
- Confirm whether the `refund` event was ever implemented and released, and if so, from what date.
- Check whether refund activity is being sent under a different event name than the one in the tracking plan.
- Compare against any independent record of refunds for Nov 1, 2020 to Jan 31, 2021, if one exists. This would show whether refunds took place in this period.
- Identify any reports or analyses of refunds or net revenue that cover this period, and flag them as unreliable until this is resolved.

## Acceptance criteria
- When a refund occurs, a `refund` event is received, matching the name listed in the tracking plan.
- For Nov 1, 2020 to Jan 31, 2021, one of the following is documented:
  - the refund activity is confirmed and backfilled where possible, or
  - it is confirmed that no refunds occurred, and the tracking plan is checked to make sure `refund` is correctly marked as active.
- Refunds and net revenue reporting for this period carry a note explaining the outcome.