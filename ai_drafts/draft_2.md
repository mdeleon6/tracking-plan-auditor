# 2.4788% of products in `begin_checkout` events are missing five required item fields

**Event:** begin_checkout
**Found by:** · **Date found:** · **Severity:** Medium

## Description
A required field coverage check flagged five fields on products in `begin_checkout` events: `item_id`, `item_name`, `item_category`, `price` and `quantity`. These fields sit inside `items` and are measured per product. Each field has a coverage rate of 0.975212, which means 2.4788% of products are missing that field. The check flags a field when coverage is below 0.99, so each field is 1.4788 percentage points short of the threshold.

All five fields have exactly the same coverage rate. The check results do not show whether the same products are missing all five fields, or whether different products are missing different fields. A shared cause has not been confirmed.

The check results do not give a date range, a count of affected products or a count of `begin_checkout` events.

## Evidence
- Check: required field coverage. A field is flagged when coverage is below 0.99.
- `items.item_id`: coverage rate 0.975212. Missing on 2.4788% of products.
- `items.item_name`: coverage rate 0.975212. Missing on 2.4788% of products.
- `items.item_category`: coverage rate 0.975212. Missing on 2.4788% of products.
- `items.price`: coverage rate 0.975212. Missing on 2.4788% of products.
- `items.quantity`: coverage rate 0.975212. Missing on 2.4788% of products.
- Gap to threshold for each field: 1.4788 percentage points.
- Date range checked: missing from the check results.
- Number of affected products and events: missing from the check results.

## Impact
Several reports that use these fields will leave out the affected products:
- The checkout funnel by exact product version, such as colour or size, uses `item_id`.
- The checkout funnel by product name uses `item_name`.
- The checkout funnel by category uses `item_category`.
- The value of carts entering checkout uses `price`.
- The units entering checkout use `quantity`.

Products without these fields cannot be placed in any product or category breakdown. They will also not be counted in the cart value and units entering checkout. These totals and breakdowns should be treated as incomplete. It is not known how much they are understated, because the counts of affected products are missing.

This is rated Medium rather than High. The affected uses are product and category breakdowns of the checkout funnel and secondary totals for carts entering checkout. The check results do not list revenue, orders, units sold or overall conversion rates as uses of these fields.

This check only measures fields on products. It does not show whether all `begin_checkout` events were received. Overall checkout counts should not be treated as confirmed complete based on this ticket.

## Suggested next steps
- Confirm the date range the check covered. Find the number of affected products and `begin_checkout` events.
- Check whether the same products are missing all five fields, or whether the gaps fall on different products.
- Look at the affected products for anything they have in common, such as date, platform, product type or page. This would help narrow down where the gap comes from.
- Check whether these products are also missing the same fields in other ecommerce events. This would show whether the gap is limited to `begin_checkout`.

## Acceptance criteria
- `item_id`, `item_name`, `item_category`, `price` and `quantity` each have a coverage rate of at least 0.99 on products in `begin_checkout` events. Ideally every product has all five fields.
- The date range and counts of affected products are recorded on this ticket. This lets anyone using the checkout funnel by product, by category, cart value or units entering checkout know which period to treat as incomplete.