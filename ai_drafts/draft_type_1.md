# `transaction_id` on purchase arrived as a number instead of a string for 456 of 537 values, Nov 1–12, 2020

**Event:** purchase
**Found by:** · **Date found:** · **Severity:** High

## Description
The tracking plan sets the `purchase` event's `transaction_id` field (in `event_params`) as a string. Between Nov 1 and Nov 12, 2020, 456 of 537 `transaction_id` values arrived as a number. On Nov 11 and Nov 12, 2020, purchases arrived with both types. The check found no number values on any day after Nov 12, 2020, through Jan 31, 2021.

This field is used for order counts, removing duplicate purchases and matching orders to the order system. Any of these steps may give wrong results for Nov 1–12 if it does not handle both types the same way.

## Evidence (Nov 1, 2020 – Jan 31, 2021)
- Check: field data type. A field is flagged when any value arrives as a different type than the tracking plan sets.
- Expected type: string. Received type for some values: number.
- Nov 1–12, 2020: 456 of 537 values (84.9%) arrived as a number.
- Nov 11, 2020: both types arrived. 35 of 63 values arrived as a number.
- Nov 12, 2020: both types arrived. 1 of 54 values arrived as a number.
- Nov 13, 2020 – Jan 31, 2021: the check found no values of the wrong type.
- The check results do not give a breakdown by day for Nov 1–10, 2020. They also do not give the total number of `transaction_id` values for the full period.
- The check results do not show whether the number values match order IDs in the order system. They also do not show whether any digits or formatting were lost.

## Impact
`transaction_id` is used for order counts, for removing duplicate purchases and for matching orders to the order system. Orders are a key business number, so this is rated **High**.

The check results do not confirm that any of these numbers is wrong. They do show a real risk for Nov 1–12, 2020, if any downstream step treats a number ID and a string ID as different values:
- Order counts could be off.
- Duplicate purchases might not be removed.
- Orders might fail to match the order system.

Until this is confirmed, order counts and order matching for Nov 1–12, 2020 should not be relied on. A possible, unconfirmed explanation is a change in how the field was sent around Nov 11–12, 2020, since that is when both types appear. The check results do not confirm any cause.

## Suggested next steps
- Find out whether order counts, duplicate removal and order matching convert `transaction_id` to a single type before use. If they do not, measure how many Nov 1–12, 2020 purchases were counted, kept as duplicates or left unmatched because of the type difference.
- Compare a sample of the number values from Nov 1–12, 2020 with the order system. Check that they match existing order IDs exactly, with no lost digits, leading characters or formatting.
- Check whether the same order appears more than once on Nov 11–12, 2020, once with a number ID and once with a string ID.
- Ask the owners of the purchase tracking whether anything changed in how `transaction_id` was sent on or around Nov 11–12, 2020.
- Get the missing figures: the breakdown by day for Nov 1–10, 2020, and the total `transaction_id` count for the full period.

## Acceptance criteria
- Every `transaction_id` value on the `purchase` event arrives as a string, as the tracking plan sets.
- For Nov 1–12, 2020, the number values are either converted to strings that match the order system, or the affected purchases are flagged in reporting.
- Order counts, duplicate removal and order matching for Nov 1–12, 2020 are re-checked after the fix, and the results are recorded on this ticket.