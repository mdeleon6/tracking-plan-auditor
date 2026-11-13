# select_item fired 436.7 times as often as view_item_list, the event it requires

**Event:** select_item (requires view_item_list)
**Found by:** · **Date found:** · **Severity:** Medium

## Description
An automated event dependency check flagged `select_item` and `view_item_list`. The check flags a pair when an event fires more often over the period than the event it requires.

`select_item` requires `view_item_list` because an item can only be selected from a list that was shown. Each `select_item` should therefore follow a `view_item_list`, and `select_item` should not outnumber `view_item_list`. Over the checked period, `select_item` fired 31007 times and `view_item_list` fired 71 times.

The check results do not show which of the two events is wrong. `view_item_list` may be undercounted, `select_item` may be overcounted, or both. The cause has not been confirmed.

## Evidence
- `select_item`: 31007 events over the period.
- `view_item_list`: 71 events over the period.
- `select_item` fired 436.7 times as often as `view_item_list`.
- **Missing:** The check results do not include the dates of the checked period or any daily breakdown. It is not known whether this affects the whole period or only part of it.

## Impact
The tracking plan lists these uses for the two events:
- `select_item`: product list click-through rate and item selection reporting.
- `view_item_list`: product list views and the list-to-product funnel step.

None of these numbers can be trusted until the problem is explained:
- Product list views and product list click-through rate are unreliable, because the counts behind them contradict each other.
- The list-to-product funnel step is unreliable for the same reason.
- Item selection reporting may also be affected if `select_item` is overcounted.

**Why Medium:** The affected reporting covers product list metrics and one funnel step. According to the tracking plan, none of these is a key business number such as revenue, orders, units sold or an overall conversion rate. This does not show that key numbers are complete or correct, only that the tracking plan does not link them to these events. If the list-to-product funnel step feeds an overall conversion rate, the severity should be raised to High.

## Suggested next steps
- Get the dates of the checked period and daily counts for both events. This will show whether `view_item_list` stopped firing, was never sent, or fired at a low level throughout.
- Check whether `view_item_list` is sent on every page or screen that shows a product list.
- Check whether `select_item` fires more than once per selection, or fires from places that are not product lists. Both are possible explanations and have not been confirmed.
- Confirm whether the list-to-product funnel step or product list click-through rate feeds any overall conversion rate, and adjust severity if so.

## Acceptance criteria
- Over any checked period, `select_item` fires no more often than `view_item_list`, and the event dependency check no longer flags this pair.
- The checked period and daily counts for both events are recorded on this ticket.
- Product list click-through rate, product list views and the list-to-product funnel step are marked as unreliable for any dates where the problem is found.