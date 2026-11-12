# 7.9058% of purchases are missing transaction_id, value, purchase_revenue, tax and payment_type

**Event:** purchase
**Found by:** · **Date found:** · **Severity:** High

## Description
The required field coverage check flags a field on the `purchase` event when coverage falls below 0.99. Five fields on `purchase` were flagged, and each has a coverage rate of 0.920942. That means 7.9058% of purchase events are missing each of these fields, which is 6.9058 percentage points short of the threshold:

- `transaction_id` (event_params)
- `value` (event_params)
- `purchase_revenue` (ecommerce)
- `tax` (event_params)
- `payment_type` (event_params)

Each field is measured per event.

The check results report 450 missing records for `transaction_id`, `value`, `tax` and `payment_type`. Every pair of these four fields overlaps on 450 records. This shows the same 450 records are missing all four fields. Shared timing alone does not prove a shared cause, and no cause has been confirmed.

`purchase_revenue` has the same coverage rate. However, the check results do not report its count of missing records or its overlap with the other fields. It cannot be confirmed that it is missing on the same 450 records.

The check results also report `shipping_tier` as missing on 1533 records. Those 1533 records include all 450 records above. The check results do not list `shipping_tier` among the flagged fields and do not give its coverage rate.

## Evidence
- Check: required field coverage. The flag threshold is coverage below 0.99.
- Coverage rate for all five flagged fields: 0.920942.
- Share missing for each flagged field: 7.9058%. Gap to threshold: 6.9058 percentage points.
- Missing record counts:
  - `transaction_id`: 450
  - `value`: 450
  - `tax`: 450
  - `payment_type`: 450
  - `shipping_tier`: 1533
- Overlaps:
  - Every pair among `transaction_id`, `value`, `tax` and `payment_type` overlaps on 450 records.
  - Each of those four fields overlaps with `shipping_tier` on 450 records.
- Not in the check results:
  - The date range checked.
  - The total number of purchase events.
  - The missing record count for `purchase_revenue`.
  - Any overlap between `purchase_revenue` and the other fields.

## Impact
Key business numbers depend on these fields, so they cannot currently be trusted. This is why the severity is High.

- **Order counts.** `transaction_id` is used for order counts, for removing duplicate purchases, and for matching orders to the order system. The 450 records without it cannot be deduplicated or matched to the order system. It is unknown whether they are real orders, duplicates or something else.
- **Revenue and average order value.** These rely on `value` and `purchase_revenue`, which are both missing on 7.9058% of purchase events.
- **Revenue before and after tax.** These rely on `tax`.
- **Orders and revenue by payment type.** These rely on `payment_type`.

The check results only show what was received. They do not show whether these purchases actually happened or what their amounts were. The purchase events that do have these fields should not be assumed complete or correct either.

## Suggested next steps
- Find out the date range checked and the total number of purchase events. Both are missing from the check results.
- Report the missing count for `purchase_revenue` and its overlap with `transaction_id` and `value`. This will confirm whether it is missing on the same 450 records.
- Look at the 450 records missing `transaction_id`, `value`, `tax` and `payment_type`. Check whether they share anything, such as dates, platform or app version.
- Try to match the 450 records against the order system by other means. This will establish whether they are real orders.
- Review `shipping_tier` separately. It is missing on 1533 records, which is more than the 450, and its coverage rate is not in the check results.

## Acceptance criteria
- `transaction_id`, `value`, `purchase_revenue`, `tax` and `payment_type` each have coverage of at least 0.99 on the `purchase` event when the required field coverage check is rerun.
- The 450 affected records are explained and documented, including whether they should count as orders and as revenue.
- The missing count and overlaps for `purchase_revenue` are reported so it can be compared with the other fields.