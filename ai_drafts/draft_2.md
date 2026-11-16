# 2.5% of products in `begin_checkout` are missing five item fields from Nov 1, 2020 to Jan 31, 2021

**Event:** begin_checkout
**Found by:** · **Date found:** · **Severity:** Medium

## Description
When a user starts checkout, the `begin_checkout` event records each product in the cart under `items`. The required field coverage check flags a field when its coverage is below 0.99. Between Nov 1, 2020 and Jan 31, 2021, five fields recorded for each product all had coverage of 97.5%, meaning 2.5% of products were missing each field. That is 1.5 percentage points short of the threshold.

The affected fields are `item_id`, `item_name`, `item_category`, `price` and `quantity`. All five have the same coverage, but the check results do not show whether the same products are missing all five fields. It is possible that one shared problem affects the same product records, but this is unconfirmed.

## Evidence (Nov 1, 2020 – Jan 31, 2021)
- Check: required field coverage on `begin_checkout`. A field is flagged when coverage is below 0.99.
- Coverage for each flagged field is 97.5%, and 2.5% of products are missing each field. The gap to the threshold is 1.5 percentage points.
- All five fields are stored in `items` and measured per product:
  - `item_id`: used in the checkout funnel by exact product version, such as colour or size.
  - `item_name`: used in the checkout funnel by product name, grouping all versions.
  - `item_category`: used in the checkout funnel by category.
  - `price`: used in the value of carts entering checkout.
  - `quantity`: used in the units entering checkout.
- The check results do not include the following:
  - The number of products or events affected.
  - A day-by-day breakdown, so it is not known whether the gap is spread across the period or concentrated on certain dates.
  - Whether the missing values fall on the same products.

## Impact
For about 2.5% of products entering checkout, the product, product version and category are unknown. These products cannot be placed correctly in the checkout funnel by product version, product name or category. Cart value and units entering checkout will also be understated for any product missing `price` or `quantity`. The size of that shortfall cannot be stated, because the check results do not give counts or values.

This is rated Medium because the affected numbers are a set of breakdowns and secondary totals:
- The checkout funnel by product version, product name and category are breakdowns.
- The value of carts entering checkout and the units entering checkout are secondary totals. They are not revenue or units sold.

The fields are recorded per product, so the overall count of checkouts started does not depend on them. However, this check does not show whether that count is complete.

## Suggested next steps
- Get the number of affected products and events for each field, so the size of the gap is known in absolute terms.
- Break coverage down by day for each field to see whether the gap is steady or limited to specific dates.
- Check whether the products missing one field are the same ones missing the other four. Find out what those products have in common, such as the product type, the platform or the page where checkout began.
- Confirm whether the same products have these fields in other events where products are recorded. This will show whether the gap is specific to `begin_checkout`.

## Acceptance criteria
- `item_id`, `item_name`, `item_category`, `price` and `quantity` each have coverage of at least 0.99 on `begin_checkout`. Ideally every product sent in `items` has all five fields.
- Until the gap is fixed or explained, checkout funnel breakdowns by product and category, cart value entering checkout, and units entering checkout for Nov 1, 2020 to Jan 31, 2021 are reported with a note that some products lack these fields.