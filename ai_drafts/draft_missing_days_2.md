# select_item has no data on 22 of 92 days, from Nov 1, 2020 to Nov 22, 2020

**Event:** select_item
**Found by:** · **Date found:** · **Severity:** Medium

## Description
The `select_item` event has no rows on 22 of the 92 days in the data period (Nov 1, 2020 to Jan 31, 2021). All of the days with no data fall in one continuous run, from Nov 1, 2020 to Nov 22, 2020. At least one other event was received on every one of these days, so data for other events was coming in during this time.

Two other events also have no data on some of the same days: `add_to_cart` and `view_item_list`. These events have gaps on other days of the period as well. Gaps on the same days do not prove a shared cause.

The check results do not show whether item selections happened on these days. The gap could mean the event was not tracked, or that the activity did not take place. This has not been confirmed.

## Evidence (Nov 1, 2020 – Jan 31, 2021)
- Check: missing days. An event is flagged for any day in the data period when it has no rows.
- `select_item` has no data on 22 of 92 days: Nov 1, 2020 to Nov 22, 2020.
- `select_item` total events received on the 70 days with data: 31007.
- At least one other event was received on every one of the 22 days with no `select_item` data.
- Events with data on every day of the period: `add_payment_info`, `add_shipping_info`, `begin_checkout`, `click`, `first_visit`, `page_view`, `purchase`, `scroll`, `select_promotion`, `session_start`, `user_engagement`, `view_item`, `view_promotion`, `view_search_results`.
- `add_to_cart` also has no data on 16 of the 22 days: Nov 2, 2020 to Nov 15, 2020 and Nov 21, 2020 to Nov 22, 2020. Across the whole period, `add_to_cart` has no data on 18 days. The check results do not list the dates of its other missing days.
- `view_item_list` also has no data on 6 of the 22 days: Nov 12, 2020 to Nov 14, 2020, Nov 16, 2020 to Nov 17, 2020, and Nov 19, 2020. Across the whole period, `view_item_list` has no data on 59 days. The check results do not list the dates of its other missing days.

## Impact
The tracking plan sets the severity of this problem as Medium.

`select_item` records when a user picks an item. Any analysis that uses this event will have no data from Nov 1, 2020 to Nov 22, 2020. This includes counts of item selections, trends over time, and funnel steps that include selecting an item. If someone compares item selections across the full period, the first 22 days will show nothing. That could look like selections started on a later date, when it may only be when data began arriving.

The 31007 events cover only the 70 days with data. The check results do not show whether those days are complete, so this total should not be treated as a confirmed full count for those days.

Funnel analysis that combines `select_item` with `add_to_cart` or `view_item_list` will be affected further, because those events also have gaps on some of the same days and on other days in the period.

The check results do not give the expected number of `select_item` events per day, so the size of the gap in event volume is unknown.

## Suggested next steps
- Find out whether `select_item` was being tracked before Nov 23, 2020. Was tracking for this event switched on after Nov 22, 2020 as a planned change, or did something stop it from being received during those days?
- Find out whether item selections were possible on the site during Nov 1–22, 2020, given that `view_item` and `page_view` were received on every day.
- Get the dates of the remaining missing days for `add_to_cart` and `view_item_list`, which are not in the check results. Review them alongside the `select_item` gap, without assuming the gaps share a cause.
- If the data for Nov 1–22, 2020 can be pulled again, check whether any `select_item` rows appear for those days.

## Acceptance criteria
- The reason for the `select_item` gap from Nov 1, 2020 to Nov 22, 2020 is confirmed and written down. It should be clear whether the gap is a tracking problem or reflects that no item selections happened.
- If the gap is a tracking problem, `select_item` has rows on every day of the period where it is expected to be tracked. If the data cannot be recovered, the gap is documented, and any analysis using `select_item` starts after Nov 22, 2020.