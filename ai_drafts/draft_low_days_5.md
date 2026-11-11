# Click events below half of typical volume on 13 days between Dec 26, 2020 and Jan 31, 2021

**Event:** click
**Found by:** · **Date found:** · **Severity:** Low

## Description
An automated low-volume check flagged the `click` event on 13 days between Dec 26, 2020 and Jan 31, 2021. The check flags a day when an event's count falls below 0.5 of its typical count. The typical count is the median for that weekday. Two flagged days fall in December 2020 and the rest in January 2021.

Typical `click` counts on these days are small, between 8 and 16 events. A drop of a few events can therefore push a day below the threshold.

None of the 13 days has a holiday name in the check results, so none of them is on the tracking plan's holiday calendar.

The check results do not show why volume was lower on these days. They also do not show whether clicks happened and were not received, or whether fewer clicks happened.

## Evidence (Dec 26, 2020 – Jan 31, 2021)
- Dec 26, 2020: 4 events, typical 9, 44.4% of typical
- Dec 27, 2020: 3 events, typical 8, 37.5% of typical
- Jan 11, 2021: 7 events, typical 15, 46.7% of typical
- Jan 13, 2021: 3 events, typical 13, 23.1% of typical
- Jan 17, 2021: 1 event, typical 8, 12.5% of typical
- Jan 19, 2021: 2 events, typical 16, 12.5% of typical
- Jan 20, 2021: 5 events, typical 13, 38.5% of typical
- Jan 21, 2021: 5 events, typical 11, 45.5% of typical
- Jan 22, 2021: 4 events, typical 15, 26.7% of typical
- Jan 25, 2021: 5 events, typical 15, 33.3% of typical
- Jan 27, 2021: 4 events, typical 13, 30.8% of typical
- Jan 30, 2021: 4 events, typical 9, 44.4% of typical
- Jan 31, 2021: 3 events, typical 8, 37.5% of typical

`click` was also below the threshold on 5 more days when many events dropped together. Those days are not part of this ticket and are covered in a separate multi-event ticket:
- Dec 24, 2020 (Christmas Eve, widely observed)
- Dec 25, 2020 (Christmas Day, widely observed)
- Jan 1, 2021 (New Year's Day, widely observed)
- Jan 4, 2021
- Jan 18, 2021 (Martin Luther King Jr. Day, US only)

For those named days, the holiday is a possible, unconfirmed explanation only. It does not apply to the 13 days in this ticket.

Some information is missing from the check results:
- The full date range the check covered
- `click` counts on days that were not flagged
- Total `click` counts for the period
- Whether the 13 days share anything in common with the multi-event days

## Impact
Daily and weekly `click` counts for the 13 flagged days may read lower than expected. Any trend, comparison or rate built on `click` that includes these days may be affected. The check results do not show whether `click` data on other days is complete.

Severity is Low. The tracking plan rates this event as Low if it stopped arriving entirely. This is a partial drop, not a full stop, so Low is the highest severity allowed. It is not raised above that.

## Suggested next steps
- For each of the 13 days, find out whether `click` events were sent but not received, or whether fewer clicks took place.
- Check whether any tracking, site or app changes were made on or around these dates. Any link to the drops is unconfirmed until checked.
- Compare these 13 days with the findings of the separate multi-event ticket. Do not assume the drops share a cause.
- Because typical counts are small, review whether this threshold is a useful way to judge `click` volume. Agree on how flags like these should be handled.

## Acceptance criteria
- Each of the 13 flagged days is either explained, as real lower activity or as events not received, or fixed so that the `click` count is at least 0.5 of its typical count.
- Any confirmed cause and any fix are documented on this ticket, along with which days they apply to.