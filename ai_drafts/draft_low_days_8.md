# view_item events fell below half of typical on Dec 29, 2020 and Jan 2, 2021

**Event:** view_item
**Found by:** · **Date found:** · **Severity:** Medium

## Description
An automated low-volume check flagged 2 days where the `view_item` event arrived well below its usual level. A day is flagged when an event's count is below 0.5 of its typical count. "Typical" means the median count for that day of the week.

On both flagged days, `view_item` was under half of typical:
- Dec 29, 2020: 44.2% of typical
- Jan 2, 2021: 44.7% of typical

Neither date is on the holiday calendar in the tracking plan. These 2 days are separate from the multi-event drops described below. The check results do not show why the count was low, and they do not show whether the lower count reflects fewer product views or events that were not received.

## Evidence
- Dec 29, 2020: 2308 events received, typical 5222, 44.2% of typical.
- Jan 2, 2021: 1390 events received, typical 3113, 44.7% of typical.
- `view_item` was also below the threshold on 7 more days, when many events dropped together. A separate multi-event ticket covers those days, so they are not part of this ticket:
  - Dec 24, 2020 (Christmas Eve, widely observed)
  - Dec 25, 2020 (Christmas Day, widely observed)
  - Dec 30, 2020
  - Dec 31, 2020 (New Year's Eve, widely observed)
  - Jan 1, 2021 (New Year's Day, widely observed)
  - Jan 4, 2021
  - Jan 18, 2021 (Martin Luther King Jr. Day, US only)
- Both flagged days fall within the same span of dates as several of the multi-event days. A link between them is possible but unconfirmed. Drops that happen near each other do not prove a shared cause.
- The check results do not include a breakdown by country or platform. They also do not include counts for related events, such as add-to-cart, on the flagged days.

## Impact
According to the tracking plan, `view_item` is used for:
- product views
- view-to-cart rate
- product performance by country and platform

On Dec 29, 2020 and Jan 2, 2021, the product view counts can't be relied on until the low volume is explained. These counts may be complete, or they may be missing events. The check results do not show which.

The view-to-cart rate for those days is also uncertain. If views are understated and add-to-cart events are not, the rate would be overstated. The check results do not include add-to-cart counts, so the effect on this rate is unknown.

The check results also do not show whether the drop affects all countries and platforms equally. Comparisons of product performance by country and platform on these days may be skewed.

**Why Medium:** On these 2 days, the problem affects a key rate (view-to-cart), which on its own would point to High. However, the tracking plan rates `view_item` as Medium if the event stopped arriving entirely. For a low-volume problem, that rating is the highest severity allowed. The event did not stop on these days, so Medium is the cap.

## Suggested next steps
- Break down `view_item` counts for Dec 29, 2020 and Jan 2, 2021 by country and platform. Check whether the drop is spread evenly or concentrated in one segment.
- Compare other events on the same 2 days, especially add-to-cart. This will show whether the view-to-cart rate moved and whether the drop is limited to `view_item`.
- Check whether any tracking, app or site changes were released close to these dates that could affect `view_item`.
- Check whether `view_item` events for these days arrived late or could be reprocessed. If so, compare the updated counts with the counts in the check results.
- Review the separate multi-event ticket for findings that may also apply to these 2 days. Do not assume the same cause until it is confirmed.

## Acceptance criteria
- The reason for the low `view_item` count is identified and documented for both Dec 29, 2020 and Jan 2, 2021, or documented as unknown.
- If events are found to be missing and can be recovered, the counts are restored. The check is then re-run to confirm whether either day is still below 0.5 of typical.
- If the low counts are confirmed as real activity, or the missing events cannot be recovered, both days are marked in reporting. Anyone using product views, view-to-cart rate or product performance by country and platform for these dates should be aware of the limitation.