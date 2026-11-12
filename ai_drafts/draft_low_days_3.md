# `add_shipping_info` events below half of typical volume on 12 days from Dec 26, 2020 to Jan 15, 2021

**Event:** add_shipping_info
**Found by:** · **Date found:** · **Severity:** High

## Description
The `add_shipping_info` event was received at less than half its usual volume on 12 days between Dec 26, 2020 and Jan 15, 2021. The low volume check flags a day when an event's count falls below 0.5 of its typical count. The typical count is the median for that weekday. On the flagged days, the count was between 32.4% and 49.4% of typical.

The check results show only how many events were received. They do not show whether fewer users actually added shipping info or whether events were sent but not received. The cause has not been confirmed.

The event was also below threshold on 7 other days when many events dropped together. A separate multi-event ticket covers those days, so this ticket does not include them.

## Evidence (Dec 26, 2020 – Jan 15, 2021)
- Dec 26, 2020: 48 events, typical 148, 32.4% of typical
- Dec 28, 2020: 101 events, typical 211, 47.9% of typical
- Dec 29, 2020: 80 events, typical 233, 34.3% of typical
- Jan 2, 2021: 48 events, typical 148, 32.4% of typical
- Jan 3, 2021: 51 events, typical 129.5, 39.4% of typical
- Jan 5, 2021: 88 events, typical 233, 37.8% of typical
- Jan 6, 2021: 116 events, typical 248, 46.8% of typical
- Jan 8, 2021: 105 events, typical 269, 39.0% of typical
- Jan 9, 2021: 58 events, typical 148, 39.2% of typical
- Jan 10, 2021: 58 events, typical 129.5, 44.8% of typical
- Jan 11, 2021: 94 events, typical 211, 44.5% of typical
- Jan 15, 2021: 133 events, typical 269, 49.4% of typical
- None of these 12 dates is on the holiday calendar in the tracking plan.
- The 7 days covered by the separate multi-event ticket are Dec 24, 2020 (Christmas Eve, widely observed), Dec 25, 2020 (Christmas Day, widely observed), Dec 30, 2020, Dec 31, 2020 (New Year's Eve, widely observed), Jan 1, 2021 (New Year's Day, widely observed), Jan 4, 2021 and Jan 18, 2021 (Martin Luther King Jr. Day, US only).
- The check results do not include the following:
  - a total event count for the period
  - counts on the days that were not flagged
  - a breakdown by country or platform
  - counts for other checkout events on these days

## Impact
According to the tracking plan, `add_shipping_info` feeds the checkout funnel and the checkout conversion rate by country and platform. Checkout conversion rate is a key business number. Its values for the 12 flagged days cannot be trusted until someone confirms whether the drop reflects real user behavior or a tracking problem. The tracking plan rates this event High if it stopped arriving entirely.

This ticket is rated High because a key business number depends on this event. The event did not stop arriving, but on every flagged day it fell below half its typical volume.

The days around these dates include named holidays. Possibly, and unconfirmed, the lower volume on some days reflects real changes in shopping behavior during this period. However, none of the 12 flagged days is itself on the holiday calendar, and this possibility does not explain the drop. These 12 days also fell below threshold while most other events did not drop with them, which is why they were not grouped into the multi-event ticket. The check results do not say whether other checkout events dropped on these days.

The check results do not show which countries or platforms were affected. Any country or platform split of checkout conversion rate for these days may therefore be affected in ways not yet known.

## Suggested next steps
- For each of the 12 days, compare `add_shipping_info` counts with the checkout funnel steps before and after it. A drop in this event alone would point toward a tracking problem. A drop across the whole funnel would point toward a real change in user behavior.
- Break the flagged days down by country and platform to see whether the drop is limited to particular segments.
- Find out whether any changes to the site, app or tracking setup were released around Dec 26, 2020, and whether any of them touched the shipping step of checkout.
- Coordinate with the owner of the separate multi-event ticket. Together, decide whether this event's drop on those 7 days should be reviewed together with the 12 days in this ticket.

## Acceptance criteria
- For each of the 12 flagged days, the drop is documented either as real user behavior, with supporting evidence from the other funnel steps, or as a tracking problem with a stated cause.
- If the drop is a tracking problem, the fix is in place and missing events are restored where possible. The checkout conversion rate for affected days is then either corrected or clearly labelled as unreliable in reporting.
- The country and platform breakdown of the drop is recorded, so that users of checkout conversion rate by country and platform know which segments were affected.