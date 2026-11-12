# 2.7995% of products in purchases are missing item details (`item_id`, `item_name`, `item_category`, `price`, `quantity`)

**Event:** purchase
**Found by:** · **Date found:** · **Severity:** High

## Description
An automated check confirms that each `purchase` event records five required fields for every product it contains. For each of these fields, 2.7995% of products are missing a value:

- `item_id`
- `item_name`
- `item_category`
- `price`
- `quantity`

All five fields have a coverage rate of 0.972005. The check flags a field when coverage is below 0.99, so each of these fields is 1.7995 percentage points below the threshold.

The five fields have the same coverage rate. This suggests the same products may be missing all five fields, but this is possible and unconfirmed. The check results report each field separately and do not show whether the missing values fall on the same products. They also do not give a cause.

## Evidence
- Check: required field coverage. Threshold: 0.99.
- Coverage rate for `item_id`, `item_name`, `item_category`, `price` and `quantity`: 0.972005.
- Share of products missing each field: 2.7995%.
- Gap to threshold: 1.7995 percentage points.
- All fields sit in `items` and are measured per product.
- **Missing from the check results:**
  - The date range checked.
  - The number of products and `purchase` events checked.
  - The number of products affected.
  - How the missing values are spread across days.

## Impact
This is **High** because `quantity` feeds **units sold**, which is a key business number. Units sold cannot be fully trusted while some products are missing `quantity`.

According to the check results, the missing fields are also used in:
- **`price`:** revenue by product and average selling price.
- **`quantity`:** revenue by product.
- **`item_id`:** revenue and units by exact product version, such as colour or size.
- **`item_name`:** revenue and units by product name, grouping all versions.
- **`item_category`:** revenue by category.

Products missing these fields cannot be placed in these breakdowns, so the breakdowns will be incomplete.

The check results do not say whether total revenue is calculated from item-level `price` and `quantity`. Do not assume total revenue is unaffected until this is confirmed.

## Suggested next steps
- Confirm whether the same products are missing all five fields, or whether different products are missing different fields.
- Get the information the check results do not include:
  - The date range.
  - The number of products and events checked.
  - The number of affected products.
  - A day-by-day view of the missing values.
- Check whether the affected products have anything in common, so the source can be found.
- Confirm whether total revenue is calculated from item-level `price` and `quantity`, or from a separate event-level value.

## Acceptance criteria
- `item_id`, `item_name`, `item_category`, `price` and `quantity` each have a coverage rate of at least 0.99 on `purchase` events, measured per product.
- The date range and the number of affected products are recorded on this ticket.
- Any report of units sold, revenue by product, revenue by category or average selling price for the affected period notes that some products are missing these fields.