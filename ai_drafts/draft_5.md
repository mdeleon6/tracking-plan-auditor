# 2.7995% of products in purchases are missing item_id, item_name, item_category, price and quantity (date range not provided)

**Event:** purchase
**Found by:** · **Date found:** · **Severity:** High

## Description
An automated required field coverage check flagged five product-level fields on the `purchase` event. Each product listed in a purchase should carry `item_id`, `item_name`, `item_category`, `price` and `quantity`. These fields sit in the `items` list of the event and are measured per product.

All five fields have the same coverage rate of 0.972005, so each is missing for 2.7995% of products. The check flags a field when coverage falls below 0.99, and these fields are 1.7995 percentage points short of that threshold.

The check results do not show whether the same products are missing all five fields. The matching rate could suggest one shared pattern, but that is unconfirmed. The fields could also be missing on different products that happen to add up to the same share.

## Evidence (date range not provided in the check results)
- Check: required field coverage, threshold 0.99.
- `item_id`: coverage_rate 0.972005.
- `item_name`: coverage_rate 0.972005.
- `item_category`: coverage_rate 0.972005.
- `price`: coverage_rate 0.972005.
- `quantity`: coverage_rate 0.972005.
- Share missing for each field: 2.7995%. Gap to threshold: 1.7995 percentage points.
- The check results do not include the following:
  - the date range checked
  - the number of products or purchase events checked
  - the number of products missing each field
  - a breakdown by day
  - any overlap between the fields

## Impact
According to the check results, `quantity` is used for units sold and `price` is used for revenue by product and average selling price. Units sold is a key business number. With `quantity` missing for 2.7995% of products, units sold cannot be fully trusted. This is why the severity is High.

The other fields affect breakdowns:
- Revenue and units by exact product version depend on `item_id`.
- Revenue and units by product name depend on `item_name`.
- Revenue by category depends on `item_category`.

Products missing these fields cannot be placed correctly in those breakdowns.

The check results do not say whether total revenue is calculated from item-level `price` and `quantity` or from a separate event-level value. Whether total revenue is affected is therefore unknown.

## Suggested next steps
- Find out the date range the check covered, and how many products and purchase events are affected. Break the missing rate down by day to see whether it is spread out or concentrated.
- Confirm whether the same products are missing all five fields, or whether different products are missing different fields.
- Look at a sample of the affected products to see what else they carry. For example, check whether these are full product entries with missing details or largely empty entries in the `items` list.
- Confirm how total revenue and units sold are calculated, so the effect on reported figures can be measured.
- Correct any reports that show units sold or product, category or price breakdowns for the affected period, or add a caveat to them.

## Acceptance criteria
- `item_id`, `item_name`, `item_category`, `price` and `quantity` each have coverage of at least 0.99 on `purchase` events, and the check no longer flags them.
- The cause of the missing values is identified and recorded, along with whether the same products were missing all five fields.
- The date range and the number of affected products are documented, so that any analysis of units sold or product-level revenue can exclude or adjust for them.