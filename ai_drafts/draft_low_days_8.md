# `view_item` fell below half of its typical daily count on Dec 29, 2020 and Jan 2, 2021

**Event:** view_item
**Found by:** · **Date found:** · **Severity:** Medium

## Description
On two days, the `view_item` event arrived at less than half its usual volume. On Dec 29, 2020, 2308 events were received against a typical 5222. On Jan 2, 2021, 1390 were received against a typical 3113.

An automated low-volume check flagged these days. The check flags a day when an event's count is below 0.5 of its typical count. "Typical" means the median count for that weekday.

The check results only show what was received. They do not show whether product viewing really dropped on these days or whether views happened but were not recorded. The cause is not known.

## Evidence (Dec 29, 2020 and Jan 2, 2021)
- **Dec 29, 2020:** 2308 `view_item` events, against a typical 5222. This is 44.2% of typical.
- **Jan 2, 2021:** 1390 `view_item` events, against a typical 3113. This is 44.7% of typical.
- **Holiday calendar:** Neither date has a holiday name next to it in the check results. According to the check results, this means neither date is on the tracking plan's holiday calendar.
- **Days handled in a separate ticket:** `view_item` was also below the threshold on 7 other days when many events dropped together. Those days are covered in a separate multi-event ticket and are not part of this ticket:
  - Dec 24, 2020 (Christmas Eve: widely observed)
  - Dec 25, 2020 (Christmas Day: widely observed)
  - Dec 30, 2020
  - Dec 31, 2020 (New Year's Eve: widely observed)
  - Jan 1, 2021 (New Year's Day: widely observed)
  - Jan 4, 2021
  - Jan 18, 2021 (Martin Luther King Jr. Day: US only)
- **Unclear whether other events dropped:** The check results list Dec 29 and Jan 2 separately from the days when many events dropped together. They do not say directly whether any other event was low on these two days.
- **Missing from the check results:**
  - Counts for other events on these two days, such as add-to-cart.
  - A breakdown of the drop by country or platform.
  - Whether any events for these days arrived later.

## Impact
According to the tracking plan, `view_item` feeds three reports:
- **Product views:** Totals for Dec 29, 2020 and Jan 2, 2021 will show less than half the usual count. Any period that includes these days will be lower than usual.
- **View-to-cart rate:** The rate for these two days may be distorted. If add-to-cart events arrived normally, the rate would look higher than usual. The check results do not include add-to-cart counts, so the size and direction of any effect is unknown.
- **Product performance by country and platform:** The check results do not show whether the drop was spread evenly or concentrated in one country or platform. Until that is known, comparisons between countries or platforms on these days should not be relied on.

**Why Medium:**
- The tracking plan rates a complete loss of `view_item` as Medium.
- This problem is limited to two days, with some events still arriving.
- Revenue, orders and units sold are not listed among the uses of `view_item`.
- View-to-cart rate is a funnel rate. If the business treats it as a key conversion rate, a higher severity may be justified. This is raised as a next step below.

## Suggested next steps
- Break down `view_item` on Dec 29, 2020 and Jan 2, 2021 by country and platform. This will show whether the drop is spread evenly or limited to one segment.
- Compare other events on the same two days, especially add-to-cart. This will show whether the drop was specific to `view_item` and whether view-to-cart rate was affected.
- Check whether any tracking or site changes were made around these two dates. Do not assume a cause until one is confirmed.
- Check whether any `view_item` events for these dates arrived late or can be re-pulled.
- Coordinate with the owner of the separate multi-event ticket. Neighboring dates such as Dec 30, 2020 and Dec 31, 2020 are covered there. Days that appear close together do not prove a shared cause, so treat these two days as separate unless a link is confirmed.
- Ask the tracking plan owner whether view-to-cart rate counts as a key conversion rate. If it does, review whether this ticket should be rated High.

## Acceptance criteria
- For both Dec 29, 2020 and Jan 2, 2021, one of the following is true:
  - `view_item` counts are restored to at least 0.5 of typical.
  - The low counts are confirmed as real user behavior, with the evidence recorded on this ticket.
- If the counts cannot be restored, reports on product views, view-to-cart rate and product performance by country and platform clearly flag these two days as unreliable.