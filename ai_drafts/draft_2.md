# 2.4788% of products in `begin_checkout` events are missing `item_id`, `item_name`, `item_category`, `price` and `quantity`

**Event:** begin_checkout
**Found by:** · **Date found:** · **Severity:** Medium

## Description
The required field coverage check flagged five product-level fields on the `begin_checkout` event. These fields sit inside the `items` list and are measured per product. Each has a coverage rate of 0.975212, below the check's threshold of 0.99, so 2.4788% of products have no value for these fields.

All five fields show the same coverage rate. This could mean the same products are missing all five fields. One possibility, which has not been confirmed, is that some products are sent with no details at all. However, the check results do not show which products are missing which fields, so this needs to be verified.

The check results do not include the time period checked, the number of events or products, or any daily breakdown. It is not known whether the gap is spread evenly over time or concentrated in certain days.

## Evidence
- Check: required field coverage. A field is flagged when its coverage is below 0.99.
- `item_id` (items, per product): coverage rate 0.975212.
- `item_name` (items, per product): coverage rate 0.975212.
- `item_category` (items, per product): coverage rate 0.975212.
- `price` (items, per product): coverage rate 0.975212.
- `quantity` (items, per product): coverage rate 0.975212.
- Share of products missing each field: 2.4788%. Gap to threshold: 1.4788 percentage points.
- Missing from the check results: the date range, event and product counts, how many products are missing more than one field, and results by day.

## Impact
According to the check results, these fields feed the following reporting:
- **`item_id`:** checkout funnel by exact product version, such as colour or size.
- **`item_name`:** checkout funnel by product name, grouping all versions.
- **`item_category`:** checkout funnel by category.
- **`price`:** value of carts entering checkout.
- **`quantity`:** units entering checkout.

The affected products cannot be placed in any product, version or category breakdown of the checkout funnel. They will also add nothing to cart value or units at the checkout step. These figures will therefore be understated by an amount that cannot be stated, because the counts are missing.

**Why Medium:** The affected uses are secondary totals and breakdowns of the checkout step: cart value entering checkout, units entering checkout, and the funnel split by product, version and category. None of the listed uses is revenue, orders, units sold or an overall conversion rate.

The check measures fields within products, not the number of `begin_checkout` events. The check results therefore neither show that overall checkout counts are affected nor confirm that they are complete. If any key metric, such as an overall checkout conversion rate, is found to depend on these fields, the severity should be raised to High.

## Suggested next steps
- Find out the time period the check covered and the number of events and products involved.
- Check whether the same products are missing all five fields, or whether different products are missing different fields.
- Break the missing values down by day to see whether the gap started on a specific date or appears throughout.
- Look for anything the affected events or products have in common, such as platform, app version or page.
- Run the same coverage check on the `items` fields of related events, such as `view_item`, `add_to_cart` and `purchase`, to see whether the gap is limited to `begin_checkout`.

## Acceptance criteria
- `item_id`, `item_name`, `item_category`, `price` and `quantity` each have a coverage rate of at least 0.99 on `begin_checkout`.
- The period affected is identified. Checkout funnel reporting by product, version or category, as well as cart value and units entering checkout, is labelled as incomplete for that period until the data is fixed.