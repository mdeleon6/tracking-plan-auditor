# 2.4788% of products in `begin_checkout` events are missing `item_id`, `item_name`, `item_category`, `price` and `quantity`

**Event:** begin_checkout
**Found by:** · **Date found:** · **Severity:** Medium

## Description
`begin_checkout` events record when a user starts checkout. Each event carries a list of the products in the cart, called `items`. The required field coverage check flags a field when its coverage is below 0.99.

Five product-level fields inside `items` are below that threshold: `item_id`, `item_name`, `item_category`, `price` and `quantity`. Each has a coverage rate of 0.975212, which means 2.4788% of products are missing that field.

The check measures coverage per product, not per checkout event. The check results do not show how many checkout events contain at least one affected product.

All five fields have the same coverage rate. This could mean that the same product entries are missing all five fields together, but the check results do not confirm it. The check results also give no cause, and the matching rates do not prove the five gaps share one cause.

## Evidence
- Check: required field coverage, with a threshold of 0.99.
- Event: `begin_checkout`. Fields are in `items` and measured per product.
- `item_id`: coverage_rate 0.975212.
- `item_name`: coverage_rate 0.975212.
- `item_category`: coverage_rate 0.975212.
- `price`: coverage_rate 0.975212.
- `quantity`: coverage_rate 0.975212.
- Share of products missing each field: 2.4788%. Gap to threshold: 1.4788 percentage points.
- The following are not included in the check results:
  - the date range the check covered
  - the number of products or events checked
  - the number of products with missing values
  - a breakdown by day or by any other dimension

## Impact
According to the check results, these fields are used in the following analyses:
- **Checkout funnel by exact product version** (for example colour or size), which uses `item_id`. Products without an ID cannot be assigned to a version.
- **Checkout funnel by product name** (all versions grouped), which uses `item_name`.
- **Checkout funnel by category**, which uses `item_category`.
- **Value of carts entering checkout**, which uses `price`. Products without a price cannot add value to this total.
- **Units entering checkout**, which uses `quantity`. Products without a quantity cannot add units to this total.

Any of these analyses that includes affected products may show incomplete or unassigned results. The size of the effect on each analysis cannot be stated, because the check results do not include counts.

**Why Medium:** The affected uses are product, name and category breakdowns of the checkout funnel, plus checkout-stage totals: cart value entering checkout and units entering checkout. None of the uses listed in the check results are revenue, orders, units sold or overall conversion rates. The check results do not show whether any of those key numbers draw on these `begin_checkout` fields. If one does, this rating should be raised to High.

## Suggested next steps
- Find out the date range the check covered, and whether the missing values are spread across that period or concentrated on particular days.
- Check whether the same product entries are missing all five fields, or whether different products are missing different fields.
- Look for anything the affected product entries have in common, such as specific products, categories, platforms or app versions.
- Confirm whether any revenue, order, units-sold or conversion-rate reporting uses `item_id`, `item_name`, `item_category`, `price` or `quantity` from `begin_checkout`. Adjust the severity if it does.
- Check whether products sent in other ecommerce events are missing these same fields.

## Acceptance criteria
- `item_id`, `item_name`, `item_category`, `price` and `quantity` each have a coverage rate of at least 0.99 in `begin_checkout` on the required field coverage check.
- The cause of the missing values is identified and documented, along with the period affected.
- Teams using the product, name or category checkout funnels, or the cart value and units entering checkout, are told about the period with incomplete product data.