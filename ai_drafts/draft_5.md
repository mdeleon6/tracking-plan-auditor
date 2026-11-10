# 2.7995% of products in purchase events are missing item details (date range not provided)

**Event:** purchase
**Found by:** · **Date found:** · **Severity:** Medium

## Description
An automated check found that some products inside `purchase` events are missing required item details. Five fields in the `items` list (`item_id`, `item_name`, `item_category`, `price` and `quantity`) each have a coverage rate of 0.972005, so 2.7995% of products are missing each field. The check flags any field with coverage below 0.99, so each field falls 1.7995 percentage points short.

This is measured per product, not per purchase event. A single purchase can contain several products, so the number of affected purchase events is not known from this input.

All five fields have the same coverage rate. This suggests the gaps may be on the same products, but the input does not confirm it. It is possible that different products are missing different fields.

## Evidence
- Check: required field coverage, threshold 0.99.
- Event: `purchase`. Location: `items`, measured per product.
- `item_id`: coverage 0.972005
- `item_name`: coverage 0.972005
- `item_category`: coverage 0.972005
- `price`: coverage 0.972005
- `quantity`: coverage 0.972005
- Share missing each field: 2.7995%. Gap to threshold: 1.7995 percentage points.
- The input does not include:
  - The date range checked.
  - The total number of products or purchase events.
  - The count of affected products.
  - A breakdown by day.
  - Whether the same products are missing all five fields.

## Impact
For the affected products there is no way to identify the product (`item_id`, `item_name`), group it (`item_category`), or value it (`price`, `quantity`). Any product-level analysis will undercount by these products. This includes top sellers, category sales, units sold and average item price.

**Severity is Medium.** The gaps are in product-level fields inside the `items` list. The purchase events themselves are still present, so counts of purchases are not affected by this check. Product and category breakdowns are the type of analysis affected.

**Severity should be raised to High if any revenue total is built from item `price` × `quantity`.** In that case, revenue totals would be missing the value of these products. The input does not show whether an event-level revenue field exists, or whether it was checked. This needs to be confirmed.

## Suggested next steps
- Confirm the date range of the check. Get the count of affected products and purchase events.
- Check whether the same products are missing all five fields, or whether the gaps are spread across different products.
- Break down the missing rate by day to see whether this started at a specific point or has been ongoing.
- Look for anything the affected products or purchases have in common, such as platform, app version, product type or page.
- Confirm how revenue is reported. Is it from an event-level field or from item `price` and `quantity`? Use the answer to settle the severity.

## Acceptance criteria
- `item_id`, `item_name`, `item_category`, `price` and `quantity` each have coverage of at least 0.99 in the `items` list of `purchase` events.
- The date range, affected counts and day-by-day breakdown are added to this ticket.
- Severity is confirmed as Medium or raised to High, based on how revenue is reported.