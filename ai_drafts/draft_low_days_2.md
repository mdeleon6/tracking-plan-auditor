# add_payment_info fell below half its typical daily count on 10 days between Dec 26, 2020 and Jan 13, 2021

**Event:** add_payment_info
**Found by:** · **Date found:** · **Severity:** High

## Description
The `add_payment_info` event was flagged by a low-volume check on 10 days between Dec 26, 2020 and Jan 13, 2021. The check flags a day when the event's count is below 0.5 of its typical count. "Typical" means the median count for that weekday.

On the 10 flagged days, the count ranged from 31.5% to 49.3% of typical. The check results show only what was received. They do not show whether fewer users added payment info on these days or whether events were sent but not received. Either is possible, and neither is confirmed.

None of the 10 dates in this ticket has a holiday name next to it in the check results.

The same event was also below threshold on 7 other days when many events dropped together. Those days are covered in a separate multi-event ticket and are not part of this one.

## Evidence (Dec 26, 2020 – Jan 13, 2021)
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
- Covered separately in the multi-event ticket (not in scope here):
  - Dec 24, 2020 (Christmas Eve: widely observed)
  - Dec 25, 2020 (Christmas Day: widely observed)
  - Dec 30, 2020
  - Dec 31, 2020 (New Year's Eve: widely observed)
  - Jan 1, 2021 (New Year's Day: widely observed)
  - Jan 4, 2021
  - Jan 18, 2021 (Martin Luther King Jr. Day: US only)
- Not in the check results:
  - total `add_payment_info` count for the period
  - counts split by country or platform
  - counts for other checkout funnel events on the same days

## Impact
According to the tracking plan, `add_payment_info` is used in the checkout funnel and in the checkout conversion rate by country and platform.

If some events on these days were sent but not received, the following numbers for the affected days cannot be trusted:
- the funnel step counts
- the conversion rates that depend on this step

The check results cannot show whether this happened.

Severity is set to High because checkout conversion rate is a key business number and could be wrong for these 10 days. The tracking plan rates this event High if it stopped arriving entirely. The event did not stop arriving here, so that rating serves only as the upper limit. The High rating comes from the effect on conversion rates.

The check results do not say whether every country and platform is affected or only some. The country and platform breakdowns may be affected unevenly.

## Suggested next steps
- Compare the 10 flagged days with the other checkout funnel steps on the same days.
  - Did the steps before and after `add_payment_info` also drop?
  - Or did only this step drop?
- Break down `add_payment_info` counts on the flagged days by country and platform. This shows whether the drop is spread evenly or concentrated in one segment.
- Check whether any change to checkout, payment or tracking code was released on or shortly before Dec 26, 2020. Also check whether anything changed around Jan 13, 2021, the last flagged day.
  - This is a question to answer, not a confirmed cause.
- Confirm with the owners of the multi-event ticket whether their findings explain any of these 10 days. Appearing in the same period does not prove a shared cause.

## Acceptance criteria
- Each of the 10 flagged days is classified as one of the following, with the supporting evidence recorded:
  - confirmed real user behavior
  - confirmed data loss
- For any day confirmed as data loss, the data is either corrected or clearly marked as unreliable for:
  - the checkout funnel
  - the checkout conversion rate by country and platform
- Analysts using checkout conversion rates for Dec 26, 2020 to Jan 13, 2021 are informed of the outcome.