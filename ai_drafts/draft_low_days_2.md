# `add_payment_info` fell below half its typical daily count on 10 days between Dec 26, 2020 and Jan 13, 2021

**Event:** add_payment_info
**Found by:** · **Date found:** · **Severity:** High

## Description
The `add_payment_info` event arrived in much lower numbers than usual on 10 days between Dec 26, 2020 and Jan 13, 2021. An automated low-volume check flags a day when an event's count is below 0.5 of its typical count. The typical count is the median for that weekday. On each of the 10 flagged days, the count was below that threshold, with the lowest at 31.5% of typical on Jan 2, 2021.

The check results show only how many events were received. They do not show whether checkout activity really dropped on these days or whether events were lost in tracking. The cause has not been confirmed.

The same event was also below the threshold on 7 more days when many events dropped together. Those days are covered in a separate multi-event ticket and are not part of this one.

## Evidence (Dec 26, 2020 – Jan 13, 2021)
- Check used: low volume. A day is flagged when the event's count is below 0.5 of its typical count (the median for that weekday).
- Number of flagged days: 10.
- Dec 26, 2020: 40 events, typical 89, 44.9% of typical
- Dec 29, 2020: 67 events, typical 168, 39.9% of typical
- Jan 2, 2021: 28 events, typical 89, 31.5% of typical
- Jan 3, 2021: 33 events, typical 73.5, 44.9% of typical
- Jan 5, 2021: 58 events, typical 168, 34.5% of typical
- Jan 6, 2021: 93 events, typical 193, 48.2% of typical
- Jan 7, 2021: 67 events, typical 136, 49.3% of typical
- Jan 8, 2021: 81 events, typical 189, 42.9% of typical
- Jan 9, 2021: 42 events, typical 89, 47.2% of typical
- Jan 13, 2021: 92 events, typical 193, 47.7% of typical
- None of the 10 flagged days has a holiday name in the check results. This means none of these dates is on the tracking plan's holiday calendar. The date range as a whole was not checked against the calendar.
- The 7 days covered in the separate multi-event ticket are Dec 24, 2020 (Christmas Eve: widely observed), Dec 25, 2020 (Christmas Day: widely observed), Dec 30, 2020, Dec 31, 2020 (New Year's Eve: widely observed), Jan 1, 2021 (New Year's Day: widely observed), Jan 4, 2021, and Jan 18, 2021 (Martin Luther King Jr. Day: US only).
- The check results do not include:
  - counts for other checkout events, such as checkout starts or purchases, on the same days
  - any split by country or platform
  - a total of missing events across the period

## Impact
According to the tracking plan, `add_payment_info` is used in the checkout funnel and in checkout conversion rate by country and platform. Checkout conversion rate is a key business number.

If the low counts on these 10 days come from lost tracking rather than real customer behavior, then the checkout funnel and checkout conversion rates for these days cannot be trusted. Because the counts are less than half of typical, the effect would be large. This is the reason for rating this ticket High.

If the drop reflects real behavior, the numbers would be accurate. The check results cannot tell these two cases apart. Until that is resolved, conversion figures that include these days should be treated with caution.

The tracking plan rates this event High if it stopped arriving entirely. That rating covers a full stop, which is not what happened here. The High severity on this ticket is based on the effect on checkout conversion rate described above.

Possible, unconfirmed context: several of the separate multi-event days fall within the same date range and carry holiday names from the calendar. Christmas Eve, Christmas Day, New Year's Eve and New Year's Day are listed as widely observed, and Martin Luther King Jr. Day is listed as US only. It has not been confirmed whether these holidays have any connection to the lower counts on the 10 days in this ticket, none of which is on the holiday calendar.

## Suggested next steps
- Compare `add_payment_info` counts on the 10 flagged days with the steps just before and after it in the checkout funnel.
  - If the earlier and later steps dropped by a similar amount, that would point toward real behavior.
  - If only `add_payment_info` dropped, that would point toward a tracking issue.
- Break the flagged days down by country and platform, since the checkout conversion rate is reported that way. Check whether the drop is concentrated in one country, one platform or one app version.
- Ask the team that owns checkout tracking whether any change was released to the payment step or its tracking around Dec 26, 2020. Ask the same about any later change that might explain the recovery after Jan 13, 2021.
- Coordinate with the owner of the separate multi-event ticket so the 7 shared days and these 10 days are investigated together. Problems appearing in the same period do not prove a shared cause.

## Acceptance criteria
- Each of the 10 flagged days is marked with a confirmed explanation: either real lower checkout activity, or a tracking issue.
- If a tracking issue is confirmed, the fix is in place and any recoverable events are restored. If events cannot be restored, the affected days are clearly marked in the checkout funnel and checkout conversion rate reports.
- After any fix, `add_payment_info` daily counts are not flagged by the low-volume check unless the flag has a confirmed explanation.