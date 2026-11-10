# 13 events fell below half their typical count on 7 days between Dec 24, 2020 and Jan 18, 2021, including purchase and checkout events

**Event:** multiple events (13)
**Found by:** · **Date found:** · **Severity:** High

## Description
On 7 days between Dec 24, 2020 and Jan 18, 2021, at least 5 events each arrived at less than half their typical count. The typical count is the median for that weekday. 13 different events were affected. They include the checkout and purchase events `add_payment_info`, `add_shipping_info`, `begin_checkout` and `purchase`, which the tracking plan rates High if they stop arriving entirely.

`add_payment_info` and `add_shipping_info` are below the threshold on every listed day. `purchase` is below the threshold on every listed day except Dec 30, 2020. The lowest values are on Jan 1, 2021, when 10 events were below the threshold.

The check results do not show whether these drops reflect real changes in user activity or a loss of tracked events. Several events dropping on the same days does not prove they share a cause.

## Evidence (Dec 24, 2020 – Jan 18, 2021)
- Check rule: a day is listed when at least 5 events are each below 0.5 of their typical count, which is the median for that weekday.
- Days listed: 7. Different events affected: 13.
- Dec 24, 2020: 8 events below threshold: `add_payment_info` 34.6%, `add_shipping_info` 32.3%, `click` 27.3%, `page_view` 45.3%, `purchase` 42.6%, `user_engagement` 43.0%, `view_item` 46.1%, `view_promotion` 46.4%.
- Dec 25, 2020: 9 events below threshold: `add_payment_info` 24.9%, `add_shipping_info` 25.3%, `click` 46.7%, `page_view` 37.9%, `purchase` 21.5%, `scroll` 37.2%, `user_engagement` 35.0%, `view_item` 31.4%, `view_promotion` 37.7%.
- Dec 30, 2020: 5 events below threshold: `add_payment_info` 32.1%, `add_shipping_info` 37.5%, `user_engagement` 42.8%, `view_item` 35.0%, `view_promotion` 45.7%.
- Dec 31, 2020: 9 events below threshold: `add_payment_info` 44.1%, `add_shipping_info` 43.1%, `purchase` 46.3%, `scroll` 41.1%, `select_item` 39.9%, `select_promotion` 46.7%, `user_engagement` 36.5%, `view_item` 33.3%, `view_promotion` 39.6%.
- Jan 1, 2021: 10 events below threshold: `add_payment_info` 17.5%, `add_shipping_info` 20.1%, `begin_checkout` 42.3%, `click` 13.3%, `purchase` 17.7%, `scroll` 35.4%, `user_engagement` 34.3%, `view_item` 28.7%, `view_promotion` 38.5%, `view_search_results` 49.7%.
- Jan 4, 2021: 5 events below threshold: `add_payment_info` 36.2%, `add_shipping_info` 28.9%, `click` 20.0%, `purchase` 30.2%, `view_item` 44.8%.
- Jan 18, 2021: 5 events below threshold: `add_payment_info` 31.9%, `add_shipping_info` 35.5%, `click` 40.0%, `purchase` 35.8%, `view_item` 41.3%.
- The check results only give percentages. The following are missing: the actual event counts, the typical counts, and any revenue figures for these days.
- Some events may also have dropped on these days without falling below the threshold. Those events would not appear in the check results. Days with fewer than 5 events below the threshold are not listed either.

## Impact
The tracking plan rates `add_payment_info`, `add_shipping_info`, `begin_checkout` and `purchase` as High if they stop arriving entirely. None of them stopped entirely on the listed days, because every value in the check results is above 0%. The tracking plan rating is therefore the highest severity allowed here, and the severity was chosen using the general rules.

The severity is High because `purchase` and the checkout events are below half their typical count on most listed days. The check results cannot show whether those counts are complete. Until that is confirmed, these key business numbers on the affected days cannot be trusted:
- order totals
- revenue based on `purchase`
- checkout conversion rates

If the drops are real changes in user activity, the numbers are accurate. If they come from lost events, the numbers understate activity. The check results do not show which is true.

Several listed days are close to holidays: Dec 24, Dec 25, Dec 31 and Jan 1. This is a possible explanation for lower activity on those days, but it is unconfirmed. It also would not explain Dec 30, Jan 4 or Jan 18 without further checking.

## Suggested next steps
- Compare `purchase` counts on the 7 listed days against an independent record of orders, if one exists, to see whether orders are missing from tracking.
- Check whether any tracking, site or release changes happened on or around Dec 30, 2020, Jan 4, 2021 and Jan 18, 2021, which are not near the holidays.
- Get the actual counts and typical counts behind the percentages, so the size of each drop is known.
- Check whether events not listed by the check also dropped on these days, without falling below the threshold.

## Acceptance criteria
- For each of the 7 listed days, it is documented whether the drop in `purchase` and checkout events reflects real activity or lost events. The documentation includes the evidence used.
- If events were lost, the affected days and events are documented. Analyses using those days either exclude them or carry a note that the counts are incomplete.
- Actual counts and typical counts for the affected events on the listed days are recorded alongside the percentages.