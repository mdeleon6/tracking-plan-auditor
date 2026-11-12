# 36.3545% of add_to_cart events are missing `quantity` on the added product

**Event:** add_to_cart
**Found by:** · **Date found:** · **Severity:** Medium

## Description
A required field coverage check flagged the `add_to_cart` event because the `quantity` field is missing on many events. This field sits on the products inside the event (`items`) and is used to count units added to cart.

The tracking plan expects `quantity` on one product per event, the product that was actually added. The check counts an event as covered if at least one of its products has `quantity`. Under that rule, 36.3545% of `add_to_cart` events have no product with `quantity`.

The check results do not include a date range, event counts, or a day-by-day breakdown. It is therefore not yet known when the problem started, whether it is ongoing, or how many events are affected.

## Evidence
- Check: required field coverage. A field is flagged when its coverage is below 0.99.
- Flagged field: `quantity` (location: `items`, measured per event).
- Coverage rate for `quantity`: 0.636455.
- Share of `add_to_cart` events missing `quantity`: 36.3545%.
- Gap to threshold: 35.3545 percentage points.
- The check results do not include:
  - the date range checked
  - total or affected event counts
  - a breakdown by day or by any other dimension

## Impact
Units added to cart cannot be trusted. That total depends on `quantity`, and more than a third of `add_to_cart` events do not carry it. Any total, trend or breakdown built on units added to cart will be incomplete. The size of the effect on that total is not known, because the check results do not include event counts or quantities.

This is Medium rather than High. The check results list units added to cart as the only use of this field. Units added to cart is a secondary total and is not one of the key business numbers such as revenue, orders, units sold or conversion rates. The check results show no key business number that depends on `quantity` in `add_to_cart`. If another report turns out to use this field for a key number, the severity should be reviewed.

## Suggested next steps
- Get the date range the check covered, plus total and affected event counts, so the size of the problem can be stated in events rather than only as a rate.
- Break down missing `quantity` by day. This will show whether the gap began on a specific date or has been present throughout.
- Compare events that have `quantity` with events that lack it, using any available dimensions such as platform or page. The goal is to find what the affected events have in common. This would only describe the pattern and would not confirm a cause.
- Confirm with whoever owns the tracking plan how `quantity` should be sent on `add_to_cart`. Also confirm whether the item that was actually added should always include it.
- Until the field is fixed, agree how reports should treat events missing `quantity`. Do not assume a default value without confirming it with the owner of the tracking plan.

## Acceptance criteria
- Every `add_to_cart` event includes `quantity` on the product that was actually added.
- The required field coverage check for `quantity` on `add_to_cart` reaches at least 0.99, so the field is no longer flagged.
- The date range affected by the missing `quantity` is identified and documented, so analyses of units added to cart can exclude or flag that period.