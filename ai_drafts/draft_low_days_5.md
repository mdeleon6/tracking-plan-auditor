# `click` events fell below half of their typical daily count on 13 days from Dec 26, 2020 to Jan 31, 2021

**Event:** click
**Found by:** · **Date found:** · **Severity:** Low

## Description
An automated low-volume check flagged the `click` event on 13 days between Dec 26, 2020 and Jan 31, 2021. The check flags a day when the event's count is below 0.5 of its typical count. "Typical" means the median count for that weekday.

On each flagged day, the check results show only a few `click` events, between 1 and 7. The typical counts for those days are between 8 and 16. Two flagged days are in late December 2020, and the rest are spread through January 2021.

The check results only show how many events were received. They do not show whether fewer clicks actually happened or whether clicks happened and were not recorded. The cause is unknown.

## Evidence (Dec 26, 2020 – Jan 31, 2021)
| Date | Events received | Typical | % of typical |
|---|---|---|---|
| Dec 26, 2020 | 4 | 9 | 44.4% |
| Dec 27, 2020 | 3 | 8 | 37.5% |
| Jan 11, 2021 | 7 | 15 | 46.7% |
| Jan 13, 2021 | 3 | 13 | 23.1% |
| Jan 17, 2021 | 1 | 8 | 12.5% |
| Jan 19, 2021 | 2 | 16 | 12.5% |
| Jan 20, 2021 | 5 | 13 | 38.5% |
| Jan 21, 2021 | 5 | 11 | 45.5% |
| Jan 22, 2021 | 4 | 15 | 26.7% |
| Jan 25, 2021 | 5 | 15 | 33.3% |
| Jan 27, 2021 | 4 | 13 | 30.8% |
| Jan 30, 2021 | 4 | 9 | 44.4% |
| Jan 31, 2021 | 3 | 8 | 37.5% |

- None of these 13 dates appears on the holiday calendar in the tracking plan.
- `click` was also below the threshold on 5 more days. On those days many events dropped together, so they are covered in a separate multi-event ticket and are not part of this one:
  - Dec 24, 2020 (Christmas Eve: widely observed)
  - Dec 25, 2020 (Christmas Day: widely observed)
  - Jan 1, 2021 (New Year's Day: widely observed)
  - Jan 4, 2021
  - Jan 18, 2021 (Martin Luther King Jr. Day: US only)
- The check results do not include:
  - `click` counts for days that were not flagged.
  - The total `click` count for the period.
  - The date range used to calculate the typical counts.

## Impact
According to the tracking plan, `click` is used in outbound link reporting. The flagged days could make outbound link counts for late December 2020 and January 2021 look lower than usual. Any trend or comparison across this period could be affected.

Severity is Low for three reasons:
- The tracking plan rates `click` as Low even if it stopped arriving entirely.
- The flagged days involve only a few events each.
- The check results do not tie `click` to any key business number such as revenue, orders, units sold or conversion rates.

If outbound link reporting is used to make decisions, this should be reviewed as Medium.

The flagged days are spread across most of January rather than isolated. This could mean a sustained drop, but that is possible and unconfirmed. The typical counts are also small, so day-to-day variation could push a day below the 0.5 threshold without any tracking problem. That is also possible and unconfirmed.

## Suggested next steps
- Find out whether anything changed in how `click` is tracked around late December 2020 or January 2021.
- Pull daily `click` counts for the days in this period that were not flagged. This shows whether volume was lower across the whole period or only on the flagged days.
- Compare `click` with related events on the same 13 days. This shows whether the drop affects only `click`.
- Confirm with the users of outbound link reporting whether they rely on this period, to settle the severity.

## Acceptance criteria
- Each of the 13 flagged days has one of these outcomes:
  - It is confirmed as real behavior, and the evidence is recorded on this ticket.
  - Its tracking issue is identified, and the counts are corrected where possible.
- If a tracking issue is found, a re-run of the low-volume check over the same period no longer flags `click` on days where the issue was fixed.
- Outbound link reporting for Dec 26, 2020 to Jan 31, 2021 includes a note about these days until they are resolved.