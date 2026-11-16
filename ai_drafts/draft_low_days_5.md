# `click` events fell below half of their typical daily count on 13 days between Dec 26, 2020 and Jan 31, 2021

**Event:** click
**Found by:** · **Date found:** · **Severity:** Low

## Description
The automated low-volume check flagged 13 days on which the `click` event arrived at less than half of its typical count. "Typical" is the median count for the same weekday. The flagged days run from Dec 26, 2020 to Jan 31, 2021, and most of them fall in January 2021.

The check results only show how many events were received. They do not show whether fewer clicks actually happened or whether clicks happened and were not recorded. The cause is not confirmed.

`click` also fell below the threshold on 5 other days when many events dropped at the same time. Those days are covered in a separate multi-event ticket and are not part of this ticket.

## Evidence (Dec 26, 2020 – Jan 31, 2021)
- Check rule: a day is flagged when the event's count is below 0.5 of its typical count, meaning the median for that weekday.
- Number of flagged days: 13.
- Dec 26, 2020: 4 events, typical 9, 44.4% of typical
- Dec 27, 2020: 3 events, typical 8, 37.5% of typical
- Jan 11, 2021: 7 events, typical 15, 46.7% of typical
- Jan 13, 2021: 3 events, typical 13, 23.1% of typical
- Jan 17, 2021: 1 event, typical 8, 12.5% of typical
- Jan 19, 2021: 2 events, typical 16, 12.5% of typical
- Jan 20, 2021: 5 events, typical 13, 38.5% of typical
- Jan 21, 2021: 5 events, typical 11, 45.5% of typical
- Jan 22, 2021: 4 events, typical 15, 26.7% of typical
- Jan 25, 2021: 5 events, typical 15, 33.3% of typical
- Jan 27, 2021: 4 events, typical 13, 30.8% of typical
- Jan 30, 2021: 4 events, typical 9, 44.4% of typical
- Jan 31, 2021: 3 events, typical 8, 37.5% of typical
- None of the 13 flagged days has a holiday name next to it in the check results. This means none of them is on the tracking plan's holiday calendar.
- Days excluded from this ticket because they belong to the separate multi-event ticket:
  - Dec 24, 2020 (Christmas Eve: widely observed)
  - Dec 25, 2020 (Christmas Day: widely observed)
  - Jan 1, 2021 (New Year's Day: widely observed)
  - Jan 4, 2021
  - Jan 18, 2021 (Martin Luther King Jr. Day: US only)
- Not in the check results:
  - Total `click` count for the whole period.
  - Daily counts for the days that were not flagged.
  - Any data after Jan 31, 2021.

## Impact
The tracking plan lists `click` as used only in outbound link reporting. On the 13 flagged days, that reporting will show fewer clicks than usual. Nobody can yet tell whether that reflects real user behavior or a recording problem.

The check results do not give a total for the period, so this ticket cannot say what share of all clicks the low days account for.

Severity is Low for these reasons:
- According to the tracking plan, no key business number such as revenue, orders, units sold or conversion rate depends on `click`.
- The tracking plan rates this event Low even if it stopped arriving entirely. A partial drop on some days should not rate higher than that.
- The typical counts on the flagged days are between 8 and 16 events. At these volumes, a difference of a few events is enough to put a day below the threshold.

If outbound link reporting is used for decisions, the rating may need to change.

## Suggested next steps
- Confirm with whoever uses outbound link reporting whether any decisions or reviews rely on daily click counts for Dec 26, 2020 – Jan 31, 2021.
- Check whether anything changed in how `click` is sent during this period, for example a release, a tagging change, or a change to the pages or links that fire it.
- Pull daily `click` counts after Jan 31, 2021 to see whether low days continue. The check results stop at Jan 31, 2021.
- Pull the total `click` count and the counts for non-flagged days in this period. This will show whether the drop is limited to the flagged days or is part of a wider decline.
- Review whether a threshold of 0.5 of the weekday median is suitable for an event with typical counts this small. Short-term variation alone may be enough to trigger it. This is a possible explanation and is unconfirmed.

## Acceptance criteria
- For each of the 13 flagged days, the low count is documented as either confirmed real behavior or a confirmed tracking issue, with the evidence used.
- If a tracking issue is confirmed, it is fixed, and later daily `click` counts stay at or above 0.5 of the weekday median.
- Outbound link reporting carries a note on the 13 flagged days so readers know the counts are under review.