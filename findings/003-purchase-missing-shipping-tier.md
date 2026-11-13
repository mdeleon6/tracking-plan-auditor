# 26.9% of purchases are missing shipping tiers from Nov 1 2020 to Jan 31 2021

**Event:** purchase
**Found by:** Martino DeLeon · **Date found:** 2026-11-06 · **Severity:** Medium

## Description
26.9% of purchases are showing in the data with no `shipping_tier`. No purchases had `shipping_tier` before Nov 20, 2020, which accounts for 988 of the 1,533 missing values. Most of these purchases from Nov 21, 2020 on missing the `shipping_tier` are also missing the `transaction_id`, there are a small amount which have the `transaction_id`.

## Evidence (Nov 1, 2020 – Jan 31, 2021)
- Overall from Nov 1, 2020 - Jan 31, 2021: 1,533 of 5,692 purchases (26.9%) missing `shipping_tier`.
- Nov 1-19, 2020: 100% of 988 purchases missing `shipping_tier`.
- Nov 20, 2020: 62.7% of 118 purchases missing `shipping_tier`. Confirmed by the automated coverage-by-day check (44 of 118 had a tier).
- Nov 21, 2020 - Jan 25, 2021: 5.6% of 4,304 purchases missing `shipping_tier`.
- Dec 30, 2020: 17 of 37 missing (20 of 37 had a tier). This day is part of the Nov 21–Jan 25 count. It was found by the automated coverage-by-day check, not the manual audit. The same day, 15 purchases are missing `transaction_id` (finding 002).
- Jan 26-31, 2021: 82.3% of 282 purchases missing `shipping_tier` and `transaction_id`.
- From Nov 21, 2020 on: 430 purchases are missing both fields, 41 are missing only `shipping_tier`, and none are missing only `transaction_id`.
- Across the whole period, all 450 purchases missing `transaction_id` also lack `shipping_tier`, as well as `value`, `tax` and `payment_type` (see finding 002). No purchase is missing only `transaction_id`. Confirmed by the automated co-missing check.
- Query: [`queries/08_shipping_tier_by_day.sql`](../queries/08_shipping_tier_by_day.sql)
- Query: [`queries/09_shipping_and_transaction_overlap.sql`](../queries/09_shipping_and_transaction_overlap.sql)
- Query: [`queries/21_purchase_param_keys.sql`](../queries/21_purchase_param_keys.sql) (automated checks)

## Impact
Shipping comparisons across the full period will be misleading. `shipping_tier` was not sent before Nov 20, 2020, so shipping choices will appear to start on that date, when that is only when tracking began.

Through experience, teams often count only purchases with a `transaction_id`. Under that rule, the 430 purchases missing both fields from Nov 21, 2020 on would already be excluded, including the 232 from Jan 26–31. Those late January purchases may also be a timing issue, as a `transaction_id` can be added once a transaction is confirmed, which can take up to 7 days. This may not apply to this dataset and has not been confirmed.

Total revenue does not depend on `shipping_tier`, which is why this is Medium rather than High. Any revenue split by shipping tier will still be incomplete, because almost all purchases from before Nov 20 have a `transaction_id` but no tier.

## Suggested next steps
- Need to confirm when `shipping_tier` was implemented into the event. Was it a planned launch on Nov 20, 2020 or was it a bug that was fixed?
- Check and confirm whether `transaction_id` and `shipping_tier` get filled in after a purchase is confirmed. If there is a re-pull done for Jan 26-31, check and confirm the values appear in the data.
- Check the 41 purchases for what they have in common since they have a `transaction_id` but no `shipping_tier`.

## Acceptance criteria
- 100% of `purchase` events have a `shipping_tier`. Purchases that do not ship send a clear value, such as `not_shipped`, instead of leaving the field empty.
- Any analysis using `shipping_tier` starts from Nov 21, 2020, because the field was not sent before Nov 20 and only partly sent on Nov 20.