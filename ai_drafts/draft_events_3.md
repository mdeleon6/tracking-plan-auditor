# `remove_from_cart` was never received from Nov 1, 2020 to Jan 31, 2021

**Event:** remove_from_cart
**Found by:** · **Date found:** · **Severity:** Low

## Description
The tracking plan lists `remove_from_cart` as an active event, but no rows for it were received at any point from Nov 1, 2020 to Jan 31, 2021. The automated planned-events check flagged it. That check flags any event the tracking plan marks as active that never appears in the data.

The check results do not say why the event is absent. Zero rows shows only that nothing was received. It does not show whether shoppers removed items from their carts during this period.

## Evidence (Nov 1, 2020 – Jan 31, 2021)
- Rows received for `remove_from_cart` in the whole period: 0.
- Tracking plan status for `remove_from_cart`: active.
- Tracking plan use for `remove_from_cart`: cart removal reporting.
- Source: automated planned-events check.

## Impact
Cart removal reporting has no data for this period. Any view of cart removals for Nov 1, 2020 to Jan 31, 2021 will be empty or show zero. Nobody can tell from the data whether that reflects real shopper behavior or a tracking gap.

Severity is Low because the tracking plan sets it to Low. According to the plan, the event is used only in cart removal reporting. The check results do not show any key business number, such as revenue, orders, units sold or conversion rates, that depends on this event.

## Suggested next steps
- Confirm whether `remove_from_cart` was ever built and released, or whether it is listed as active in the tracking plan before being implemented.
- Confirm whether the site or app lets shoppers remove items from their cart. This will show whether the event should be expected at all.
- Find out who uses cart removal reporting and whether the missing period affects any decisions they make.
- If cart removal reporting turns out to feed any key business number, ask the tracking plan owner to review the Low rating.

## Acceptance criteria
- `remove_from_cart` events are received whenever a shopper removes an item from their cart. Alternatively, the tracking plan is updated to mark the event as not active if it is not meant to be sent.
- Cart removal reporting notes that no `remove_from_cart` data exists for Nov 1, 2020 to Jan 31, 2021. Zero rows for this period should not be read as zero cart removals.