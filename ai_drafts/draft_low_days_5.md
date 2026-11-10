# `click` events fell below half their typical daily count on 13 days from Dec 26, 2020 to Jan 31, 2021

**Event:** click
**Found by:** · **Date found:** · **Severity:** Low

## Description
An automated low-volume check flagged the `click` event on 13 days between Dec 26, 2020 and Jan 31, 2021. The check flags a day when an event's count falls below 0.5 of its typical count. The typical count is the median count for that day of the week.

Most flagged days fall in the second half of January 2021. Every day from Jan 17 to Jan 22, 2021 was below threshold. Jan 18 is not in this ticket's list because it is covered by a separate ticket, described below. The lowest days were Jan 17 and Jan 19, 2021, both at 12.5% of typical.

`click` was also below threshold on 5 more days when many events dropped at the same time: Dec 24, 2020, Dec 25, 2020, Jan 1, 2021, Jan 4, 2021 and Jan 18, 2021. Those days are covered in a separate multi-event ticket and are not part of this ticket.

The check results do not show whether these low counts reflect fewer clicks actually happening or clicks that happened but were not recorded. They also do not show the cause.

## Evidence (Dec 26, 2020 – Jan 31, 2021)
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

The check results do not include the following:
- The date range used to calculate each weekday's median.
- Total `click` counts for the period.
- Counts for days that were not flagged.

## Impact
The tracking plan rates `click` as Low if it stopped arriving entirely. On these days `click` did not stop arriving entirely, because events were still received on every flagged day. A partial drop cannot be rated higher than a complete stop, so Low is the highest severity allowed here. The severity rules give no reason to go lower:
- `click` is not a revenue, order or conversion measure.
- This drop does not appear to affect any key business totals.

Any analysis that counts clicks or tracks click trends over this period may still be affected. This includes daily or weekly click counts and comparisons of January 2021 with other months. Receiving some events on a day does not show that the day's data is complete. Click counts for the flagged days should be treated with caution until the drop is explained.

The typical daily counts for `click` are small, between 8 and 16 on the flagged days. With counts this small, a drop of a few events produces a large percentage change. This is worth considering when judging how unusual these days are.

## Suggested next steps
- Find out whether anything changed in how `click` is tracked around late December 2020 or mid-January 2021, such as a release, a page change or a tracking configuration change. Nothing in the check results confirms any such change.
- Find out whether real click activity could plausibly have been lower on these days. For example, Dec 26–27 fall during the holiday period. This is a possible explanation only and has not been confirmed. It would not explain the run of low days later in January.
- Check whether events for these days could have arrived late, and whether re-pulling the data changes the counts.
- After the separate multi-event ticket is investigated, check whether its findings also apply to these 13 days. The two sets of days should not be assumed to share a cause.

## Acceptance criteria
- Each of the 13 flagged days has one of these outcomes, documented in this ticket:
  - It is confirmed as real low activity, with the evidence used to confirm it.
  - It is confirmed as a tracking problem, and the problem is fixed or the data is restored.
- If a tracking problem is found and fixed, re-running the low-volume check on `click` for Dec 26, 2020 – Jan 31, 2021 no longer flags the affected days, or any remaining flags are explained.