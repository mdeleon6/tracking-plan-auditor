# `quantity` is missing for 94.4174% of products in `add_to_cart` events (date range not given)

**Event:** add_to_cart
**Found by:** · **Date found:** · **Severity:** Medium

## Description
An automated check measures how often required fields are filled in. It flags any field with coverage below 0.99. It flagged the `quantity` field on the `add_to_cart` event.

`quantity` sits inside the `items` list and is measured per product. It is filled in for only a small share of products added to cart, so most cart additions do not record how many units were added.

The check results do not include a date range, event or product counts, or a breakdown by day, platform or product. It is not known whether the gap covers the whole period or only part of it.

## Evidence
- Field: `quantity`. Location: `items`, measured per product.
- Coverage rate: 0.055826. The flag threshold is 0.99.
- Share of products missing `quantity`: 94.4174%.
- Gap to threshold: 93.4174 percentage points.
- The check results list "units added to cart" as the metric that uses this field.
- Missing from the check results: the date range, the number of products checked and the number missing `quantity`.

## Impact
"Units added to cart" depends on `quantity`. With the field missing for 94.4174% of products, that total cannot be relied on for the checked period. Any breakdown of units added to cart by product, category or other dimension is affected in the same way.

The severity is Medium because "units added to cart" is a secondary total. It is not one of the key business numbers such as revenue, orders, units sold or conversion rates. The check results do not show that any key business number depends on `quantity` in `add_to_cart`. If a team uses this field to calculate a key number, the severity should be reassessed. The check results do not give a severity from the tracking plan.

## Suggested next steps
- Get the date range the check covered and the counts behind the 0.055826 coverage rate.
- Look at coverage by day to see whether `quantity` was never sent, stopped at some point, or has always been sent only in some cases.
- Compare the products that have `quantity` with those that do not, for example by platform, app version, page or product type, to find what the populated cases have in common.
- Confirm with the owners of the tracking plan whether `quantity` is meant to be sent with every product in `add_to_cart`. A possible, unconfirmed explanation is that the field is only set up in some places where products can be added to cart. This needs checking before any fix is chosen.
- Find any reports or dashboards that show units added to cart, and tell their users the figure is not reliable until this is fixed.

## Acceptance criteria
- `quantity` coverage on products in `add_to_cart` events is at or above 0.99, and the required field coverage check no longer flags it.
- The period affected by the gap is documented, so that analyses of units added to cart can exclude or label it.