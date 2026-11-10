# 2.4788% of products in begin_checkout events are missing item_id, item_name, item_category, price and quantity

**Event:** begin_checkout
**Found by:** · **Date found:** · **Severity:** Medium

## Description
An automated check confirms that required fields are filled in. It flags any field filled in for less than 0.99 of records, which is 99%. In the `begin_checkout` event, five product fields inside the `items` list fall below this threshold. Each one is filled in for 0.975212 of products, so 2.4788% of products are missing it. This is 1.4788 percentage points short of the threshold.

The check measures these fields for each product, not each event. A `begin_checkout` event that contains several products is counted once for each product.

All five fields have exactly the same coverage. This could mean the same products are missing all five fields, but that has not been confirmed. The cause is also unknown.

## Evidence (date range not provided)
- Check: required field coverage. Threshold is 0.99.
- Event: `begin_checkout`
- All of these fields are in `items` and measured per product, each with coverage of 0.975212:
  - `item_id`
  - `item_name`
  - `item_category`
  - `price`
  - `quantity`
- Share of products missing each field: 2.4788%.
- Gap to threshold: 1.4788 percentage points.
- **Missing from the input:**
  - The date range checked.
  - The total number of products or events checked.
  - The count of affected products.
  - Whether the same products are missing all five fields.
  - Any daily breakdown showing when the problem started.

## Impact
Product-level checkout analysis is incomplete. About 2.4788% of products in checkouts have no `item_id`, `item_name` or `item_category`. These products cannot be identified or grouped, so they will be left out of reports such as:
- checkouts by product or category
- product drop-off between checkout and purchase

The missing `price` and `quantity` could also lower any checkout value that is calculated from the items. It is not known whether an event-level value field exists or is affected.

The severity is Medium rather than High for two reasons:
- The problem is limited to product breakdowns within `begin_checkout`.
- The input does not show any effect on revenue, orders or overall conversion rates.

The count of `begin_checkout` events should still be correct, because the gaps are in product fields, not in the event itself. This has not been verified. If checkout value or conversion rates are calculated from the item fields, the severity should be reviewed again.

## Suggested next steps
- Get the date range, the total number of products checked and the count of affected products for this check.
- Confirm whether the same products are missing all five fields, or whether different products are missing different fields.
- Break the affected products down by day to find out whether the problem started on a specific date or has always existed.
- Look for anything the affected products have in common, such as:
  - platform or app version
  - product type
  - checkout entry point
- Confirm whether any checkout value or conversion metric is calculated from `price` and `quantity` in `items`.

## Acceptance criteria
- `item_id`, `item_name`, `item_category`, `price` and `quantity` in `begin_checkout` `items` each reach at least 0.99 coverage on this check. The target is for every product to have all five fields.
- Any product analysis that uses these fields records the known gap, or excludes the affected period once the date range has been confirmed.