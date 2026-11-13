# 36.3545% of add_to_cart events are missing `quantity` from Nov 1 2020 to Jan 31 2021

**Event:** add_to_cart
**Found by:** · **Date found:** · **Severity:** Medium

## Description
The `quantity` field on `add_to_cart` events is often missing. The field sits in the `items` list and is meant to record how many units of the product were added to the cart. The tracking plan expects one product per event, which is the product actually added. An event counts as covered if at least one of its products has `quantity`.

Across Nov 1, 2020 to Jan 31, 2021, coverage of `quantity` was 0.636455. That means 36.3545% of `add_to_cart` events are missing the field. The check flags a field when coverage is below 0.99, so this is 35.3545 percentage points short.

The missing values are not spread evenly over the period. The check results show coverage falling in at least two stages:
- **Late November.** On Nov 27 and Nov 28, 2020, coverage dropped to 88.1% and 88.2%. Before that, the median of the previous 7 days was 99.3%.
- **Early December.** On Dec 9–12, 2020, coverage dropped to between 50.7% and 57.3%. Before that, the median of the previous 7 days was between 83.1% and 88.6%.

The check results do not show the cause of either drop.

## Evidence (Nov 1, 2020 – Jan 31, 2021)
The source for all figures below is the automated required field coverage check.

**Overall**
- `quantity` coverage rate was 0.636455, against a threshold of 0.99.
- 36.3545% of events were missing `quantity`, a gap of 35.3545 percentage points to the threshold.
- The check results do not include the total number of `add_to_cart` events, or the number missing `quantity`, for the full period.

**Flagged days**
A day is flagged when its coverage is more than 10 percentage points below the median of the previous 7 days with data.

| Day | Events with `quantity` | Coverage | Previous 7 days' median | Next day with data |
|---|---|---|---|---|
| Nov 27, 2020 | 1083 of 1229 | 88.1% | 99.3% | 88.2%, still more than 10 points below |
| Nov 28, 2020 | 949 of 1076 | 88.2% | 99.3% | 90.8%, back within 10 points |
| Dec 9, 2020 | 1018 of 1787 | 57.0% | 88.6% | 57.3%, still more than 10 points below |
| Dec 10, 2020 | 997 of 1739 | 57.3% | 88.6% | 50.7%, still more than 10 points below |
| Dec 11, 2020 | 1082 of 2135 | 50.7% | 87.8% | 56.3%, still more than 10 points below |
| Dec 12, 2020 | 777 of 1381 | 56.3% | 83.1% | 58.5%, still more than 10 points below |
| Jan 24, 2021 | 187 of 473 | 39.5% | 54.1% | 51.5%, back within 10 points |

**How to read the flagged days**
- The 7-day median before Nov 27 was 99.3%. The 7-day median before Dec 9 was 88.6%. This suggests coverage did not fully recover to its earlier level between the two drops. However, the check results do not include daily coverage for the days between Nov 29 and Dec 8, so this cannot be confirmed.
- After Dec 12, the next day with data was still more than 10 points below the previous median, but no further days are flagged in December. The check notes that a flagged day can mark where a lasting change starts. Once the lower level becomes the new normal, later days are no longer flagged. The absence of flags after Dec 12 therefore does not show that coverage recovered.
- The 7-day median before Jan 24, 2021 was 54.1%. This suggests coverage was still around the lower December level in late January.
- Daily coverage for days that were not flagged is missing from the check results.

## Impact
The check results list one use for `quantity`: **units added to cart**. Any total of units added to cart for this period will be understated or unreliable.

The effect is likely to be uneven over time. Coverage was near the threshold before Nov 27, but the medians shown from Dec 9 onward are much lower. So a units-added-to-cart trend across the period may show a decline that comes from the tracking gap rather than from customer behaviour. The check results cannot tell us whether customer behaviour changed on these days.

The data cannot tell us what quantity was actually added on events without `quantity`. Days that have events with `quantity` should also not be treated as complete or correct. 1083 of 1229 events covered on Nov 27, for example, still leaves that day incomplete.

**Severity: Medium.** Units added to cart is a secondary total. The check results do not list any key business number, such as revenue, orders, units sold or conversion rates, as depending on this field. Counts of `add_to_cart` events do not need `quantity`. If `quantity` on `add_to_cart` feeds any key business number not listed in the check results, severity should be raised to High.

## Suggested next steps
- **Find out what changed on Nov 27, 2020 and Dec 9, 2020.** Check for site, app or tracking releases on those dates. The check results do not confirm any cause.
- **Get daily coverage for the full period,** including the days that were not flagged. This shows:
  - whether coverage recovered between Nov 29 and Dec 8
  - where coverage settled after Dec 12
  - whether it is still low at Jan 31, 2021
- **Compare events with and without `quantity`** to see what the events without it have in common. For example, compare where they were sent from, or which products were added.
- **Confirm how current units-added-to-cart reports handle events without `quantity`.** For example, are those events dropped, counted as zero, or counted as one? Then flag any reports for this period that may be affected.

## Acceptance criteria
- `quantity` coverage on `add_to_cart` events is at or above 0.99 in the required field coverage check.
- Daily coverage stays at or above 0.99, with no days flagged as more than 10 percentage points below the previous 7-day median.
- Any units-added-to-cart figures for Nov 27, 2020 onward are labelled as affected by missing `quantity` until the field is fixed or the gap is explained.