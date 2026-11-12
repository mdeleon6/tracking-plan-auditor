# 2.7995% of purchased products are missing item_id, item_name, item_category, price and quantity

**Event:** purchase
**Found by:** · **Date found:** · **Severity:** High

## Description
An automated check flags a required field when its coverage is below 0.99. On the `purchase` event, five fields on the products inside each purchase (the `items` list) fell below that level: `item_id`, `item_name`, `item_category`, `price` and `quantity`. Coverage is measured per product, not per purchase.

All five fields have the same coverage of 0.972005, which means 2.7995% of products are missing each field. The check results do not show whether the same products are missing all five fields or whether different products are missing different ones. The matching rates alone do not prove a shared cause.

## Evidence
- Check: required field coverage, threshold 0.99.
- Event: `purchase`. Location: `items`, measured per product.
- `item_id`: coverage 0.972005.
- `item_name`: coverage 0.972005.
- `item_category`: coverage 0.972005.
- `price`: coverage 0.972005.
- `quantity`: coverage 0.972005.
- Share of products missing each field: 2.7995%. Gap to threshold: 1.7995 percentage points.
- Missing from the check results:
  - the date range checked
  - the number of products and purchases checked
  - the number of products missing each field
  - whether the gaps are spread across all dates or concentrated on specific dates

## Impact
The check results list `quantity` as a field used for units sold. Units sold is a key business number, so it cannot be fully trusted while some products have no `quantity`. This is the reason for the High rating.

The other fields affect these numbers, according to the check results:
- `price`: revenue by product and average selling price.
- `item_id`: revenue and units by exact product version, such as colour or size.
- `item_name`: revenue and units by product name.
- `item_category`: revenue by category.

The check results do not say whether total revenue is calculated from these product fields or from a separate field on the purchase. The effect on total revenue is not confirmed either way.

## Suggested next steps
- Find out whether the same products are missing all five fields or whether the gaps fall on different products.
- Get the date range checked and break the missing values down by day. This shows whether the problem started on a specific date or has always been present.
- Confirm whether total revenue and total units sold are built from `price` and `quantity` in `items`. This will show how far key numbers are affected.
- Look for anything the affected products have in common, such as product type or how the purchase was made. No cause has been identified so far.

## Acceptance criteria
- `item_id`, `item_name`, `item_category`, `price` and `quantity` have coverage of at least 0.99 on every product in `purchase` events.
- The affected date range and number of products are documented, so that reports on units sold and product-level revenue can note or correct the affected period.