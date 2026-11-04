# view_item_list fires on ~0.03% of category page loads (trigger issue)

**Event:** view_item_list
**Found by:** Martino DeLeon · **Date found:** 2026-11-04 · **Severity:** High

## Description
`view_item_list` is implemented, but only fires on ~0.03% of page loads. The trigger for this event seems to not be working properly.

## Evidence (Nov 1, 2020 – Jan 31, 2021)
- `view_item_list` fired 71 times; `select_item` fired 31,007 times. (Users can't select from a list that never loaded.)
- Across the 10 category pages where it fired, `view_item_list` fired on ~0.03% of page loads (71 events / ~247,000 page views). Expected: ~100%, since every category page shows a product list.
- Worst example: YouTube brand page, 1 event in 40,360 page views.
- Queries: [`queries/02_daily_list_vs_select.sql`](../queries/02_daily_list_vs_select.sql), [`queries/04_fire_rate_by_page.sql`](../queries/04_fire_rate_by_page.sql)

## Impact
Product-list click-through rate (`select_item` ÷ `view_item_list`) can't be calculated, so we can't tell which category pages drive product clicks.

## Suggested next steps
- Check the `view_item_list` trigger on category page templates (does it fire before the list loads? is the condition wrong?).
- Verify the fix in GA4 DebugView on several category pages.

## Acceptance criteria
- `view_item_list` fires on every category page load.
- Daily `view_item_list` volume is higher than `select_item`.