# 2.7995% of purchase products are missing item_id, item_name, item_category, price and quantity from Nov 1 2020 to Jan 31 2021

**Event:** purchase
**Found by:** · **Date found:** · **Severity:** High

## Description
Each purchase event holds a list of the products bought, called `items`. Five product fields inside `items` fall below the required coverage threshold of 0.99: `item_id`, `item_name`, `item_category`, `price` and `quantity`. Coverage is measured per product, and all five fields have the same coverage rate, 0.972005. This means 2.7995% of products in purchases are missing each field.

All five fields have the same rate, but the check results do not show whether the same products are missing all five. That has not been confirmed.

## Evidence (Nov 1, 2020 – Jan 31, 2021)
- Check: required field coverage. A field is flagged when coverage is below 0.99.
- `items.item_id`: coverage_rate 0.972005, 2.7995% missing, 1.7995 percentage points below the threshold.
- `items.item_name`: coverage_rate 0.972005, 2.7995% missing, 1.7995 percentage points below the threshold.
- `items.item_category`: coverage_rate 0.972005, 2.7995% missing, 1.7995 percentage points below the threshold.
- `items.price`: coverage_rate 0.972005, 2.7995% missing, 1.7995 percentage points below the threshold.
- `items.quantity`: coverage_rate 0.972005, 2.7995% missing, 1.7995 percentage points below the threshold.
- The check results do not include:
  - the number of products or purchases affected,
  - a breakdown by day,
  - whether the missing values sit on the same products.

## Impact
The check results list these uses for the flagged fields:
- **`quantity`:** units sold and revenue by product.
- **`price`:** revenue by product and average selling price.
- **`item_id`:** revenue and units by exact product version, such as colour or size.
- **`item_name`:** revenue and units by product name, grouping all versions.
- **`item_category`:** revenue by category.

The severity is High because `quantity` is used for units sold, which is a key business number. Units sold cannot be trusted while `quantity` is missing for 2.7995% of products. Every product-level breakdown is also affected:
- revenue and units by product version,
- revenue and units by product name,
- revenue by category,
- average selling price.

The check results do not say whether total revenue or order counts come from these product fields. Do not treat those totals as unaffected until this is confirmed.

The cause is unknown. It is not known whether the products were sent without these fields or the fields were lost later. It is also not known whether the gap is spread across the whole period or limited to certain dates.

## Suggested next steps
- Find out whether the same products are missing all five fields, or whether different products are missing different fields.
- Break the missing values down by day to see whether the gap covers the whole period or is limited to certain dates.
- Get the number of affected products and the number of purchases that contain them. These counts are missing from the check results.
- Confirm whether total revenue and order counts are calculated from `items` or from purchase-level fields, to decide which reports need correcting.
- Check whether the affected purchases have anything in common, for example how or where the purchase was made.

## Acceptance criteria
- `item_id`, `item_name`, `item_category`, `price` and `quantity` each reach a coverage rate of at least 0.99 in the required field coverage check for purchase products.
- Units sold and product-level revenue reports state whether they include products missing these fields, until the gap is fixed.