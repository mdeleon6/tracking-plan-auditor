# view_item_list received 1 event on Nov 18, 2020 (25.0% of typical), and no data on many days from Nov 12, 2020 to Jan 31, 2021

**Event:** view_item_list
**Found by:** · **Date found:** · **Severity:** Medium

## Description
The low volume check flagged one day for the `view_item_list` event. On Nov 18, 2020, 1 event was received, while the typical count is 4. That is 25.0% of typical. The check flags a day when its count falls below 0.5 of the typical count, which is the median for the same weekday.

The check results also list many dates with no `view_item_list` data at all. These run from Nov 12, 2020 to Jan 31, 2021 and include an unbroken stretch from Dec 13, 2020 to Jan 2, 2021. Nov 18 falls directly between two no-data periods: Nov 16–17, 2020 and Nov 19, 2020.

The check results do not say whether these low and empty days reflect real user behavior or a tracking problem. Receiving no rows does not show whether product lists were actually viewed on those days.

## Evidence
- Flagged day: Nov 18, 2020, 1 event received against a typical count of 4 (25.0% of typical).
- Number of flagged days: 1.
- Days with no `view_item_list` data:
  - Nov 12 – Nov 14, 2020
  - Nov 16 – Nov 17, 2020
  - Nov 19, 2020
  - Nov 24 – Nov 25, 2020
  - Nov 29, 2020
  - Dec 2 – Dec 3, 2020
  - Dec 5 – Dec 6, 2020
  - Dec 8 – Dec 9, 2020
  - Dec 13, 2020 – Jan 2, 2021
  - Jan 4 – Jan 8, 2021
  - Jan 11 – Jan 15, 2021
  - Jan 17 – Jan 22, 2021
  - Jan 24 – Jan 27, 2021
  - Jan 29 – Jan 31, 2021
- Nov 18, 2020 has no holiday name in the check results, so it is not on the tracking plan's holiday calendar. The no-data date ranges were not checked against the calendar.
- The check results do not include the following:
  - the start and end dates of the period the check covered
  - the total number of `view_item_list` events in that period
  - the event counts for days that were not flagged

## Impact
The typical daily count for this event is 4, so a single low day such as Nov 18 changes the numbers by only a few events. The larger concern is the long list of dates with no data. If those gaps come from tracking loss rather than real behavior, any analysis of product list views will be incomplete over this period. That includes list view trends and any funnel step that starts from a list view. This has not been confirmed.

The tracking plan rates this event High if it stops arriving entirely. The event did not stop entirely, because data was received on dates between the no-data periods. For that reason, the High rating is treated as the ceiling and is not applied directly.

The severity is Medium rather than High because revenue and order counts are not measured by this event. The problem affects analysis that depends on product list views. That analysis cannot be relied on for this period until the gaps are explained.

## Suggested next steps
- Confirm whether `view_item_list` was expected to fire on every day from Nov 12, 2020 to Jan 31, 2021. For example, check whether the event was live on all relevant pages throughout this period.
- Check whether a typical count of 4 per day means that days with zero events are normal for this event. Treat this only as a possible, unconfirmed explanation.
- Compare the no-data dates, especially Dec 13, 2020 – Jan 2, 2021, against release or tracking change records to see whether any change lines up with them. Matching dates alone would not confirm a cause.
- Obtain the missing figures listed in Evidence, so the size of the gaps can be judged against the full period.

## Acceptance criteria
- Nov 18, 2020 and each no-data date range have a documented explanation. Each explanation either confirms real user behavior or identifies a tracking issue.
- If a tracking issue is confirmed, the fix is in place, and any data that can be recovered for the affected dates is restored.
- Analyses that use `view_item_list` for Nov 12, 2020 – Jan 31, 2021 note these gaps until they are resolved.