# 7.9058% of purchase events are missing five required fields, including revenue and transaction ID

**Event:** purchase
**Found by:** · **Date found:** · **Severity:** High

## Description
An automated required field coverage check flagged five fields on the `purchase` event. A field fails the check when its coverage is below 0.99. All five fields have a coverage rate of 0.920942, which means 7.9058% of purchase events are missing each field. This is 6.9058 percentage points short of the threshold.

The five fields have the same coverage rate. This does not prove that the same purchase events are missing all five fields, and it does not prove that the gaps share one cause. The check results do not give a cause.

## Evidence
- Check: required field coverage on `purchase`. A field is flagged when coverage is below 0.99.
- Coverage rate for each flagged field: 0.920942.
- Share of purchase events missing each field: 7.9058%.
- Gap to threshold: 6.9058 percentage points.
- Flagged fields, all measured per event:
  - `transaction_id` (`event_params`): used in order counts, removing duplicate purchases, and matching orders to the order system.
  - `value` (`event_params`): used in revenue and average order value.
  - `purchase_revenue` (`ecommerce`): used in revenue and average order value.
  - `tax` (`event_params`): used in revenue before and after tax.
  - `payment_type` (`event_params`): used in orders and revenue by payment type.
- The check results do not include the following information:
  - The date range the check covered.
  - The total number of purchase events and the number missing each field.
  - A breakdown by day, platform or any other dimension.
  - Whether the missing values fall on the same events.

## Impact
The severity is **High** because the affected fields feed key business numbers:
- **Revenue and average order value:** These depend on `value` and `purchase_revenue`. Both fields are missing on 7.9058% of purchase events, so revenue totals and average order value from this data cannot be trusted.
- **Order counts and duplicate removal:** These depend on `transaction_id`. Purchases without it may not be deduplicated or counted correctly. They also cannot be matched to the order system, so reconciling with that system will be harder.
- **Revenue before and after tax:** This depends on `tax`. It is affected for the same share of events.
- **Orders and revenue by payment type:** This depends on `payment_type`. The breakdown will be incomplete.

The check results do not show how much revenue or how many orders are affected. The size of the effect on totals is therefore unknown.

## Suggested next steps
- Find out which period the check covered and how many purchase events it measured.
- Check whether the missing values for all five fields fall on the same purchase events or on different ones.
- Break the events with missing fields down by date and by any available dimensions, such as platform or app version. This would show whether the gap is ongoing, limited to a certain time, or limited to certain traffic.
- Before any cause is assumed, confirm with the owners of the purchase tracking whether these fields are expected on every purchase event.

## Acceptance criteria
- `transaction_id`, `value`, `purchase_revenue`, `tax` and `payment_type` each reach a coverage rate of at least 0.99 on the `purchase` event when the required field coverage check is rerun.
- The affected period and the overlap between the five missing fields are documented. Any revenue, order or payment type analysis that covers that period can then account for the gap.