# 450 purchase events are missing `transaction_id`, `value`, `purchase_revenue`, `tax` and `payment_type` from Nov 1 2020 to Jan 31 2021

**Event:** purchase
**Found by:** · **Date found:** · **Severity:** High

## Description
The automated required-field coverage check flagged five fields on the `purchase` event: `transaction_id`, `value`, `purchase_revenue`, `tax` and `payment_type`. Each field has a coverage rate of 0.920942, which means 7.9058% of purchase events are missing it. The check flags a field when coverage is below 0.99, so these fields are 6.9058 percentage points short of the threshold.

The gaps fall on the same events. Each of the five fields is missing on 450 records, and every pair of these fields is missing together on 450 records. So the same 450 purchase events lack all five fields. All 450 of these events also lack `shipping_tier`, which is missing on 1533 records in total.

Most of the gap is on a few days. On Dec 30, 2020, Jan 17, 2021 and Jan 26–31, 2021, coverage was more than 10 percentage points below the typical daily coverage of 96.3%. Jan 26–31, 2021 had the lowest coverage, at 17.7%.

The cause is not known. The check results do not show why these fields are absent.

## Evidence (Nov 1, 2020 – Jan 31, 2021)
- **Overall coverage:** `transaction_id`, `value`, `tax` and `payment_type` (in event_params) and `purchase_revenue` (in ecommerce) each have a coverage rate of 0.920942. That means 7.9058% of events are missing each field, 6.9058 percentage points below the 0.99 threshold. Coverage is measured per event.
- **Records missing each field:**
  - `transaction_id`: 450
  - `value`: 450
  - `purchase_revenue`: 450
  - `tax`: 450
  - `payment_type`: 450
  - `shipping_tier`: 1533
- **Overlap between fields:** Every pair of the five flagged fields is missing together on 450 records. Each of the five fields is also missing together with `shipping_tier` on 450 records.
- **Days with coverage more than 10 percentage points below the typical daily coverage of 96.3%** (applies to all five flagged fields):
  - Dec 30, 2020: 22 of 37 (59.5%)
  - Jan 17, 2021: 12 of 14 (85.7%)
  - Jan 26–31, 2021: 50 of 282 (17.7%)
  - Together, these days account for 249 missing records.
- **Information the check results do not include:**
  - The total number of purchase events in the period.
  - The number of missing records on each listed day.
  - How the missing records are spread across the other days.

## Impact
These five fields feed key business numbers, according to the check results:
- **`transaction_id`:** order counts, removing duplicate purchases, and matching orders to the order system.
- **`value` and `purchase_revenue`:** revenue and average order value.
- **`tax`:** revenue before and after tax.
- **`payment_type`:** orders and revenue by payment type.

For the 450 affected events, revenue cannot be counted from `value` or `purchase_revenue`. These events also cannot be deduplicated or matched to the order system, because they have no `transaction_id`. Revenue, order counts and average order value for the period therefore cannot be trusted. This is why the severity is High.

The problem is worst on Jan 26–31, 2021, where coverage was 17.7%. Any reporting on that period is most affected.

Having rows on other days does not show that the data on those days is complete. Totals for those days should not be treated as correct based on this check alone.

The check results do not confirm whether the 450 events are real purchases that lost their fields or events that should not count as purchases. Both are possible and unconfirmed. The answer decides whether revenue and orders are undercounted or whether these events should be excluded.

## Suggested next steps
- **Size the problem:** Get the total number of purchase events in the period and the number of missing records on each day. These numbers are not in the check results.
- **Check against the order system:** For Dec 30, 2020, Jan 17, 2021 and Jan 26–31, 2021, compare against the order system. This shows whether orders exist that correspond to the purchase events missing these fields.
- **Look for a pattern:** Review the other fields on the 450 affected events to see whether they share anything that would explain why all five fields are absent together.
- **Find out how the fields are sent:** Confirm with the people who own the purchase tracking how and when these fields are sent. Check whether any tracking changes were made around the listed dates.

## Acceptance criteria
- `transaction_id`, `value`, `purchase_revenue`, `tax` and `payment_type` each have coverage of at least 0.99 on `purchase` events for Nov 1, 2020 to Jan 31, 2021. The check should be re-run to confirm this.
- No day in the period has coverage for these fields more than 10 percentage points below their typical daily coverage.
- If the 450 events cannot be fixed, there is a documented decision on how revenue, order and average order value reporting handles them. This should cover Jan 26–31, 2021 in particular.