# Low volume in 13 events across 7 days from Dec 24, 2020 to Jan 18, 2021, including purchase and checkout events

**Event:** multiple events (13)
**Found by:** · **Date found:** · **Severity:** High

## Description
An automated check flags days when at least 5 events each arrive at below 0.5 of their typical count. The typical count is the median for that weekday. The check flagged 7 days and 13 different events. On these days, several events arrived at well under half their usual volume.

Checkout and purchase events appear on most of the listed days. `add_payment_info`, `add_shipping_info` and `view_item` are below the threshold on all 7 days. `purchase` is below the threshold on every listed day except Dec 30, 2020.

Five of the 7 days have a holiday name next to them in the tracking plan's holiday calendar. These holidays are a possible explanation for lower activity, but this is unconfirmed. Dec 30, 2020 and Jan 4, 2021 have no holiday name and are not on that calendar.

The check results do not show whether these drops reflect real changes in user activity or data that was not received. The low counts may come from either.

## Evidence (Dec 24, 2020 – Jan 18, 2021)
Each event's count is shown as a percentage of its typical count.

- **Dec 24, 2020** (Christmas Eve, widely observed as a day off): 8 events below threshold
  - `add_payment_info` 34.6%, `add_shipping_info` 32.3%, `click` 27.3%, `page_view` 45.3%, `purchase` 42.6%, `user_engagement` 43.0%, `view_item` 46.1%, `view_promotion` 46.4%
- **Dec 25, 2020** (Christmas Day, widely observed as a day off): 9 events below threshold
  - `add_payment_info` 24.9%, `add_shipping_info` 25.3%, `click` 46.7%, `page_view` 37.9%, `purchase` 21.5%, `scroll` 37.2%, `user_engagement` 35.0%, `view_item` 31.4%, `view_promotion` 37.7%
- **Dec 30, 2020** (not on the holiday calendar): 5 events below threshold
  - `add_payment_info` 32.1%, `add_shipping_info` 37.5%, `user_engagement` 42.8%, `view_item` 35.0%, `view_promotion` 45.7%
- **Dec 31, 2020** (New Year's Eve, widely observed as a day off): 9 events below threshold
  - `add_payment_info` 44.1%, `add_shipping_info` 43.1%, `purchase` 46.3%, `scroll` 41.1%, `select_item` 39.9%, `select_promotion` 46.7%, `user_engagement` 36.5%, `view_item` 33.3%, `view_promotion` 39.6%
- **Jan 1, 2021** (New Year's Day, widely observed as a day off): 10 events below threshold
  - `add_payment_info` 17.5%, `add_shipping_info` 20.1%, `begin_checkout` 42.3%, `click` 13.3%, `purchase` 17.7%, `scroll` 35.4%, `user_engagement` 34.3%, `view_item` 28.7%, `view_promotion` 38.5%, `view_search_results` 49.7%
- **Jan 4, 2021** (not on the holiday calendar): 5 events below threshold
  - `add_payment_info` 36.2%, `add_shipping_info` 28.9%, `click` 20.0%, `purchase` 30.2%, `view_item` 44.8%
- **Jan 18, 2021** (Martin Luther King Jr. Day, observed as a day off in the US only): 5 events below threshold
  - `add_payment_info` 31.9%, `add_shipping_info` 35.5%, `click` 40.0%, `purchase` 35.8%, `view_item` 41.3%

**Information missing from the check results:**
- The actual event counts and the typical (median) counts behind the percentages.
- The full date range the check covered.
- Any breakdown by region, platform or other dimension.

## Impact
The tracking plan rates `add_payment_info`, `add_shipping_info`, `begin_checkout` and `purchase` as High, but only if they stop arriving entirely. None of these events stopped arriving on the listed days, so that rating does not apply directly. It sets the highest severity this ticket can have.

Using the general rules, this ticket is rated High:
- The affected events include `purchase` and the checkout steps leading to it. Order counts, revenue and checkout conversion rates are built on these events.
- If the low volume comes from data not being received, these key numbers are understated on the listed days.
- The check results cannot rule this out, so totals for these days cannot be trusted until the cause is confirmed.

Even if the drops reflect real user behavior, the listed days will stand out in any daily trend or comparison. Analysts need to know whether to treat them as real activity or as data gaps.

## Suggested next steps
- **Compare `purchase` counts with an independent record of orders.** Do this for each listed day, using a record that does not rely on this tracking, if one exists. This would show whether purchases were lost from tracking or were truly lower.
- **Look into Dec 30, 2020 and Jan 4, 2021 first.** These days are not on the holiday calendar, so no holiday is available as a possible explanation.
- **Split Jan 18, 2021 by region, if that data is available.** Martin Luther King Jr. Day is observed as a day off in the US only. Check whether the drop is concentrated in US traffic or appears across all regions.
- **Get the missing figures.** Pull the actual and typical counts for each affected event on each listed day so the size of the drop is known.
- **Re-check the listed days for late-arriving data.** Confirm whether the counts have changed since the check ran.
- **Check for tracking or release changes.** Look for any tracking changes, releases or outages recorded near the listed days.

## Acceptance criteria
- For each of the 7 listed days, there is a documented finding on whether the low volume reflects real activity or data that was not received.
- `purchase` counts on the listed days are reconciled against an independent order record, or a documented reason is given for why this cannot be done.
- If any data was not received, it is either recovered or the affected days and events are clearly flagged for anyone using these numbers.