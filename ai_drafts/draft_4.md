# 7.9058% of purchase events are missing transaction_id, value, purchase_revenue, tax and payment_type

**Event:** purchase
**Found by:** · **Date found:** · **Severity:** High

## Description
An automated required-field check flagged five fields on the `purchase` event because their coverage is below the 0.99 threshold. All five fields have a coverage_rate of 0.920942, which means 7.9058% of purchase events are missing each field. That share is 6.9058 percentage points away from the threshold.

The flagged fields are `transaction_id`, `value`, `purchase_revenue`, `tax` and `payment_type`. All five are measured per event.

The five fields have the same coverage rate, but the input does not show whether the same purchase events are missing all of them. A shared rate does not prove a shared cause or the same affected events. The input also does not state the cause.

## Evidence
- Check: required field coverage. A field is flagged when coverage is below 0.99.
- Share of purchase events missing each field: 7.9058%. Gap to threshold: 6.9058 percentage points.
- `transaction_id`: location event_params, measured per event, coverage_rate 0.920942.
- `value`: location event_params, measured per event, coverage_rate 0.920942.
- `purchase_revenue`: location ecommerce, measured per event, coverage_rate 0.920942.
- `tax`: location event_params, measured per event, coverage_rate 0.920942.
- `payment_type`: location event_params, measured per event, coverage_rate 0.920942.
- **Missing from the input:** the date range checked, the total number of purchase events, the number of events missing each field, whether the missing values affect the same events, and any breakdown by day, platform or other dimension.

## Impact
The severity is High because two of the flagged fields, `value` and `purchase_revenue`, carry revenue. Revenue totals built from these fields cannot be trusted while 7.9058% of purchase events lack them. The missing `transaction_id` also affects work that counts or deduplicates orders by transaction ID, so order counts and any conversion rates based on them may also be unreliable. Tax reporting and payment-type breakdowns are affected because `tax` and `payment_type` are also missing at the same rate.

The size of the revenue or order gap in absolute terms cannot be given because the input does not include event counts or revenue amounts.

## Suggested next steps
- Confirm whether the same purchase events are missing all five fields, or whether different events are missing different fields.
- Get the date range and event counts for this check so the number of affected purchases is known.
- Break the missing events down by date to see whether the gap is ongoing, started on a specific date, or is limited to one period.
- Break the missing events down by any available dimension, such as platform or app version, to see whether the gap is concentrated in one place.
- Compare against a source of record for orders or revenue, if one is available, to measure how much revenue and how many orders are missing from tracking.

## Acceptance criteria
- `transaction_id`, `value`, `purchase_revenue`, `tax` and `payment_type` each have coverage at or above 0.99 on the `purchase` event when the required-field coverage check is rerun.
- The affected date range and number of affected events are recorded on this ticket, so that analyses using revenue or order counts can exclude or flag the affected period.