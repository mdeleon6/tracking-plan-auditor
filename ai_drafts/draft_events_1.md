# `add_to_wishlist` is listed as active in the tracking plan but has 0 rows from Nov 1, 2020 to Jan 31, 2021

**Event:** add_to_wishlist
**Found by:** · **Date found:** · **Severity:** Medium

## Description
The tracking plan lists `add_to_wishlist` as an active event, but no rows for this event were received at any point between Nov 1, 2020 and Jan 31, 2021. The automated planned-events check flagged it. That check flags any event the tracking plan lists as active that never appears in the data.

The check results show only what was received. They do not show whether users added items to a wishlist during this period. The cause has not been confirmed. Several possible, unconfirmed explanations are worth checking:
- The event was never set up.
- The wishlist feature was not available.
- Wishlist actions were sent under a different event name.
- The event was sent but did not reach this dataset.

## Evidence (Nov 1, 2020 – Jan 31, 2021)
- Check: planned events.
- Rows received for `add_to_wishlist` across the whole period: 0.
- Tracking plan status for `add_to_wishlist`: active.
- The tracking plan lists the event as used in wishlist reporting.
- The check results do not include a first or last date the event was ever received, and they do not cover any period outside Nov 1, 2020 to Jan 31, 2021.

## Impact
Wishlist reporting cannot be built from this data for Nov 1, 2020 to Jan 31, 2021, because the event it relies on has no rows. Any wishlist figures for this period may be empty, may show as zero, or may be missing. A zero would not tell you whether customers used wishlists.

The severity is Medium, as set by the tracking plan. This fits the impact: the tracking plan names wishlist reporting as the only use of this event, which is one type of reporting. The check results do not show any key business number, such as revenue, orders, units sold or conversion rates, that depends on `add_to_wishlist`. The check results also do not say how often wishlist reporting is used or whether decisions are made from it.

## Suggested next steps
- Confirm whether `add_to_wishlist` was actually implemented and expected to send data between Nov 1, 2020 and Jan 31, 2021. Also confirm whether the "active" status in the tracking plan was correct for this period.
- Confirm whether the wishlist feature was available to users during this period.
- Check whether wishlist actions appear in the data under another event name or as part of another event. This is a possible explanation only and has not been confirmed.
- If the event was sent, find out where the rows went and whether they can be recovered for this period.
- Let the people who use wishlist reporting know that this period has no `add_to_wishlist` rows. Find out what the reporting currently shows for these dates.

## Acceptance criteria
- Either `add_to_wishlist` rows are received whenever a wishlist add occurs, or the tracking plan is updated so the event is no longer listed as active.
- The cause of the 0 rows is confirmed and recorded on this ticket.
- Wishlist reporting for Nov 1, 2020 to Jan 31, 2021 is marked as having no `add_to_wishlist` data, unless the missing rows are recovered.