# 2.7995% of products in purchases are missing item_id, item_name, item_category, price and quantity

**Event:** purchase
**Found by:** · **Date found:** · **Severity:** High

## Description
Some products recorded inside `purchase` events arrive without five required item fields: `item_id`, `item_name`, `item_category`, `price` and `quantity`. These fields sit in the `items` list of each purchase and are measured per product.

A field is flagged when its coverage is below 0.99. All five fields have a coverage rate of 0.972005, so 2.7995% of products are missing each one.

All five fields have the same coverage rate. The check results do not show whether the same products are missing all five fields or whether different products are missing different fields. The cause of the gap is unknown.

## Evidence
- Check: required field coverage on the `purchase` event, with a threshold of 0.99.
- Coverage rate for each flagged field: 0.972005.
- Share missing for each field: 2.7995%.
- Gap to threshold: 1.7995 percentage points.
- Flagged fields, all in `items` and measured per product:
  - `item_id`, used for revenue and units by exact product version, such as colour or size.
  - `item_name`, used for revenue and units by product name, grouping all versions.
  - `item_category`, used for revenue by category.
  - `price`, used for revenue by product and average selling price.
  - `quantity`, used for units sold and revenue by product.
- The check results do not include:
  - the date range checked
  - a breakdown by day
  - the number of products or purchases affected
  - whether the missing values overlap across the five fields.

## Impact
This is **High** because `quantity` is used for units sold, which is a key business number. Products without a `quantity` cannot be counted reliably. Units sold totals that include this period cannot be trusted until the gap is understood.

Revenue by product, by product name and by category, along with average selling price, will be incomplete for the affected products. Products without `item_id`, `item_name` or `item_category` cannot be placed into those breakdowns. Products without `price` cannot contribute to price-based figures.

The check results do not say whether total revenue is calculated from these item fields or from a separate field. Until that is confirmed, do not assume total revenue is unaffected.

## Suggested next steps
- Find out how many products and how many purchases are affected, and over what date range. None of this is in the check results.
- Break the missing values down by day to see whether the gap is spread out or concentrated in a particular period.
- Check whether the products missing one field are the same products missing the other four. That shows whether whole product entries are empty or fields are dropping independently.
- Confirm how total revenue and units sold are calculated, and whether either depends on the item-level fields flagged here.
- Look at the affected purchases for anything they share, such as a platform, app version or checkout path. Treat any pattern found as a lead to investigate, not a confirmed cause.

## Acceptance criteria
- Every product in the `items` list of a `purchase` event has `item_id`, `item_name`, `item_category`, `price` and `quantity` filled in.
- At minimum, each of the five fields has a coverage rate at or above 0.99 when the required field coverage check is re-run.
- The affected date range and the number of affected purchases are documented. Anyone reporting units sold or product-level revenue for that range can then account for the gap.