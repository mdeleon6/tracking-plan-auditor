# `click` events fell below half of typical daily volume on 13 days between Dec 26, 2020 and Jan 31, 2021

**Event:** click
**Found by:** · **Date found:** · **Severity:** Low

## Description
The low-volume check flagged the `click` event on 13 days between Dec 26, 2020 and Jan 31, 2021. On each of these days the event count was below 0.5 of its typical count. The typical count is the median for that weekday.

The check results do not show whether these low counts reflect fewer real clicks or clicks that were not received. The event did not stop arriving entirely. The lowest flagged day still recorded 1 event.

Daily volumes for this event are small. Typical counts on the flagged days range from 8 to 16. A drop of a few events can therefore fall below the threshold. This is a possible explanation that has not been confirmed.

## Evidence (Dec 26, 2020 – Jan 31, 2021)
- Dec 26, 2020: 4 events, typical 9, 44.4% of typical
- Dec 27, 2020: 3 events, typical 8, 37.5% of typical
- Jan 11, 2021: 7 events, typical 15, 46.7% of typical
- Jan 13, 2021: 3 events, typical 13, 23.1% of typical
- Jan 17, 2021: 1 events, typical 8, 12.5% of typical
- Jan 19, 2021: 2 events, typical 16, 12.5% of typical
- Jan 20, 2021: 5 events, typical 13, 38.5% of typical
- Jan 21, 2021: 5 events, typical 11, 45.5% of typical
- Jan 22, 2021: 4 events, typical 15, 26.7% of typical
- Jan 25, 2021: 5 events, typical 15, 33.3% of typical
- Jan 27, 2021: 4 events, typical 13, 30.8% of typical
- Jan 30, 2021: 4 events, typical 9, 44.4% of typical
- Jan 31, 2021: 3 events, typical 8, 37.5% of typical
- None of these 13 dates is on the holiday calendar in the tracking plan.
- `click` was also below threshold on 5 more days, when many events dropped together. A separate multi-event ticket covers those days, and they are not part of this ticket:
  - Dec 24, 2020 (Christmas Eve, widely observed)
  - Dec 25, 2020 (Christmas Day, widely observed)
  - Jan 1, 2021 (New Year's Day, widely observed)
  - Jan 4, 2021
  - Jan 18, 2021 (Martin Luther King Jr. Day, observed in the US only)

  For the named dates, the holiday is a possible, unconfirmed explanation. The 13 days in this ticket fall near some of those dates. That does not show they share a cause.

## Impact
According to the tracking plan, `click` is used in outbound link reporting. Outbound link counts for the 13 flagged days will be lower than typical. Until the cause is known, those reports cannot show whether that reflects real behavior or incomplete tracking. Trends across late December and January may look weaker than usual.

The tracking plan rates this event Low if it stopped arriving entirely. The event did not stop arriving, so Low is the highest severity allowed here. Under the severity rules, the problem affects one reporting area and has little effect on key business numbers such as revenue, orders or conversion rates. That also points to Low.

## Suggested next steps
- Check whether the `click` tracking, or the outbound links it records, changed around Dec 26, 2020 or during January 2021.
- Find out whether another source records outbound link clicks for the flagged days. If one exists, compare it with the received `click` counts to see whether the drop also appears there.
- Check whether `click` counts returned to typical levels after Jan 31, 2021. The check results do not cover dates after Jan 31, 2021.
- Look at the outcome of the separate multi-event ticket. It may help explain the January drops, but these days should be investigated on their own and not assumed to share its cause.

## Acceptance criteria
- The cause of the low counts on the 13 flagged days is identified and confirmed as either real behavior or a tracking problem.
- If it is a tracking problem, the problem is fixed, and daily `click` counts stay at or above 0.5 of typical outside days covered by known multi-event drops.
- Outbound link reports covering Dec 26, 2020 – Jan 31, 2021 carry a note about the flagged days until the cause is confirmed.