# 2.4788% of products in begin_checkout events are missing item_id, item_name, item_category, price and quantity

**Event:** begin_checkout
**Found by:** · **Date found:** · **Severity:** Medium

## Description
An automated required field coverage check flagged five product-level fields on the `begin_checkout` event. These fields sit inside the `items` list and are measured per product. Each of the five has a coverage rate of 0.975212, which is below the check's threshold of 0.99. This means 2.4788% of products in `begin_checkout` events are missing each field.

The flagged fields are `item_id`, `item_name`, `item_category`, `price` and `quantity`. All five have the same coverage rate. However, the check results do not show whether the same products are missing all five fields, so this should not be assumed. The cause has not been confirmed.

The check results do not include a date range, so it is not known which period this applies to or whether the gap is limited to certain days.

## Evidence
- Check: required field coverage. A field is flagged when coverage is below 0.99.
- Coverage rate for each flagged field: 0.975212.
- Share of products missing each field: 2.4788%.
- Gap to threshold: 1.4788 percentage points.
- Flagged fields, all in `items` and measured per product:
  - `item_id`: used in the checkout funnel by exact product version, such as colour or size
  - `item_name`: used in the checkout funnel by product name, grouping all versions
  - `item_category`: used in the checkout funnel by category
  - `price`: used in the value of carts entering checkout
  - `quantity`: used in units entering checkout
- Not included in the check results:
  - the date range checked
  - the number of events or products checked
  - the number of products missing each field
  - whether the missing values overlap across fields
  - any split by day, platform or product

## Impact
The products missing these fields cannot be assigned to a product version, product name or category. As a result, checkout funnel breakdowns by product and category will be incomplete. The value of carts entering checkout and the units entering checkout will also be incomplete, because `price` and `quantity` are missing on some products. Any figures built from these fields should not be treated as complete until the gap is understood.

**Why this is Medium:** The affected numbers are breakdowns of the checkout funnel and secondary totals for checkout value and units. These fields are on `begin_checkout` rather than on a purchase event, so revenue, orders and units sold are not part of this check. The check results also do not show that the overall count of checkout events depends on these product-level fields. If revenue, orders or units sold are found to be built from these `begin_checkout` fields, the severity should be raised to High.

## Suggested next steps
- Find out the date range the check covered. Then check whether the missing values are spread evenly over time or concentrated on particular days.
- Check whether the same products are missing all five fields together, or whether different products are missing different fields.
- Look for anything the affected products have in common, such as platform, app version, page or product type.
- Check whether the affected products appear with these fields filled in on other events, such as a purchase event. This will show whether the gap is limited to `begin_checkout`.

## Acceptance criteria
- `item_id`, `item_name`, `item_category`, `price` and `quantity` each reach a coverage rate of at least 0.99 on `begin_checkout`.
- Any checkout funnel breakdown by product or category, and any checkout value or units figure, notes the affected period and the products missing these fields until the gap is resolved.