# add_shipping_info below half of typical volume on 12 days between Dec 26, 2020 and Jan 15, 2021

**Event:** add_shipping_info
**Found by:** · **Date found:** · **Severity:** High

## Description
The `add_shipping_info` event was flagged by the low-volume check on 12 days between Dec 26, 2020 and Jan 15, 2021. The check flags a day when an event's count falls below 0.5 of its typical count, where "typical" means the median count for that weekday. On each flagged day, `add_shipping_info` arrived at between 32.4% and 49.4% of its typical count.

The event did not stop arriving on any flagged day. Every flagged day still has events.

None of these 12 dates has a holiday name next to it in the check results, so none of them is on the tracking plan's holiday calendar.

The check results show that `add_shipping_info` was also below threshold on 7 more days in this period. On those days many events dropped together, so they are covered in a separate multi-event ticket and are not part of this one.

## Evidence (Dec 26, 2020 – Jan 15, 2021)
- Dec 26, 2020: 48 events, typical 148, 32.4% of typical
- Dec 28, 2020: 101 events, typical 211, 47.9% of typical
- Dec 29, 2020: 80 events, typical 233, 34.3% of typical
- Jan 2, 2021: 48 events, typical 148, 32.4% of typical
- Jan 3, 2021: 51 events, typical 129.5, 39.4% of typical
- Jan 5, 2021: 88 events, typical 233, 37.8% of typical
- Jan 6, 2021: 116 events, typical 248, 46.8% of typical
- Jan 8, 2021: 105 events, typical 269, 39.0% of typical
- Jan 9, 2021: 58 events, typical 148, 39.2% of typical
- Jan 10, 2021: 58 events, typical 129.5, 44.8% of typical
- Jan 11, 2021: 94 events, typical 211, 44.5% of typical
- Jan 15, 2021: 133 events, typical 269, 49.4% of typical
- The following days were also below threshold but are covered in the separate multi-event ticket:
  - Dec 24, 2020 (Christmas Eve: widely observed)
  - Dec 25, 2020 (Christmas Day: widely observed)
  - Dec 30, 2020
  - Dec 31, 2020 (New Year's Eve: widely observed)
  - Jan 1, 2021 (New Year's Day: widely observed)
  - Jan 4, 2021
  - Jan 18, 2021 (Martin Luther King Jr. Day: US only)

The check results do not include the following information:
- Counts for other checkout-step events on these 12 days.
- Any breakdown by country or platform.
- Counts for days in this period that were not flagged.

## Impact
According to the tracking plan, `add_shipping_info` is used in the checkout funnel and in checkout conversion rate by country and platform.

The check results only show how many events were received. They do not show whether fewer users actually added shipping info or whether events were sent but not received. Until that is known, the checkout funnel and checkout conversion rate cannot be trusted for these 12 days. Conversion rate is a key business number, which is why this ticket is rated High.

The tracking plan rates this event High if it stops arriving entirely. The event did not stop arriving. That rating is therefore used only as the highest severity allowed, and this ticket stays within it.

The holidays named in the check results fall on the separately ticketed days, not on the 12 days in this ticket. Holidays observed near this period (Christmas Eve, Christmas Day, New Year's Eve and New Year's Day, all widely observed) are a possible, unconfirmed explanation for lower activity around these dates. This has not been confirmed. The check results give no cause for the drop.

## Suggested next steps
- Compare `add_shipping_info` on the 12 flagged days with the checkout steps immediately before and after it. If those steps show a similar drop, that would point toward a real change in user activity. If only this event dropped, that would point toward a tracking issue.
- Split the flagged days by country and platform, since the conversion rate is reported on those dimensions. Check whether the drop is limited to one country or platform, or applies to all of them.
- Find out whether any release or tracking change affecting `add_shipping_info` happened between Dec 26, 2020 and Jan 15, 2021.
- Check whether events for these dates can arrive late. If they can, check whether a later re-pull changes the counts.

## Acceptance criteria
- For each of the 12 flagged days, there is a documented finding. The finding states either that the low count reflects real user activity, or that it reflects a tracking gap with its confirmed cause.
- If a tracking gap is confirmed, one of the following is true:
  - The counts for the affected days are restored and no longer fall below 0.5 of typical.
  - Checkout funnel and checkout conversion rate reports exclude or clearly mark those days.