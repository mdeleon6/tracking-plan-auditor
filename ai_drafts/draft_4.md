# 7.9% of purchases are missing `transaction_id`, `value`, `purchase_revenue`, `tax` and `payment_type` from Nov 1, 2020 to Jan 31, 2021

**Event:** purchase
**Found by:** · **Date found:** · **Severity:** High

## Description
An automated check on required fields flagged five fields on the `purchase` event. Each field is missing on 7.9% of purchase events (coverage 92.1%). The check flags a field when its coverage is below 0.99.

The five fields are:
- `transaction_id`
- `value`
- `purchase_revenue`
- `tax`
- `payment_type`

Each field is missing on 450 records. Every pair of these fields is missing together on 450 records, so the same 450 purchases are missing all five fields at once. All 450 are also missing `shipping_tier`.

Coverage was much lower than usual on three dates or date ranges: Dec 30, 2020, Jan 17, 2021, and Jan 26–31, 2021.

## Evidence (Nov 1, 2020 – Jan 31, 2021)
**Whole period**
- Each flagged field is missing on 7.9% of purchase events (coverage 92.1%). This is 6.9 percentage points short of the check's threshold.
- Each field is measured per event. The check results list where each field is stored:

| Field | Stored in | Used for |
|---|---|---|
| `transaction_id` | event_params | Order counts, removing duplicate purchases, matching orders to the order system |
| `value` | event_params | Revenue, average order value |
| `purchase_revenue` | ecommerce | Revenue, average order value |
| `tax` | event_params | Revenue before and after tax |
| `payment_type` | event_params | Orders and revenue by payment type |

- The check results do not give the total number of purchase events for the period.

**Fields missing together**
- Each of the five fields is missing on 450 records.
- Every pair of the five fields is missing together on 450 records.
- Each of the five fields is also missing together with `shipping_tier` on 450 records.
- `shipping_tier` is missing on 1,533 records in total. Most of those are outside the scope of this ticket.

**Days with unusually low coverage**
The check lists days when coverage was more than 10 percentage points below the fields' typical daily coverage of 96.3%. All five fields show the same figures:
- Dec 30, 2020: 22 of 37 (59.5%)
- Jan 17, 2021: 12 of 14 (85.7%)
- Jan 26–31, 2021: 50 of 282 (17.7%)

The check results report 249 missing records across these flagged days. The check results do not say how the remaining missing records are spread across the other days.

## Impact
Severity is **High** because these fields feed key business numbers: revenue, average order value and order counts.

- **Revenue and average order value.** The 450 purchases have no `value` or `purchase_revenue`, so they add nothing to revenue or average order value. Neither revenue nor average order value can be trusted for the period until these purchases are explained.
- **Order counts.** Without `transaction_id`, these purchases cannot be checked for duplicates or matched to the order system. Order counts may include duplicates or may leave out these purchases, depending on how each report handles a missing `transaction_id`.
- **Tax and payment type.** Revenue before and after tax and the breakdown by payment type are also affected.
- **Recent and daily reporting.** Coverage on Jan 26–31, 2021 was 17.7%, so any reporting on those days is badly affected. Dec 30, 2020 is also heavily affected.

The check results only show what was received. They do not show whether these 450 events are real purchases, duplicates, or something else.

Because all five fields go missing on exactly the same records, one shared cause is possible. This has not been confirmed. Jan 26–31 are the last days of the data period, but the check results do not say whether that is related.

## Suggested next steps
- Confirm whether the 450 events are real purchases. For the flagged days, compare the number of purchase events with the number of orders in the order system.
- Look at the other fields on the 450 events to see what they have in common, compared with purchases that have all five fields.
- Get the missing figures:
  - the total number of purchase events in the period
  - the number of records missing these fields on each day outside the flagged days
- Agree how revenue and order reports should treat these 450 events until the issue is resolved, and note this on any affected reports.
- Track the other `shipping_tier` gaps in a separate ticket. Only 450 of the 1,533 records missing `shipping_tier` are covered here.

## Acceptance criteria
- `transaction_id`, `value`, `purchase_revenue`, `tax` and `payment_type` each meet the check's 0.99 coverage threshold on `purchase` events.
- No day has coverage more than 10 percentage points below the typical daily coverage for any of these fields.
- There is a documented decision on how the 450 existing purchases without these fields are handled in revenue and order reporting.