# 2.4788% of products in begin_checkout are missing item details from Nov 1 2020 to Jan 31 2021

**Event:** begin_checkout
**Found by:** · **Date found:** · **Severity:** Medium

## Description
An automated check found that five item fields on the `begin_checkout` event are missing for 2.4788% of products between Nov 1, 2020 and Jan 31, 2021. The check flags a required field when coverage falls below 0.99. All five fields have a coverage rate of 0.975212, which is 1.4788 percentage points short of that threshold.

These fields are stored in the `items` list of the event, so coverage is measured per product, not per event. When they are missing, those products cannot be identified, grouped, priced or counted in checkout reporting.

All five fields have the same coverage rate, but the check results do not show whether the same products are missing all five. Matching rates do not prove a shared cause.

## Evidence (Nov 1, 2020 – Jan 31, 2021)
- Check: required field coverage. Threshold: 0.99.
- Share of products missing each field: 2.4788%. Gap to threshold: 1.4788 percentage points.
- Flagged fields, all with coverage rate 0.975212:
  - `item_id` (in `items`, per product). Used in the checkout funnel by exact product version, such as colour or size.
  - `item_name` (in `items`, per product). Used in the checkout funnel by product name, grouping all versions.
  - `item_category` (in `items`, per product). Used in the checkout funnel by category.
  - `price` (in `items`, per product). Used in the value of carts entering checkout.
  - `quantity` (in `items`, per product). Used in units entering checkout.
- **Not in the check results:**
  - The number of products or events affected.
  - A breakdown by day, so it is unknown whether the gap is spread across the period or concentrated on certain dates.
  - Whether the same products are missing all five fields.
  - Whether other events, such as `purchase`, show the same gap.

## Impact
- **Product, name and category breakdowns:** The checkout funnel split by product version, product name or category will undercount products at the checkout step. Conversion by product or category may look lower than it is for the affected products.
- **Cart value entering checkout:** This total will be understated for any product missing `price`.
- **Units entering checkout:** This total will be understated for any product missing `quantity`.

The size of these effects for any single product or category is unknown, because the check results only give the overall share.

**Why Medium:** The affected uses are breakdowns of the checkout funnel and checkout-stage totals (cart value and units entering checkout). None of the listed uses is revenue, orders, units sold or overall conversion. The check covers only `begin_checkout`, so it does not show whether those key numbers are affected. Severity should be reviewed if the same gap is found on `purchase`, or if checkout cart value or units are used as key business numbers.

## Suggested next steps
- Count the products and `begin_checkout` events affected, and break the gap down by day to see whether it is constant or limited to certain dates.
- Check whether the same products are missing all five fields, or whether each field is missing on different products.
- Look for anything the affected products have in common, such as the product type, the page or platform where checkout started, or the app or site version.
- Check whether `purchase` and other ecommerce events have the same gap for these fields over the same period.

## Acceptance criteria
- `item_id`, `item_name`, `item_category`, `price` and `quantity` each reach coverage of at least 0.99 on `begin_checkout`, with the goal of every product in `items` carrying all five fields.
- Checkout funnel reports by product, name or category, and checkout cart value and units, state the period they cover. Until the gap is resolved, they also note that some products in Nov 1, 2020 – Jan 31, 2021 are missing these fields.