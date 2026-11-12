# `select_item` fired 436.7 times as often as `view_item_list`, the event it requires

**Event:** select_item (requires view_item_list)
**Found by:** · **Date found:** · **Severity:** Medium

## Description
An item can only be selected from a product list after that list has been shown. Every `select_item` event should therefore follow a `view_item_list` event, and `select_item` should not fire more often than `view_item_list`.

The event dependency check flagged this pair because the opposite happened. Over the checked period, `select_item` fired 31007 times and `view_item_list` fired only 71 times, so `select_item` fired 436.7 times as often as the event it requires.

The check results do not show which event is wrong. Possible explanations, none of them confirmed, are:
- `view_item_list` is not firing on some or most lists.
- `select_item` is firing in places that are not product lists.
- Both of the above are happening.

## Evidence
- `select_item`: 31007 events over the checked period.
- `view_item_list`: 71 events over the checked period.
- Ratio: `select_item` fired 436.7 times as often as `view_item_list`.
- The start and end dates of the checked period are missing from the check results.
- No daily, page-level or list-level breakdown was provided, so it is not known whether the problem affects the whole period or only part of it.

## Impact
According to the tracking plan, these events feed the following reporting:
- `select_item`: product list click-through rate and item selection reporting.
- `view_item_list`: product list views and the list-to-product funnel step.

**Product list click-through rate and the list-to-product funnel step cannot be trusted.** The data shows far more selections than list views, which is not possible in real use. At least one of the two counts must be wrong.

**Product list views and item selection reporting are also unreliable.** We cannot yet tell which of the two counts is correct, so neither can be relied on until this is resolved.

**Severity is Medium.** The affected reporting is a secondary set of list and funnel metrics. The check results do not show that revenue, orders, units sold or an overall conversion rate depend on these events. If the list-to-product funnel step feeds an overall conversion rate, severity should be raised to High. That dependency has not been confirmed.

## Suggested next steps
- Confirm the dates of the checked period.
- Break both events down by day to see whether the gap is constant or starts on a particular date.
- Confirm where `view_item_list` is meant to fire, and check whether it fires on every product list that allows item selection.
- Check where `select_item` is firing, and whether any of those places are not product lists.
- Find out which team uses product list click-through rate and the list-to-product funnel step. Tell them these figures are unreliable until this is resolved.

## Acceptance criteria
- Over any checked period, `select_item` does not fire more often than `view_item_list`.
- `view_item_list` fires on every product list from which an item can be selected.
- `select_item` fires only when an item is selected from a product list.
- Product list click-through rate and the list-to-product funnel step are not used for any period affected by this problem. The affected dates should be documented once they are known.