# 36.3545% of add_to_cart events are missing `quantity`

**Event:** add_to_cart
**Found by:** · **Date found:** · **Severity:** Medium

## Description
A required field coverage check flagged the `quantity` field on the `add_to_cart` event. 36.3545% of `add_to_cart` events are missing `quantity`. The check flags a field when its coverage is below 0.99.

`quantity` sits inside the `items` list of the event and is used to calculate units added to cart. According to the tracking plan, each `add_to_cart` event should carry one product, the product actually added, and that product should have `quantity`. The check measures each event as a whole. An event counts as covered if at least one of its products has `quantity`, so every flagged event has no product with `quantity` at all.

The check results do not say when this started, which dates they cover, or whether the gap is spread evenly or concentrated in certain periods. The cause is unknown and has not been confirmed.

## Evidence
- Check: required field coverage, with a threshold of 0.99.
- Field: `quantity` (location: `items`, measured per event).
- coverage_rate: 0.636455.
- Share of events missing the field: 36.3545%.
- Gap to threshold: 35.3545 percentage points.
- Missing from the check results: the date range checked, the total number of `add_to_cart` events, the number of events missing `quantity`, and any daily or per-product breakdown.

## Impact
The check results list one use for `quantity`: units added to cart. Any units added to cart total built from these events cannot be trusted, because 36.3545% of events give no quantity to count. The check results do not show how missing quantities are currently treated, for example whether they are skipped or counted as a default value, so the direction and size of the error in that total are unknown.

This is Medium rather than High. Units added to cart is a secondary total, and the check results do not show any key business number, such as revenue, orders, units sold or conversion rates, that depends on `quantity` in `add_to_cart`. This check only covers `quantity`. It says nothing about whether the rest of the `add_to_cart` data is complete, so it should not be read as confirming that add-to-cart counts are correct.

## Suggested next steps
- Get the date range behind this check, along with daily coverage of `quantity`, to see whether the gap began on a particular date or has always been present.
- Break the missing `quantity` events down by any available dimension, such as platform, app version or product, to find where the gap is concentrated.
- Confirm how reports that show units added to cart currently handle events with no `quantity`, and whether anyone uses those reports for decisions.
- Check whether `add_to_cart` events really contain one product each, as the tracking plan expects. Events with zero products or several products would change how this gap should be read.

## Acceptance criteria
- Coverage of `quantity` on `add_to_cart` events is at or above the 0.99 threshold in the required field coverage check.
- The date range affected by the gap is identified and recorded, so that units added to cart reporting for that range can be flagged or excluded.