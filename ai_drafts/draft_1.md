# 36.4% of `add_to_cart` events are missing `quantity` from Nov 1, 2020 to Jan 31, 2021

**Event:** add_to_cart
**Found by:** · **Date found:** · **Severity:** Medium

## Description
The required field coverage check flagged `quantity` on the `add_to_cart` event. From Nov 1, 2020 to Jan 31, 2021, 36.4% of `add_to_cart` events do not have `quantity`, so coverage is 63.6%. The check flags any field with coverage below 0.99, and `quantity` is 35.4 percentage points short of that threshold.

`quantity` sits on the products (`items`) in each event. The tracking plan expects one product per event, which is the product actually added to the cart. An event counts as covered if at least one of its products has `quantity`.

Coverage appears to have dropped in steps rather than all at once. The check flagged three periods:
- **Nov 27–28, 2020:** coverage fell to about 88%. Before these days, coverage had been at 99.3%.
- **Dec 9–12, 2020:** coverage fell to between 50.7% and 58.5%. Before these days, coverage had been between 83.1% and 88.6%.
- **Jan 24, 2021:** coverage fell to 39.5%. Before this day, coverage had been at 54.1%.

The "before" figures are the median of the previous 7 days with data. That median was 99.3% before Nov 27 and 54.1% before Jan 24.

## Evidence (Nov 1, 2020 – Jan 31, 2021)
- **Overall:** 63.6% coverage for `quantity` on `add_to_cart`, with 36.4% missing. That is 35.4 percentage points below the 0.99 threshold. The check results do not include the total number of events or the number missing `quantity` for the full period.
- **How days are flagged:** a day is flagged when its coverage is more than 10 percentage points below the median of the previous 7 days with data. Once a lower level becomes normal, later days at that level are no longer flagged.
- **Nov 27, 2020:** 1083 of 1229 events had `quantity` (88.1%).
  - Previous 7 days' median: 99.3%.
  - Next day with data: 88.2%, still more than 10 points below the previous median.
- **Nov 28, 2020:** 949 of 1076 had `quantity` (88.2%).
  - Previous 7 days' median: 99.3%.
  - Next day with data: 90.8%, back within 10 points of the previous median.
- **Dec 9, 2020:** 1018 of 1787 had `quantity` (57.0%).
  - Previous 7 days' median: 88.6%.
  - Next day with data: 57.3%, still more than 10 points below.
- **Dec 10, 2020:** 997 of 1739 had `quantity` (57.3%).
  - Previous 7 days' median: 88.6%.
  - Next day with data: 50.7%, still more than 10 points below.
- **Dec 11, 2020:** 1082 of 2135 had `quantity` (50.7%).
  - Previous 7 days' median: 87.8%.
  - Next day with data: 56.3%, still more than 10 points below.
- **Dec 12, 2020:** 777 of 1381 had `quantity` (56.3%).
  - Previous 7 days' median: 83.1%.
  - Next day with data: 58.5%, still more than 10 points below.
- **Jan 24, 2021:** 187 of 473 had `quantity` (39.5%).
  - Previous 7 days' median: 54.1%.
  - Next day with data: 51.5%, back within 10 points.
- **Not in the check results:** daily coverage for days that were not flagged, including the days after Dec 12, 2020. Because of how days are flagged, coverage may have stayed at a lower level after Dec 12 without being flagged. The check results do not confirm this either way.
- **Source:** automated required field coverage check.

## Impact
According to the check results, `quantity` is used for **units added to cart**. That number cannot be trusted for this period. Events without `quantity` cannot be counted correctly toward units, and there is no basis in the check results for assuming a default value such as 1.

Comparisons over time will also be misleading. Units added to cart could appear to fall around Nov 27, Dec 9 and Jan 24 because coverage dropped on those days. The check results do not show whether actual cart behavior changed.

Severity is **Medium** for these reasons:
- Units added to cart is a secondary total. It is not revenue, orders, units sold or a conversion rate.
- The check results only list units added to cart as depending on this field.
- The check results only cover `add_to_cart`. They do not show whether other events, such as purchases, are complete.

If `add_to_cart` `quantity` feeds any key business number, this rating should be raised to High.

## Suggested next steps
- **Confirm which metrics use the field.** Check whether `add_to_cart` `quantity` feeds any key business number beyond units added to cart. If it does, raise the severity to High.
- **Get the missing figures.** Pull daily coverage of `quantity` for the full period, especially after Dec 12, 2020 and after Jan 24, 2021. This will show whether coverage stayed low. Also get the total event count and the number of events missing `quantity` for the period.
- **Look for changes on the drop dates.** Check whether any releases or tracking changes happened on or just before Nov 27, 2020, Dec 9, 2020 and Jan 24, 2021. A change on those dates is a possible explanation only and has not been confirmed.
- **Look for a pattern in the affected events.** Compare `add_to_cart` events with and without `quantity` to see whether the missing events share something in common, such as the same source or implementation.
- **Check the products sent per event.** Confirm whether events send one product, as the tracking plan expects. If some events send more than one product, check whether `quantity` is missing only on some of them.

## Acceptance criteria
- `quantity` coverage on `add_to_cart` is at or above 0.99 for the full period, and no days are flagged by the daily coverage check.
- Every `add_to_cart` event sends `quantity` on the product that was added to the cart.
- Until the gap is fixed or explained, any reporting of units added to cart for Nov 1, 2020 to Jan 31, 2021 notes that `quantity` coverage was incomplete.