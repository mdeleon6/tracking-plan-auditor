# add_to_wishlist has 0 rows from Nov 1, 2020 to Jan 31, 2021, though the tracking plan lists it as active

**Event:** add_to_wishlist
**Found by:** · **Date found:** · **Severity:** Medium

## Description
The tracking plan lists `add_to_wishlist` as an active event, but no rows for it were received at any point between Nov 1, 2020 and Jan 31, 2021. The automated planned events check flagged it. This check flags any event that the tracking plan lists as active but that never appears in the data.

The check results only show that no rows arrived. They do not show whether users added items to a wishlist during this period. The cause is not confirmed. Possible causes include:
- The event was never sent.
- The event was sent under a different name.
- The wishlist feature was not in use during the period.

## Evidence (Nov 1, 2020 – Jan 31, 2021)
- Check: planned events. It flags events that are listed as active in the tracking plan but never appear in the data.
- Rows received for `add_to_wishlist` in the whole period: 0.
- Tracking plan status: active.
- Used in, according to the tracking plan: wishlist reporting.
- The check results do not include:
  - when `add_to_wishlist` was added to the tracking plan
  - whether the event has ever been received outside this period
  - any row counts for other wishlist-related events

## Impact
Wishlist reporting has no `add_to_wishlist` data for Nov 1, 2020 to Jan 31, 2021. Any wishlist report covering this period cannot show how often items were added to wishlists. A zero or empty result in that report should not be read as users not using the wishlist, because the check results cannot show whether that activity happened.

The severity is Medium, set by the tracking plan. This rating fits the check results. The tracking plan lists only wishlist reporting as using this event, which is a secondary type of reporting. The check results do not show any key business number, such as revenue, orders, units sold or conversion rates, depending on `add_to_wishlist`.

## Suggested next steps
- Ask the tracking plan owner to confirm that `add_to_wishlist` was expected to be live for the full period from Nov 1, 2020 to Jan 31, 2021. Also ask when it was first marked as active.
- Confirm whether the wishlist feature was available to users during this period.
- Check whether the site or app code sends `add_to_wishlist`, and whether it uses exactly that event name.
- Check whether wishlist activity is arriving under a different event name.
- Confirm who uses wishlist reporting and whether any other report or metric depends on `add_to_wishlist`. If a key business number does depend on it, ask the tracking plan owner to review the Medium rating.

## Acceptance criteria
- Adding an item to a wishlist in a test session produces an `add_to_wishlist` row in the data.
- The tracking plan status for `add_to_wishlist` matches what is actually sent. If the event is not implemented, it is no longer listed as active.
- The planned events check no longer flags `add_to_wishlist` for periods after the fix.
- Wishlist reporting notes that `add_to_wishlist` data is not available for Nov 1, 2020 to Jan 31, 2021.