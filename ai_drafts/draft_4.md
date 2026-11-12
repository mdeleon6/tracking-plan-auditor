# 7.9058% of purchase events are missing `transaction_id`, `value`, `purchase_revenue`, `tax` and `payment_type`

**Event:** purchase
**Found by:** · **Date found:** · **Severity:** High

## Description
An automated check on required fields flagged five fields on the `purchase` event. Each field has a coverage rate of 0.920942, below the check's threshold of 0.99. For each field, 7.9058% of purchase events are missing it.

The flagged fields are used for order counts, revenue, average order value, tax reporting and payment type breakdowns.

The check results do not include the date range checked, the number of purchase events or a breakdown by day. They also do not show whether the same purchase events are missing all five fields. All five fields have the same coverage rate, but that does not show that the same events are affected. Whether the gaps share a cause is not confirmed.

## Evidence (date range not provided in the check results)
- Check: required field coverage. A field is flagged when coverage is below 0.99.
- Coverage rate for each flagged field: 0.920942.
- Share of purchase events missing each field: 7.9058%.
- Gap to threshold: 6.9058 percentage points.
- Flagged fields:
  - `transaction_id`: in `event_params`, measured per event. Used for order counts, removing duplicate purchases and matching orders to the order system.
  - `value`: in `event_params`, measured per event. Used for revenue and average order value.
  - `purchase_revenue`: in `ecommerce`, measured per event. Used for revenue and average order value.
  - `tax`: in `event_params`, measured per event. Used for revenue before and after tax.
  - `payment_type`: in `event_params`, measured per event. Used for orders and revenue by payment type.
- Missing from the check results:
  - the date range
  - total and affected event counts
  - a daily or other breakdown
  - how the missing fields overlap across events

## Impact
This is High because key business numbers depend on these fields:
- **Revenue and average order value** come from `value` and `purchase_revenue`. Both are missing on 7.9058% of purchase events, so revenue and average order value built from these fields cannot be trusted until the gap is explained.
- **Order counts** depend on `transaction_id`. Without it, the affected purchases cannot be deduplicated or matched to the order system. Order counts may therefore be over- or under-stated, depending on how those purchases are handled.
- **Revenue before and after tax** depends on `tax`.
- **Orders and revenue by payment type** depend on `payment_type`.

The check results only show which values were received. They do not show whether these purchases happened as recorded or what their correct values would be. Purchase events that do contain these fields are not confirmed to be complete or correct either.

## Suggested next steps
- Get the date range the check covered, plus the total number of purchase events and the number of affected events.
- Find out whether the same purchase events are missing all five fields, or whether different events are missing different fields.
- Break the missing values down by day to see whether the gap is spread across the period or limited to certain dates.
- For purchases that do have a `transaction_id`, compare them against the order system. For purchases missing it, find out whether any other field can link them to orders.
- Look for anything the affected purchase events have in common.

## Acceptance criteria
- When the required field coverage check is run again, `transaction_id`, `value`, `purchase_revenue`, `tax` and `payment_type` each have a coverage rate at or above 0.99 on `purchase` events.
- The date range and the number of affected purchase events are documented.
- Any revenue, order count, average order value, tax or payment type reporting for the affected period carries a note about the missing fields until the gap is resolved or explained.