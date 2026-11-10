# add_to_cart volume low on 6 days and not received at all on Nov 2–15 and Nov 21–24, 2020

**Event:** add_to_cart
**Found by:**  · **Date found:**  · **Severity:** High

## Description
An automated low-volume check flagged the `add_to_cart` event on 6 days between Nov 1, 2020 and Jan 3, 2021. A day is flagged when the event's count is below 0.5 of its typical count. "Typical" means the median count for that weekday.

On two other date ranges, no `add_to_cart` rows were received at all:
- Nov 2, 2020 to Nov 15, 2020
- Nov 21, 2020 to Nov 24, 2020

Most of the flagged days fall in November 2020, either next to or between the no-data ranges. Jan 3, 2021 is a separate flagged day.

The check results show only what was received. They do not show whether customers added items to their carts on these days. They also do not show why the counts are low or absent. Low volume on the flagged days and no data on the other days may or may not share a cause.

## Evidence (Nov 1, 2020 – Jan 3, 2021)
- Nov 1, 2020: 4 events, typical 473, 0.8% of typical.
- Nov 2–15, 2020: no `add_to_cart` data received.
- Nov 16, 2020: 85 events, typical 585, 14.5% of typical.
- Nov 19, 2020: 187 events, typical 642, 29.1% of typical.
- Nov 20, 2020: 15 events, typical 572, 2.6% of typical.
- Nov 21–24, 2020: no `add_to_cart` data received.
- Nov 25, 2020: 297 events, typical 665, 44.7% of typical.
- Jan 3, 2021: 229 events, typical 473, 48.4% of typical.

The check results do not include the following:
- Counts or typical values for Nov 17 and Nov 18, 2020. These days were not flagged, so their counts were at least 0.5 of typical. Whether those days are complete is unknown.
- Typical values for the no-data days.
- Total `add_to_cart` counts for the period.
- Whether other events were also low or absent on the same days.

## Impact
`add_to_cart` is a funnel step. Totals and conversion rates that use it cannot be trusted for the affected dates or for any period that includes them. Examples include add-to-cart rate and cart-to-purchase rate.

During the no-data ranges, the event counts as zero. On the flagged days, the counts are far below typical. Any figures that include these dates may therefore be misleading. This includes November 2020 totals and comparisons between November and other months.

This is rated High because key business numbers (conversion rates built on `add_to_cart`) cannot be trusted for these dates. The tracking plan rates this event High if it stops arriving entirely. On Nov 2–15 and Nov 21–24, 2020, no `add_to_cart` data was received, so High is within the allowed limit.

It is not yet known whether the low and absent counts reflect a tracking problem or a real drop in activity. Until that is confirmed, these dates should not be treated as accurate either way.

## Suggested next steps
- **Check other events on the same days.** For example, check page views and purchases on Nov 1–25, 2020 and Jan 3, 2021. This shows whether the drop affects only `add_to_cart` or the site's tracking more broadly.
- **Look for tracking or site changes.** Find out whether any changes to tracking setup or the add-to-cart flow happened around Nov 1, Nov 16–25, 2020 and Jan 3, 2021.
- **Check for real-world reasons.** A site outage, store closure or holiday could possibly explain some of these days, Jan 3, 2021 in particular. This is unconfirmed.
- **Check whether lost events can be recovered.** Find out whether `add_to_cart` events for the no-data ranges and flagged days can be recovered or reloaded from any source.
- **Pull the missing counts.** Get daily counts for Nov 17–18, 2020 to judge whether the days between the flagged dates are reliable.

## Acceptance criteria
- `add_to_cart` data is received every day, with no day below 0.5 of its weekday median unless a confirmed real-world reason is documented.
- For each affected date, one of the following is true:
  - the data is recovered and the date passes the low-volume check, or
  - the date is documented as unreliable and excluded from `add_to_cart` totals and conversion rates, with the reason recorded.