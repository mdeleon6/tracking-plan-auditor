# view_item volume below half of typical on Dec 29, 2020 and Jan 2, 2021

**Event:** view_item
**Found by:** · **Date found:** · **Severity:** Medium

## Description
An automated low-volume check flagged the `view_item` event on 2 days. On each day, the number of `view_item` events received was below 0.5 of its typical count. "Typical" means the median count for the same weekday.

The check results show only what was received. They do not show whether fewer items were actually viewed on these days or whether some events were not collected. Neither date has a holiday name in the check results, so neither is on the tracking plan's holiday calendar.

`view_item` was also below the threshold on 7 other days when many events dropped at the same time. A separate multi-event ticket covers those days, so they are not included here.

## Evidence (Dec 29, 2020 – Jan 2, 2021)
- **Dec 29, 2020:** 2308 events, compared with a typical count of 5222 (44.2% of typical).
- **Jan 2, 2021:** 1390 events, compared with a typical count of 3113 (44.7% of typical).
- **Other low days covered by the separate multi-event ticket:**
  - Dec 24, 2020 (Christmas Eve: widely observed)
  - Dec 25, 2020 (Christmas Day: widely observed)
  - Dec 30, 2020
  - Dec 31, 2020 (New Year's Eve: widely observed)
  - Jan 1, 2021 (New Year's Day: widely observed)
  - Jan 4, 2021
  - Jan 18, 2021 (Martin Luther King Jr. Day: US only)
- The check results do not give any counts for those 7 days.

## Impact
The cause of the low counts is not known. There are two possibilities:
- **Some events were not collected.** In that case, `view_item` counts for Dec 29, 2020 and Jan 2, 2021 are understated. Any metric that uses item views on these days would also be off, such as view-to-purchase conversion rates.
- **The low counts reflect real activity.** In that case, the data is accurate as received.

The check results cannot tell these apart.

**Severity is Medium.** Under the general rules, a possible effect on conversion rates would point to High. However, the tracking plan rates this event Medium if it stopped arriving entirely. `view_item` did not stop arriving on either day, so Medium is the highest severity allowed here.

## Suggested next steps
- Find out whether any release, tracking configuration change or data pipeline issue affected `view_item` on or around Dec 29, 2020 or Jan 2, 2021.
- Check whether `view_item` events for these 2 days arrived late, or could still be backfilled. If they are reloaded, run the low-volume check again for these dates.
- Compare these 2 days with other events that are closely tied to item views. This will show whether the drop affected only `view_item` or reflects lower overall activity.
- Decide whether these 2 days should be reviewed together with the separate multi-event ticket. Their dates are close to the days in that ticket, but the check results do not show a shared cause.
- **Possible, unconfirmed explanation:** the calendar names holidays on nearby dates, including Christmas Day (Dec 25, 2020) and New Year's Day (Jan 1, 2021), both widely observed. The period around them may have had lower activity. Neither flagged date is on the holiday calendar, and this has not been confirmed.

## Acceptance criteria
- The reason for the low `view_item` counts on Dec 29, 2020 and Jan 2, 2021 is identified and recorded as either real activity or a data collection problem.
- If it is a data collection problem, one of the following is true:
  - The missing events are restored, and the low-volume check no longer flags these dates.
  - The 2 dates are clearly marked so that analyses using `view_item` can exclude or adjust for them.
- If it is real activity, the 2 dates are documented as expected lows so they are not raised again.