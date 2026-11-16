# `select_item` fired 436.7 times as often as `view_item_list`, the event it requires

**Event:** select_item (requires view_item_list)
**Found by:** · **Date found:** · **Severity:** Medium

## Description
An automated event dependency check flagged `select_item`. According to the check results, `select_item` requires `view_item_list`, because an item can only be selected from a list that was shown. So `select_item` should not fire more often than `view_item_list`.

Over the checked period, `select_item` fired 31007 times and `view_item_list` fired 71 times. That means `select_item` fired 436.7 times as often as the event it depends on.

The check results do not show which event is wrong. Two explanations are possible, and neither is confirmed:
- `view_item_list` may not be sent when lists are shown.
- `select_item` may be sent in cases that do not involve a list being shown.

Both could also be true at once.

## Evidence
- Check: event dependencies. A pair is flagged when an event fires more often over the period than the event it requires.
- `select_item`: 31007 events.
- `view_item_list`: 71 events.
- `select_item` fired 436.7 times as often as `view_item_list`.
- **Missing:** the check results do not give the start and end dates of the period.
- **Missing:** the check results do not include any daily, page-level or list-level breakdown.

## Impact
According to the tracking plan, these metrics use the two events:
- **`select_item`:** product list click-through rate and item selection reporting.
- **`view_item_list`:** product list views and the list-to-product funnel step.

Product list click-through rate cannot be trusted. It compares item selections with list views, and these two counts do not agree with each other. Product list views and the list-to-product funnel step cannot be trusted either. Item selection reporting may also be affected if `select_item` is over-firing.

Severity is Medium because the affected metrics are product list and list funnel metrics. The tracking plan does not list any key business number as using these events. That includes revenue, orders, units sold and overall conversion rate. This does not prove those numbers are correct. If any key business number is found to use either event, this ticket should be raised to High.

## Suggested next steps
- Confirm the date range the check covered.
- Break both event counts down by day to see whether the gap is present throughout the period or starts at a specific point.
- Check whether `view_item_list` is set up to send on every page and placement that shows a list of items.
- Check where `select_item` is being sent from, and whether any of those places do not show a list of items.
- Ask the tracking plan owner to confirm whether any metric beyond those listed in the tracking plan uses either event.

## Acceptance criteria
- For any period checked, `select_item` does not fire more often than `view_item_list`, and the event dependency check no longer flags this pair.
- The cause of the gap is identified and recorded on this ticket. The ticket states which event was wrong, or whether both were.
- Product list click-through rate and the list-to-product funnel step are marked as unreliable for the affected period until the fix is confirmed.