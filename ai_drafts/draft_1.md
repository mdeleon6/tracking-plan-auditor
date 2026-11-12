# 36.3545% of add_to_cart events are missing `quantity` on the added product

**Event:** add_to_cart
**Found by:** · **Date found:** · **Severity:** Medium

## Description
The `add_to_cart` event should include a `quantity` value inside `items` for the product added to the cart. 36.3545% of `add_to_cart` events have no product with `quantity`.

Under the tracking plan, each event should carry one product in `items`: the product that was added. This check counts an event as covered if at least one of its products has `quantity`. The flagged events therefore have `quantity` missing on every product they carry.

The check results do not give a date range, the number of events checked, or the number of events missing `quantity`. They also do not say whether the missing values cluster on certain days or in certain parts of the data. The cause is not known.

## Evidence
- Check: required field coverage. A field is flagged when its coverage is below 0.99.
- `quantity` (location: `items`, measured per event): coverage_rate 0.636455.
- Share of events missing `quantity`: 36.3545%.
- Gap to the 0.99 threshold: 35.3545 percentage points.
- Not in the check results: date range, total event count, count of affected events, and any breakdown by day or other dimension.

## Impact
The check results list `quantity` as an input to **units added to cart**. Because 36.3545% of events lack it, that total cannot be built from the reported quantities for those events. The resulting figure will be incomplete or will depend on an assumption about the missing values.

This is rated **Medium**. Units added to cart is a secondary total, and the check results do not show any key business number that uses this field, such as revenue, orders, units sold, or conversion rates. If a key business number is found to use `add_to_cart` `quantity`, raise the severity to High.

These checks only show that the field is missing. They do not show that other `add_to_cart` fields, or totals built from them, are complete or correct.

## Suggested next steps
- Find out which reports and metrics read `quantity` from `add_to_cart`. Confirm that no key business number depends on it.
- Find out how those reports currently handle a missing `quantity`, for example by skipping the event or by assuming a default value.
- Break the affected events down by date, and by any other dimensions available. This will show whether the gap started at a particular point or affects only part of the traffic.
- Check the `add_to_cart` implementation to see whether `quantity` is set on the product in `items` in every case where the event fires.

## Acceptance criteria
- `quantity` coverage on `add_to_cart` is at or above the 0.99 threshold when the required field coverage check is run again.
- The period affected by the gap is identified and recorded, so that analyses of units added to cart can exclude it or flag it.