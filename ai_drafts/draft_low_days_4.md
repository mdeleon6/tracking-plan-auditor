# add_to_cart volume below half of typical on 6 days between Nov 1, 2020 and Jan 3, 2021

**Event:** add_to_cart
**Found by:** · **Date found:** · **Severity:** High

## Description
On 6 days, the `add_to_cart` event arrived at less than half its usual volume. The low-volume check flags a day when the event's count is below 0.5 of its typical count. "Typical" means the median count for that weekday.

Five of the flagged days fall in November 2020, and one falls on Jan 3, 2021. On two days, Nov 1 and Nov 20, 2020, almost no events arrived (0.8% and 2.6% of typical). The other days arrived at between 14.5% and 48.4% of typical.

The check results only show how many events were received. They do not show whether add-to-cart activity actually dropped on these days or whether events were not received.

This event also has days with no data at all, from Nov 2 to Nov 15, 2020 and from Nov 21 to Nov 24, 2020. Those days are covered in a separate missing-day ticket and are not part of this one.

## Evidence (Nov 1, 2020 – Jan 3, 2021)
- Nov 1, 2020: 4 events, typical 473, 0.8% of typical
- Nov 16, 2020: 85 events, typical 585, 14.5% of typical
- Nov 19, 2020: 187 events, typical 642, 29.1% of typical
- Nov 20, 2020: 15 events, typical 572, 2.6% of typical
- Nov 25, 2020: 297 events, typical 665, 44.7% of typical
- Jan 3, 2021: 229 events, typical 473, 48.4% of typical
- None of these dates are named on the holiday calendar in the tracking plan.
- Four of the flagged days fall right next to the missing-day periods:
  - Nov 1 is the day before Nov 2–15.
  - Nov 16 is the day after Nov 2–15.
  - Nov 20 is the day before Nov 21–24.
  - Nov 25 is the day after Nov 21–24.
  
  This is an observation only. It has not been confirmed that the low volume and the missing days share a cause.

## Impact
The tracking plan uses `add_to_cart` in the add-to-cart rate, the cart-to-purchase conversion rate and the checkout funnel. These are key business numbers.

On the flagged days, the add_to_cart counts are far below normal. Until someone confirms whether these counts reflect real activity, those three numbers cannot be trusted for these days. The same applies to any period that includes these days, such as weekly or monthly figures for November 2020 and early January 2021.

The tracking plan rates this event High if it stopped arriving entirely. For a low-volume problem, that rating is the highest severity allowed. This ticket is rated High because conversion rates and the funnel built on this event cannot be trusted for the affected days.

## Suggested next steps
- For each of the 6 days, confirm whether all `add_to_cart` events were received, or whether real add-to-cart activity was low.
- Check whether other events in the checkout funnel also show low volume on these same days. This would show whether the drop affects `add_to_cart` alone.
- Review the 4 flagged days next to the missing-day periods together with the separate missing-day ticket. The goal is to see whether they may be related. That link is possible but unconfirmed.
- Look at Nov 19 and Jan 3, 2021 separately. They do not border a missing-day period.

## Acceptance criteria
- Each of the 6 flagged days has a documented explanation. Either the low count is confirmed as real activity, or the events that were not received are identified.
- Where events were not received and can be recovered, the low-volume check no longer flags that day after the data is updated.
- Any day that stays below 0.5 of typical and cannot be explained is clearly noted for anyone using the add-to-cart rate, the cart-to-purchase conversion rate or the checkout funnel.