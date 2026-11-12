# 7.9058% of purchase events are missing transaction_id, value, purchase_revenue, tax and payment_type

**Event:** purchase
**Found by:** · **Date found:** · **Severity:** High

## Description
An automated check confirms that each `purchase` event includes the fields needed for order and revenue reporting. It flags a field when fewer than 0.99 of events have it. Five fields were flagged, each with a coverage rate of 0.920942, so 7.9058% of purchase events are missing each one. That is 6.9058 percentage points below the threshold.

Four of the fields (`transaction_id`, `value`, `tax` and `payment_type`) are each missing on 450 records, and these are the same 450 records. All 450 are also missing `shipping_tier`, which is missing on 1533 records in total. `purchase_revenue` has the same coverage rate as the other four fields, but the check results do not say how many records are missing it or whether they are the same 450 records.

Coverage for `transaction_id`, `value`, `tax` and `payment_type` dropped sharply on Dec 30, 2020, Jan 17, 2021 and Jan 26–31, 2021. Jan 26–31 had the lowest coverage. The cause has not been confirmed. Several fields going missing on the same records and days does not by itself prove that they share a cause.

## Evidence
The overall period covered by the check and the total number of purchase events are not in the check results.

- Coverage for each flagged field: 0.920942. Threshold: 0.99. Gap: 6.9058 percentage points.
- Share of events missing each flagged field: 7.9058%.
- Flagged fields and where they are stored:
  - `transaction_id`: event_params, measured per event.
  - `value`: event_params, measured per event.
  - `purchase_revenue`: ecommerce, measured per event.
  - `tax`: event_params, measured per event.
  - `payment_type`: event_params, measured per event.
- `transaction_id`, `value`, `tax` and `payment_type` are each missing on 450 records. Every pair of these fields is missing together on 450 records.
- 450 records are missing `shipping_tier` together with each of those four fields. `shipping_tier` is missing on 1533 records in total.
- Missing counts and overlaps for `purchase_revenue` are not in the check results.
- Days with coverage more than 10 percentage points below typical, for `payment_type`, `tax`, `transaction_id` and `value` (typical daily coverage 96.3%):
  - Dec 30, 2020: 22 of 37 (59.5%).
  - Jan 17, 2021: 12 of 14 (85.7%).
  - Jan 26–31, 2021: 50 of 282 (17.7%).
- These flagged days account for 249 missing records. The check results do not give dates for the remaining missing records.

## Impact
This is High severity because the missing fields feed key business numbers:
- **Revenue and average order value** come from `value` and `purchase_revenue`. Revenue reporting cannot be trusted while these fields are missing on 7.9058% of purchase events.
- **Order counts, removing duplicate purchases and matching orders to the order system** depend on `transaction_id`. Without it, these 450 records cannot be matched to orders. They also cannot be confirmed as unique purchases or as duplicates.
- **Revenue before and after tax** depends on `tax`.
- **Orders and revenue by payment type** depend on `payment_type`.

Reports covering Jan 26–31, 2021 are the most affected, because coverage on those days was 17.7%. Days that were not flagged should not be assumed complete. The check results only show what was received.

## Suggested next steps
- Confirm the full date range of the check and the total number of purchase events in it.
- Get the missing count for `purchase_revenue` and check whether those records are the same 450 records missing the other four fields.
- Find out whether the 450 records correspond to real orders in the order system. Without `transaction_id`, they cannot be matched by that field.
- Investigate Dec 30, 2020, Jan 17, 2021 and Jan 26–31, 2021 to find out what changed on those days. Record the cause once it is confirmed.
- Find the dates of the missing records that fall outside the flagged days.
- Find out why `shipping_tier` is missing on 1533 records, more than the 450 missing the other fields. It was not one of the flagged fields in this check.
- Decide how revenue, order and payment-type reports should handle the affected records until the gap is fixed, and tell report users.

## Acceptance criteria
- `transaction_id`, `value`, `purchase_revenue`, `tax` and `payment_type` each have coverage of at least 0.99 on `purchase` events.
- No day has coverage more than 10 percentage points below a field's typical daily coverage for these fields.
- The missing count and overlap for `purchase_revenue` are reported alongside the other fields.
- Reports using revenue, order counts, tax or payment type for Dec 30, 2020, Jan 17, 2021 and Jan 26–31, 2021 are corrected or clearly marked as affected.