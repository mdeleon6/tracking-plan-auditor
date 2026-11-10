# 94.4174% of products in add_to_cart events are missing `quantity`

**Event:** add_to_cart
**Found by:** · **Date found:** · **Severity:** Medium

## Description
An automated check found that most products in `add_to_cart` events have no `quantity`. The field sits inside the `items` list of the event and was measured per product, not per event. The check flags a field when its coverage is below 0.99. `quantity` had a coverage rate of 0.055826, so 94.4174% of products are missing it.

`quantity` is the only flagged field. The cause is not known, and the input does not say when the problem started or whether it affects all dates equally.

## Evidence (date range missing)
- Check: required field coverage, which flags a field when coverage is below 0.99.
- `quantity` (location: `items`, measured per product): coverage rate 0.055826.
- Share of products missing `quantity`: 94.4174%.
- Gap to threshold: 93.4174 percentage points.
- **Missing from the input:**
  - The date range checked.
  - The number of `add_to_cart` events and products checked, and how many were missing `quantity`.
  - Any daily or weekly breakdown.
  - Any query or link to the check.

## Impact
Any analysis that relies on how many units were added to cart cannot be trusted. Examples include units per add-to-cart and cart value calculated as price × quantity. Because almost all products lack `quantity`, these numbers would describe only a small, possibly unrepresentative share of products.

I set this to Medium rather than High because the input points to only one type of analysis being affected. The count of `add_to_cart` events does not depend on `quantity`, and neither do purchase-based totals such as revenue and orders. This assumes the team does not report any key business number built on `add_to_cart` quantity. If it does, for example cart value, raise this to High.

## Suggested next steps
- Get the missing details: the date range checked, the event and product counts, and the number of products missing `quantity`.
- Break coverage down by day to see whether `quantity` was never sent or stopped being sent at a certain point.
- Check whether the missing values are concentrated in a particular platform, page or product type. The input does not include this breakdown.
- Confirm with whoever owns the `add_to_cart` tracking whether `quantity` is expected to be sent for every product in `items`.
- Check whether other events that use `items` (for example `purchase`) have the same gap. This check did not cover them.

## Acceptance criteria
- Coverage of `quantity` in `add_to_cart` `items` is at or above 0.99, measured per product, and the check no longer flags it.
- The affected date range is documented, so analyses that use `add_to_cart` quantity exclude or clearly label the period with missing values.