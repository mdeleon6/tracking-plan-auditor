# 7.9% of Purchases missing transaction ids from Nov 1 2020 - Jan 31 2021

**Event:** purchase
**Found by:** Martino DeLeon · **Date found:** 2026-11-04 · **Severity:** High

## Description
7.9% of purchases are showing in the data with no `transaction_id`. One possible cause is purchases that did not complete, but this has not been confirmed. Most of these are concentrated in Jan 26-31.

## Evidence (Nov 1, 2020 – Jan 31, 2021)
- 450 of 5,692 purchases (7.9%) have no `transaction_id` in `event_params`.
- Nov 1–17: 2 of 836 missing (0.2%).
- Nov 18–Jan 25: 216 of 4,574 missing (4.7%).
- Jan 26–31: 232 of 282 missing (82.3%). On Jan 31, 0 of 19 purchases had an ID.
- `ecommerce.transaction_id` is empty through Nov 10, partly filled Nov 11–12, then matches `event_params`.
- Query: [`queries/06_purchase_transaction_ids.sql`](../queries/06_purchase_transaction_ids.sql)

## Impact
Purchase and revenue numbers cannot be trusted until this is explained. If these orders did not complete, purchases and revenue are being overstated. If they did complete, they are real sales that cannot be matched to order records or checked for duplicates.


## Suggested next steps
- Need to confirm when a purchase receives a transaction id. Then find out why these purchases don't have one. If it is because the transaction was not completed then why is the event firing?
- Check whether the Jan 26–31 drop is real. A jump from 4.7% to 82.3% is too sudden to be explained by cancelled orders alone, so look for a tracking change around Jan 26, or a limitation in the sample data.


## Acceptance criteria
- 100% of `purchase` should have a `transaction_id`.
-`purchase` events should only fire for completed orders.
