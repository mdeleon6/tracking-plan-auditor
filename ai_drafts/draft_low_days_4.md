# add_to_cart volume fell below half of its typical level on 6 days between Nov 1, 2020 and Jan 3, 2021

**Event:** add_to_cart
**Found by:** · **Date found:** · **Severity:** High

## Description
An automated low-volume check flagged 6 days on which the `add_to_cart` event arrived in much smaller numbers than usual. The check flags a day when the event's count is below 0.5 of its typical count. "Typical" is the median count for that weekday.

On the worst flagged days, almost no events were received. Nov 1, 2020 had 4 events, which is 0.8% of typical. Nov 20, 2020 had 15 events, which is 2.6% of typical. The other flagged days ranged from 14.5% to 48.4% of typical.

Five of the six flagged days fall right next to periods when `add_to_cart` had no data at all: Nov 2–15, 2020 and Nov 21–24, 2020. Those empty days are covered in a separate missing-day ticket and are not part of this one. One possible but unconfirmed explanation is that some flagged days are partial days at the start or end of those gaps. Days that sit next to each other do not prove that they share a cause.

Jan 3, 2021 is not next to any of the listed gaps. It may need to be looked at on its own.

None of the flagged dates appear on the holiday calendar in the tracking plan.

## Evidence (Nov 1, 2020 – Jan 3, 2021)
- Nov 1, 2020: 4 events, typical 473, 0.8% of typical
- Nov 16, 2020: 85 events, typical 585, 14.5% of typical
- Nov 19, 2020: 187 events, typical 642, 29.1% of typical
- Nov 20, 2020: 15 events, typical 572, 2.6% of typical
- Nov 25, 2020: 297 events, typical 665, 44.7% of typical
- Jan 3, 2021: 229 events, typical 473, 48.4% of typical
- Days with no `add_to_cart` data at all, handled in a separate ticket: Nov 2–15, 2020 and Nov 21–24, 2020.
- Not in the check results: how many weeks each weekday median is based on, and the counts of related events such as purchases or checkouts on these days.

## Impact
According to the tracking plan, `add_to_cart` is used in the add-to-cart rate, the cart-to-purchase conversion rate and the checkout funnel. On the flagged days, the check results only show that far fewer events were received than usual. They do not show whether fewer people actually added items to their carts or whether events were not recorded.

Until that is known, both conversion rates and the checkout funnel cannot be trusted for these dates. This also applies to any weekly or monthly figure that includes these dates. If events were not recorded, the add-to-cart rate would look too low. The cart-to-purchase conversion rate would also look distorted, because purchases would be divided by an incomplete cart count.

Conversion rates are key business numbers, so this is High. The tracking plan also rates the loss of this event as High.

## Suggested next steps
- Find out whether any tracking releases, site changes or collection outages happened on or around each flagged date. This is especially important for the days next to the Nov 2–15 and Nov 21–24 gaps.
- Compare other events on the same six days. This will show whether the drop affects only `add_to_cart` or tracking in general.
- Look into Jan 3, 2021 on its own, since it does not sit next to a known gap.
- Check whether `add_to_cart` events for these days could still arrive late or be recovered. If they are recovered, rerun the low-volume check.
- Coordinate with the owner of the missing-day ticket. If a shared cause is confirmed, the two tickets can be linked.

## Acceptance criteria
- Each of the 6 flagged days has a confirmed explanation. Either the day reflects real user behavior, or the events were not recorded.
- Where events were not recorded and can be recovered, the day's count is no longer flagged by the low-volume check after the data is restored.
- Where events cannot be recovered, the affected dates are documented. Reports using the add-to-cart rate, the cart-to-purchase conversion rate or the checkout funnel either exclude these dates or clearly mark them as unreliable.