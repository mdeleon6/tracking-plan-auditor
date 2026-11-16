# 2.8% of products in `purchase` events are missing `item_id`, `item_name`, `item_category`, `price` and `quantity` (Nov 1, 2020 – Jan 31, 2021)

**Event:** purchase
**Found by:** · **Date found:** · **Severity:** High

## Description
An automated check found five product-level fields on the `purchase` event below the required coverage level. The check flags a field when its coverage is below 0.99. Each of the five fields has 97.2% coverage, meaning 2.8% of products in purchases have no value for that field.

All five fields sit in the `items` part of the event and are measured per product. They are used for units sold and for revenue broken down by product, product version and category.

The five fields have identical coverage. However, the check results do not show whether the same products are missing all five fields or whether different products are missing different fields. This needs to be confirmed.

## Evidence (Nov 1, 2020 – Jan 31, 2021)
- Check: required field coverage, threshold 0.99.
- Coverage for each flagged field: 97.2%.
- Share of products missing each field: 2.8%.
- Gap to threshold: 1.8 percentage points.
- Flagged fields and where they are used, as listed in the check results:
  - `item_id`: revenue and units by exact product version, such as colour or size.
  - `item_name`: revenue and units by product name, grouping all versions.
  - `item_category`: revenue by category.
  - `price`: revenue by product, average selling price.
  - `quantity`: units sold, revenue by product.
- The check results do not include:
  - the number of products or purchases affected
  - a day-by-day breakdown
  - whether the missing values overlap across fields
  - whether purchase-level totals are affected

## Impact
Severity is High because `quantity` is used for units sold, which is a key business number. With `quantity` missing for 2.8% of products, units sold cannot be trusted for this period until the gap is explained.

The following breakdowns will also be incomplete:
- Revenue by product
- Revenue by product version
- Revenue by product name
- Revenue by category
- Average selling price

The check results do not say whether overall revenue is calculated from item-level `price` and `quantity` or from a separate purchase-level value. If it relies on item-level fields, overall revenue would also be affected. This should not be assumed in either direction until confirmed.

The cause is unknown. The check results do not show whether the gap affects all dates evenly or is concentrated on particular days.

## Suggested next steps
- Get the count of affected products and the count of purchases that contain at least one affected product. The check results only give percentages.
- Find out whether the same products are missing all five fields or whether the gaps fall on different products.
- Break the missing values down by day to see whether they are spread across Nov 1, 2020 – Jan 31, 2021 or grouped on specific dates.
- Confirm how units sold and overall revenue are calculated. In particular, check whether either depends on item-level `quantity` and `price`, so the full reach of this gap is known.
- Look at the affected purchases for anything they share that could help locate where the values are being dropped.

## Acceptance criteria
- `item_id`, `item_name`, `item_category`, `price` and `quantity` each have coverage of at least 0.99 on `purchase` events, and the check no longer flags them.
- The number of affected products and purchases for Nov 1, 2020 – Jan 31, 2021 is documented.
- Any report of units sold, or revenue by product, version, name or category, that covers this period notes the gap until it is resolved.