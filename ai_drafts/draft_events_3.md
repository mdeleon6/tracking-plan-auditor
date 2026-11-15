# remove_from_cart has 0 rows from Nov 1, 2020 to Jan 31, 2021

**Event:** remove_from_cart
**Found by:** · **Date found:** · **Severity:** Low

## Description
The tracking plan lists `remove_from_cart` as an active event, but the data has no rows for it between Nov 1, 2020 and Jan 31, 2021. The automated planned-events check flagged it. This check flags any event that the tracking plan marks as active but that never appears in the data.

The check results do not say why there are no rows. This ticket does not assume whether the event is not being sent or whether no cart removals happened. Either is possible, and neither has been confirmed.

## Evidence (Nov 1, 2020 – Jan 31, 2021)
- Rows received for `remove_from_cart` in the whole period: 0.
- Source: the automated planned-events check.
- The check results do not include:
  - when `remove_from_cart` was added to the tracking plan
  - whether it was expected to be active for the whole period
  - whether rows exist for any dates outside this period

## Impact
According to the tracking plan, `remove_from_cart` is used in cart removal reporting. With no rows received in this period, that reporting has no data to show for Nov 1, 2020 to Jan 31, 2021.

The check results do not say whether any key business number, such as revenue, orders, units sold or conversion rates, uses this event. They also do not say whether anyone makes decisions from cart removal reporting.

**Severity:** Low, as set by the tracking plan. That rating fits if cart removal reporting is not used for decisions. If teams do act on it, the problem would be closer to Medium. In that case one type of reporting would be empty, but based on the check results no key business number depends on it. The plan owner should confirm which applies (see next steps).

## Suggested next steps
- Confirm with the owner of the tracking plan whether `remove_from_cart` has been built and released, and from what date it was expected to send data.
- Check whether the site or app sends `remove_from_cart` when an item is removed from the cart, for example by removing an item in a test session and seeing whether an event is recorded.
- Ask the owners of cart removal reporting whether anyone uses it, and whether it showed empty or unexpected results for this period.
- Ask the tracking plan owner to review the Low rating once it is known whether cart removal reporting is used for decisions.

## Acceptance criteria
- Either `remove_from_cart` rows appear in the data when items are removed from the cart, or the tracking plan is updated so it no longer lists the event as active.
- Cart removal reporting notes that there is no `remove_from_cart` data for Nov 1, 2020 to Jan 31, 2021, unless that data is later recovered.