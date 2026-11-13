# 7.9% of Purchases missing transaction ids from Nov 1 2020 - Jan 31 2021

**Event:** purchase
**Found by:** Martino DeLeon · **Date found:** 2026-11-04 · **Severity:** High

## Description
7.9% of purchases are showing in the data with no `transaction_id`. One possible cause is purchases that did not complete, but this has not been confirmed. Most of these are concentrated in Jan 26-31. The same 450 purchases are also missing `value`, `tax`, `payment_type` and `purchase_revenue`, so this looks like one gap across several fields rather than five separate ones. The cause is still unconfirmed.

## Evidence (Nov 1, 2020 – Jan 31, 2021)
- 450 of 5,692 purchases (7.9%) have no `transaction_id` in `event_params`.
- Nov 1–17: 2 of 836 missing (0.2%).
- Nov 18–Jan 25: 216 of 4,574 missing (4.7%).
- Jan 26–31: 232 of 282 missing (82.3%). On Jan 31, 0 of 19 purchases had an ID.
- Dec 30, 2020: 15 of 37 missing (22 of 37 had an ID). This day is part of the Nov 18–Jan 25 count. It was found by the automated coverage-by-day check, not the manual audit.
- `ecommerce.transaction_id` is empty through Nov 10, partly filled Nov 11–12, then matches `event_params`.
- The same 450 purchases are missing `transaction_id`, `value`, `tax`, `payment_type` and `purchase_revenue`, and all 450 also lack `shipping_tier` (see finding 003). Confirmed by the automated co-missing check, which counts purchases missing each pair of fields.
- Queries: [`queries/06_purchase_transaction_ids.sql`](../queries/06_purchase_transaction_ids.sql), [`queries/21_purchase_param_keys.sql`](../queries/21_purchase_param_keys.sql)

## Impact
Purchase and revenue numbers cannot be trusted until this is explained. If these orders did not complete, purchase counts are being overstated. If they did complete, they are real sales that cannot be matched to order records or checked for duplicates. Because `value` and `tax` are missing on the same purchases, these orders count toward purchase totals but add nothing to revenue, so average order value is understated.


## Suggested next steps
- Need to confirm when a purchase receives a transaction id. Then find out why these purchases don't have one. If it is because the transaction was not completed then why is the event firing?
- Check whether the Jan 26–31 drop is real. A jump from 4.7% to 82.3% is too sudden to be explained by cancelled orders alone, so look for a tracking change around Jan 26, or a limitation in the sample data.


## Acceptance criteria
- 100% of `purchase` should have a `transaction_id`.
- `purchase` events should only fire for completed orders.
