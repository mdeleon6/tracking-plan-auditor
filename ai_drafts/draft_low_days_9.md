# view_item_list count was 25.0% of typical on Nov 18, 2020

**Event:** view_item_list
**Found by:** · **Date found:** · **Severity:** Low

## Description
On Nov 18, 2020, the `view_item_list` event received 1 event. Its typical count for that day is 4, so the day was at 25.0% of typical. The low-volume check flags a day when an event's count falls below 0.5 of its typical count. The typical count is the median for that weekday. This is the only flagged day for this event.

Nov 18, 2020 falls between days with no data at all: Nov 16 to Nov 17, 2020 and Nov 19, 2020. Those no-data days are covered in a separate missing-day ticket and are not part of this one. It is possible, but not confirmed, that the low count on Nov 18 is related to them.

The check results do not list a holiday for Nov 18, 2020.

## Evidence
- Check: low volume. A day is flagged when the count is below 0.5 of the typical count, which is the median for that weekday.
- Nov 18, 2020: 1 event, typical 4, 25.0% of typical.
- Number of flagged days for `view_item_list`: 1.
- No query or supporting file was included in the check results.

## Impact
According to the tracking plan, `view_item_list` is used in product list views and in the list-to-product funnel step. For Nov 18, 2020, the product list view count and the list-to-product funnel step may be understated. The check results only show what was received. They cannot show whether fewer list views happened that day or whether some were not recorded.

**Severity reasoning:** The tracking plan rates this event High if it stopped arriving entirely. That rating does not apply here, because this ticket covers one low day with some events received. The flagged day is a single day with a small count, so it is unlikely to change a decision on its own. That is why this ticket is Low rather than Medium or High. The no-data days for this event are handled in the separate missing-day ticket. If that ticket shows a wider tracking problem, this day should be reviewed as part of it.

## Suggested next steps
- Find out whether the single event on Nov 18, 2020 reflects actual list views or a partial loss of tracking.
- Check other events on Nov 18, 2020 to see whether they also show low counts. This would help tell whether the drop is limited to `view_item_list`.
- Coordinate with the owner of the separate missing-day ticket. Nov 18 sits between no-data days on Nov 16–17 and Nov 19, so it could be checked alongside them.

## Acceptance criteria
- The Nov 18, 2020 count for `view_item_list` is either confirmed as real behavior or corrected through a re-pull.
- If the data is re-pulled, the Nov 18, 2020 count no longer falls below 0.5 of its typical count, or the remaining gap is explained and documented.
- Any analysis of product list views or the list-to-product funnel step that includes Nov 18, 2020 notes this day as flagged until the item is resolved.