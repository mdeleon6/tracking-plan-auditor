# `view_item_list` received 1 event on Nov 18, 2020, 25.0% of its typical count

**Event:** view_item_list
**Found by:** · **Date found:** · **Severity:** Low

## Description
An automated low-volume check flagged one day for the `view_item_list` event. On Nov 18, 2020, 1 event was received. The typical count for that day is 4, so the day reached 25.0% of typical.

The check flags a day when an event's count is below 0.5 of its typical count. "Typical" means the median count for that weekday.

The check results do not show why the count was low. Fewer events received on a day does not prove whether fewer list views actually happened or whether events were not recorded. Nov 18, 2020 is not on the holiday calendar in the tracking plan.

## Evidence
- Check: low volume, `view_item_list`.
- Number of flagged days: 1.
- Nov 18, 2020: 1 event received, typical 4, 25.0% of typical.
- Nov 18, 2020 has no holiday name in the check results, so it is not on the tracking plan's holiday calendar.
- The check results also list many days with no `view_item_list` data at all between Nov 12, 2020 and Jan 31, 2021. This includes Nov 17, 2020 and Nov 19, 2020, the days directly before and after the flagged day. Those days are covered in a separate missing-day ticket and are not part of this one. It has not been confirmed whether the low count on Nov 18 and the days with no data have anything in common.

## Impact
According to the tracking plan, `view_item_list` is used in product list views and in the list-to-product funnel step. Counts and funnel figures that include Nov 18, 2020 may be understated for that day. The check results do not give a number for how many events may be missing.

This is rated Low because it affects a single day with a small number of events. That is unlikely to change any decision on its own. No key business number such as revenue, orders, units sold or overall conversion rate is shown to depend on this one day.

The tracking plan rates this event High if it stopped arriving entirely. That rating does not apply here, because events were still received on Nov 18, 2020. The days with no data are rated in their own ticket.

## Suggested next steps
- Confirm whether the low count on Nov 18, 2020 reflects real activity or events that were not recorded. Use a source outside this event's tracking if one exists.
- Confirm how many weeks the typical count of 4 is based on. At volumes this small, a drop to 1 event may be ordinary variation rather than a tracking problem. Consider whether the 0.5 threshold is useful for this event.
- Once the separate missing-day ticket is investigated, check whether its findings also explain Nov 18, 2020. Do not assume a shared cause until this is confirmed.

## Acceptance criteria
- The low count on Nov 18, 2020 is either confirmed as real activity or traced to a tracking issue, and the finding is recorded on this ticket.
- If it is a tracking issue and the data can be recovered, the corrected count for Nov 18, 2020 is recorded. If it cannot be recovered, the list-to-product funnel reporting notes that Nov 18, 2020 is incomplete.