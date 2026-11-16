# `add_to_cart` volume is below 0.5 of typical on 6 days between Nov 1, 2020 and Jan 3, 2021

**Event:** add_to_cart
**Found by:** · **Date found:** · **Severity:** High

## Description
The automated low-volume check flagged 6 days on which far fewer `add_to_cart` events were received than usual. The check flags a day when its count is below 0.5 of the typical count. "Typical" means the median count for that weekday.

Two of the days are almost empty. Nov 1, 2020 received 4 events, which is 0.8% of typical. Nov 20, 2020 received 15 events, which is 2.6% of typical. The other four days fall between 14.5% and 48.4% of typical.

The check results only show how many events were received. They do not show whether fewer people added items to their carts on these days or whether events were sent but not recorded. The cause is unknown.

## Evidence
From the automated low-volume check:

| Date | Events received | Typical (weekday median) | % of typical |
|---|---|---|---|
| Nov 1, 2020 | 4 | 473 | 0.8% |
| Nov 16, 2020 | 85 | 585 | 14.5% |
| Nov 19, 2020 | 187 | 642 | 29.1% |
| Nov 20, 2020 | 15 | 572 | 2.6% |
| Nov 25, 2020 | 297 | 665 | 44.7% |
| Jan 3, 2021 | 229 | 473 | 48.4% |

- None of these dates has a holiday name next to it in the check results. This means none of them is on the tracking plan's holiday calendar.
- The check results also report days with no `add_to_cart` data at all: Nov 2–15, 2020 and Nov 21–24, 2020. Those days belong to a separate missing-day ticket and are not counted here.
- Four of the flagged days sit directly next to those empty ranges:
  - Nov 1 is the day before the Nov 2–15 range.
  - Nov 16 is the day after it.
  - Nov 20 is the day before the Nov 21–24 range.
  - Nov 25 is the day after it.

  This is an observation only. It does not show that the low days and the empty days share a cause.
- The check results do not include:
  - the total `add_to_cart` count for the period
  - counts for other events, such as `purchase`, on these days

## Impact
According to the tracking plan, `add_to_cart` is used in three places:
- the add-to-cart rate
- the cart-to-purchase conversion rate
- the checkout funnel

On the flagged days, these numbers cannot be trusted. The same applies to any weekly, monthly or period figure that includes these days. Conversion rates are key business numbers, which is why this ticket is rated **High**.

The tracking plan rates this event High if it stops arriving entirely. In this case the event did not stop entirely on these days, but on Nov 1 and Nov 20 it came close.

It is not known whether the low counts reflect real user behavior or a recording problem. If `add_to_cart` events were under-recorded while purchases were recorded normally, the cart-to-purchase rate would be overstated on these days. This is possible but unconfirmed, because the check results do not include purchase counts.

## Suggested next steps
- Compare `purchase` and the other checkout funnel events on the same 6 days. This will show whether the drop is limited to `add_to_cart` or appears across the funnel.
- Ask whoever owns the `add_to_cart` implementation whether anything changed or failed around Nov 1, Nov 16, Nov 19, Nov 20, Nov 25, 2020 and Jan 3, 2021.
- Work with the owner of the missing-day ticket to check whether the four flagged days next to the empty ranges are connected to those ranges. Do not assume they are.
- Check separately whether Nov 19, 2020 and Jan 3, 2021 have their own explanation, since neither sits next to an empty range.
- If the data can be sent again for these days, re-run the low-volume check afterwards.

## Acceptance criteria
- Each of the 6 days is either:
  - back at or above 0.5 of its typical count after the data is corrected, **or**
  - confirmed as real user behavior, with the explanation recorded.
- Until then, any report using the add-to-cart rate, cart-to-purchase conversion rate or checkout funnel either excludes these 6 days or clearly labels them as unreliable.