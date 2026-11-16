# `view_cart` has 0 rows from Nov 1, 2020 to Jan 31, 2021, although the tracking plan lists it as active

**Event:** view_cart
**Found by:** · **Date found:** · **Severity:** Medium

## Description
The tracking plan lists `view_cart` as an active event, but the check results show 0 rows for it in the data from Nov 1, 2020 to Jan 31, 2021. According to the tracking plan, the checkout funnel uses this event.

The check results show only what was received. They do not show whether people viewed their carts during this period, and they do not show why no rows arrived.

## Evidence (Nov 1, 2020 – Jan 31, 2021)
- Check: planned events. This check flags any event that the tracking plan lists as active but that never appears in the data.
- Rows received for `view_cart` in the whole period: 0.
- Where the event is used, according to the tracking plan: checkout funnel.
- Severity set by the tracking plan: Medium.
- The check results do not include any information about other events, other dates or other data sources.

## Impact
The checkout funnel cannot show the `view_cart` step for this period. Any funnel step that relies on `view_cart`, such as movement into or out of the cart view, has no data to report.

The tracking plan sets the severity to Medium, and this ticket keeps that rating. The check results do not show whether any key business number depends on `view_cart`, such as orders, revenue or overall conversion. If the checkout funnel only counts users who pass through every step in order, the missing step could also affect funnel conversion figures. The check results do not confirm how the funnel is built.

Possible explanations include the following. None of them is confirmed by the check results:
- The event was never built.
- The event is sent under a different name.
- The tracking plan lists the event as active when it is not in use.

## Suggested next steps
- Ask the tracking plan owner whether `view_cart` was expected to be live at any point between Nov 1, 2020 and Jan 31, 2021, and since what date.
- Check whether the site or app sends a cart-view event under another name. If it does, decide whether to rename that event or update the tracking plan.
- Find out how the checkout funnel is defined and whether it requires `view_cart` for users to count in later steps.
- If the funnel does require `view_cart`, ask the tracking plan owner to review the Medium rating, because funnel conversion figures may then be affected.
- Review any checkout funnel reports covering Nov 1, 2020 to Jan 31, 2021 and note that they have no `view_cart` data.

## Acceptance criteria
- One of these is true:
  - `view_cart` rows appear in the data and the planned events check no longer flags the event.
  - The tracking plan is updated to show that `view_cart` is not active, and the checkout funnel no longer depends on it.
- The checkout funnel definition states how this period is handled, given that no `view_cart` rows were received from Nov 1, 2020 to Jan 31, 2021.