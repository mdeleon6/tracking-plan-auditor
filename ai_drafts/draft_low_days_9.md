# view_item_list received 25.0% of its typical count on Nov 18, 2020, and has many days with no data

**Event:** view_item_list
**Found by:** · **Date found:** · **Severity:** Low

## Description
An automated low-volume check flagged `view_item_list` on one day. It flags a day when an event's count falls below 0.5 of its typical count. The typical count is the median for that weekday. On Nov 18, 2020, 1 `view_item_list` event was received against a typical count of 4.

The check results also list many days when no `view_item_list` events were received, from Nov 12, 2020 through Jan 31, 2021. These days were not flagged as low-volume days. The check results do not show whether users had no list views on those days or whether events were sent but not received.

The cause of the low count and of the days with no data has not been confirmed. Both appear in the same check results, but that does not mean they share a cause.

## Evidence
- Flagged by the low-volume check (threshold: below 0.5 of the weekday median):
  - Nov 18, 2020: 1 event received, typical 4, 25.0% of typical.
- Number of flagged days: 1.
- Days with no `view_item_list` data in the check results:
  - Nov 12, 2020 to Nov 14, 2020
  - Nov 16, 2020 to Nov 17, 2020
  - Nov 19, 2020
  - Nov 24, 2020 to Nov 25, 2020
  - Nov 29, 2020
  - Dec 2, 2020 to Dec 3, 2020
  - Dec 5, 2020 to Dec 6, 2020
  - Dec 8, 2020 to Dec 9, 2020
  - Dec 13, 2020 to Jan 2, 2021
  - Jan 4, 2021 to Jan 8, 2021
  - Jan 11, 2021 to Jan 15, 2021
  - Jan 17, 2021 to Jan 22, 2021
  - Jan 24, 2021 to Jan 27, 2021
  - Jan 29, 2021 to Jan 31, 2021
- The check results do not include the following:
  - the full date range checked
  - the daily counts on days with data
  - the total `view_item_list` count for the period
  - whether days with no data are included when calculating the weekday median

## Impact
The tracking plan rates this event High if it stops arriving entirely. In the check results, `view_item_list` events continue to arrive on some days through the period, so the check results do not show that the event stopped arriving entirely. This means High is the highest severity allowed here, and the severity is set using the standard rules.

The flagged shortfall is on a single day, with 1 event received against a typical count of 4. Any day-level or weekday analysis of product list views that includes Nov 18, 2020 will show lower activity than usual. The check results cannot tell us whether that drop is real.

`view_item_list` is not a revenue or order event. Based on the flagged day alone, the effect on decisions is likely small, so this is rated Low.

The check results cannot confirm that `view_item_list` totals for the period are correct. They also cannot confirm which reports or funnels use this event. If any conversion rate uses `view_item_list` as a step, the gaps in received events could affect that rate. This is possible and has not been confirmed.

## Suggested next steps
- Find out whether the days with no `view_item_list` data reflect no list views by users or events that were not received.
  - One way is to check whether other events that would normally appear alongside product list views were received on those days.
- Confirm how the weekday median is calculated, including whether days with no data are counted.
  - This affects whether a typical count of 4 is a reliable baseline.
- Check which reports, dashboards or funnels use `view_item_list`, so the effect of the gaps can be understood.
- Look at Nov 18, 2020 for any recorded release, configuration change or outage.
  - Do the same for the start and end of the longer no-data period from Dec 13, 2020 to Jan 2, 2021.

## Acceptance criteria
- The reason for the low count on Nov 18, 2020 is identified and documented, either as real user behavior or as a tracking problem.
- Every listed day with no `view_item_list` data is explained and documented, either as real user behavior or as a tracking problem.
- If a tracking problem is confirmed, the fix is in place and `view_item_list` arrives every day it is expected.
- How the typical count is calculated is documented, so future low-volume flags for this event can be read correctly.