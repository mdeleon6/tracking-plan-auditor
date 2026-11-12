# add_payment_info below 0.5 of typical volume on 10 days from Dec 26, 2020 to Jan 13, 2021

**Event:** add_payment_info
**Found by:** · **Date found:** · **Severity:** High

## Description
The `add_payment_info` event was received at less than 0.5 of its typical daily count on 10 days between Dec 26, 2020 and Jan 13, 2021. "Typical" is the median count for the same weekday. On these 10 days the event arrived at between 31.5% and 49.3% of typical. The lowest day was Jan 2, 2021, at 31.5%.

The check results only show how many events were received. They do not show whether fewer people added payment information on these days or whether events were sent but not received. The cause of the low counts is not confirmed.

The event was also below the threshold on 7 more days, when many events dropped together. A separate multi-event ticket covers those days, so they are left out of this ticket. Some of those 7 days have holiday names in the check results. The check results name no holiday next to any of the 10 days in this ticket.

## Evidence (Dec 26, 2020 – Jan 13, 2021)
Flagged days for `add_payment_info` (received count, typical count, % of typical):
- Dec 26, 2020: 40 events, typical 89, 44.9% of typical
- Dec 29, 2020: 67 events, typical 168, 39.9% of typical
- Jan 2, 2021: 28 events, typical 89, 31.5% of typical
- Jan 3, 2021: 33 events, typical 73.5, 44.9% of typical
- Jan 5, 2021: 58 events, typical 168, 34.5% of typical
- Jan 6, 2021: 93 events, typical 193, 48.2% of typical
- Jan 7, 2021: 67 events, typical 136, 49.3% of typical
- Jan 8, 2021: 81 events, typical 189, 42.9% of typical
- Jan 9, 2021: 42 events, typical 89, 47.2% of typical
- Jan 13, 2021: 92 events, typical 193, 47.7% of typical

The 7 days covered by the separate multi-event ticket, as listed in the check results:
- Dec 24, 2020 (Christmas Eve: widely observed)
- Dec 25, 2020 (Christmas Day: widely observed)
- Dec 30, 2020
- Dec 31, 2020 (New Year's Eve: widely observed)
- Jan 1, 2021 (New Year's Day: widely observed)
- Jan 4, 2021
- Jan 18, 2021 (Martin Luther King Jr. Day: US only)

Information that is missing from the check results:
- Counts for other checkout funnel events on the 10 flagged days.
- A breakdown of the flagged days by country or platform.
- The checkout conversion rates for these days.
- Any query or link behind the check.

## Impact
According to the tracking plan, `add_payment_info` feeds the checkout funnel and the checkout conversion rate by country and platform. On the 10 flagged days, the received count was below 0.5 of typical. Until someone confirms whether these counts reflect real activity, the following figures cannot be trusted for those days:
- The funnel step for `add_payment_info`.
- Any checkout conversion rate built on that step.
- Comparisons of these figures across this period.

The severity is High because a conversion rate is a key business number and it depends on this event. The tracking plan also rates this event High if it stopped arriving entirely. The event did not stop on these days, but its counts were low enough to affect that conversion rate.

Without a country and platform breakdown, it is unknown whether the low counts affect all countries and platforms or only some of them.

## Suggested next steps
- Compare the received counts of the funnel steps before and after `add_payment_info` on the 10 flagged days. If those steps stayed near typical while this event fell, that may point to a tracking problem rather than lower activity. This is possible and unconfirmed.
- Break down `add_payment_info` on the flagged days by country and platform. This shows whether the drop is spread evenly or concentrated in one segment.
- Find out whether any changes to the checkout payment step or its tracking were released between Dec 26, 2020 and Jan 13, 2021.
- Find out whether events for these days could still arrive late. If the data is re-pulled, re-run the low volume check for these dates.

## Acceptance criteria
- Each of the 10 flagged days is either:
  - confirmed as real activity, with the evidence recorded on this ticket, or
  - traced to a tracking or delivery problem, with the cause recorded on this ticket.
- If a tracking or delivery problem is found, it is fixed or the affected data is restored. Re-running the low volume check for `add_payment_info` on these dates must then show each day at or above 0.5 of typical, or the remaining gap must be explained.
- Checkout funnel and conversion rate reports carry a note about these 10 days until the above is resolved.