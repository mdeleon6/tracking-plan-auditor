# 84.9% of `transaction_id` values on purchases arrived as a number instead of a string from Nov 1 to Nov 12, 2020

**Event:** purchase
**Found by:** · **Date found:** · **Severity:** High

## Description
The tracking plan says the `purchase` event's `transaction_id` field (in `event_params`) should always arrive as a string. From Nov 1 to Nov 12, 2020, 456 of 537 values arrived as a number. The check found both types only on Nov 11 and Nov 12, 2020. It found no number-type values on any other day in the period.

`transaction_id` is used for order counts, for removing duplicate purchases, and for matching orders to the order system. These uses depend on the ID being stored and compared consistently. The check results do not say why the type changed.

## Evidence (Nov 1, 2020 – Jan 31, 2021)
- The automated field data type check flags a field when any value arrives as a different type than the tracking plan sets.
- Expected type: string. Type received on the flagged days: number.
- Nov 1–12, 2020: 456 of 537 `transaction_id` values (84.9%) arrived as a number.
- Nov 11, 2020: 35 of 63 values arrived as a number. Both types arrived that day.
- Nov 12, 2020: 1 of 54 values arrived as a number. Both types arrived that day.
- The check results do not give daily counts for Nov 1–10, 2020.
- The check results list no number-type values from Nov 13, 2020 to Jan 31, 2021. This only describes the type of the values received. It does not show that those values are complete or correct.
- The check results do not show whether every purchase had a `transaction_id`, so 537 should be read as values received, not as total purchases.

## Impact
Order counts depend on `transaction_id`, which makes this High. Order counts are a key business number, and they cannot be trusted for Nov 1–12, 2020 until it is confirmed how the number-type values are handled. The check results do not show any of these effects directly, so each one is a risk to confirm rather than a known result:
- **Duplicate removal:** the same purchase may be sent more than once, with one copy as a string and another as a number. In that case, duplicate removal may not recognise the copies as the same order, and they could be counted twice.
- **Order system matching:** joins to the order system may fail or behave differently when one side is a number and the other a string. This could leave orders from Nov 1–12 unmatched.
- **Information loss:** the check results do not show whether any ID content was lost when sent as a number, for example leading zeros or very long IDs.

The change from number to string appears to happen across Nov 11 and Nov 12, 2020. That timing could possibly reflect a tracking change, but this is unconfirmed. The check results do not state a cause.

## Suggested next steps
- Confirm with the owners of the `purchase` tracking whether a change to how `transaction_id` is sent was made around Nov 11–12, 2020.
- For Nov 1–12, 2020, compare a sample of the number-type `transaction_id` values against the order system. Confirm they match exactly and that no characters, such as leading zeros, were lost.
- Check how the current duplicate-removal and order-matching logic treats number-type IDs. Confirm whether the same order arriving as both a string and a number would be counted once or twice, especially for Nov 11 and Nov 12, 2020.
- Get the daily counts for Nov 1–10, 2020, which are missing from the check results, to see how the 456 number-type values are spread across those days.

## Acceptance criteria
- 100% of `purchase` events send `transaction_id` as a string, as set in the tracking plan.
- The Nov 1–12, 2020 values are either corrected to strings or handled with a documented conversion. Duplicate removal and order-system matching for those days are confirmed to give the same results as for string values.
- The field data type check shows no number-type `transaction_id` values for the period once it is re-run.