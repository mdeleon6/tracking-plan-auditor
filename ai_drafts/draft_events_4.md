# view_cart is listed as active in the tracking plan but has 0 rows from Nov 1, 2020 to Jan 31, 2021

**Event:** view_cart
**Found by:** · **Date found:** · **Severity:** Medium

## Description
The tracking plan lists `view_cart` as an active event, but the check results show no rows for it at any point from Nov 1, 2020 to Jan 31, 2021. According to the tracking plan, the checkout funnel uses this event.

The check results do not say why the event is absent. Having no rows does not show whether people viewed their carts during this period. It only shows that no `view_cart` data was received. The check results do not confirm whether the event was ever implemented, was sent under another name, or stopped being sent before the period began.

## Evidence (Nov 1, 2020 – Jan 31, 2021)
- Rows received for `view_cart` across the whole period: 0.
- The automated planned events check flagged this event. That check flags any event that the tracking plan lists as active but that never appears in the data.
- Tracking plan status for `view_cart`: active.
- Tracking plan usage for `view_cart`: checkout funnel.

## Impact
The checkout funnel cannot be reported as planned for this period, because one of its listed events has no data. Any step in the funnel that relies on `view_cart`, and any step-to-step rate that starts or ends at that step, will be missing or misleading.

The tracking plan sets the severity to Medium. The check results do not say whether any key business number depends on `view_cart`, such as an overall checkout conversion rate that is calculated through this step. If no key number depends on it, the effect is limited to one type of breakdown, which fits Medium. If a reported conversion rate is calculated through this step, the problem could be more serious than the plan's rating suggests. That is why one of the next steps below asks for a review.

## Suggested next steps
- Ask the tracking plan owner to confirm whether `view_cart` was meant to be live during Nov 1, 2020 – Jan 31, 2021, and if so, from what date.
- Check whether cart views are being recorded under a different event name. This is one possible explanation, but it is unconfirmed.
- Find out how the checkout funnel currently handles the missing `view_cart` step, and whether any reported conversion rate is calculated through it.
- Ask the tracking plan owner to review the Medium rating in light of the checkout funnel usage, especially if a key conversion rate depends on this step.

## Acceptance criteria
- Either `view_cart` rows are received in the data while the event is listed as active, or the tracking plan is updated so that `view_cart` is no longer listed as active.
- The checkout funnel documentation states which dates have no `view_cart` data, so that nobody reads the missing step as zero cart views.