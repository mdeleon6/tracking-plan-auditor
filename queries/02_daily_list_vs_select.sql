-- Q: Per day, how often did view_item_list and select_item fire?
-- COUNTIF (not WHERE) keeps every day, so days with zero events still show up.
-- Finding: select_item is 0 until 2020-11-23 (added mid-period);
--          view_item_list stays at 0-8 per day the whole time.
SELECT
  event_date,
  COUNTIF(event_name = 'view_item_list') AS view_item_list,
  COUNTIF(event_name = 'select_item') AS select_item
FROM `bigquery-public-data.ga4_obfuscated_sample_ecommerce.events_*`
GROUP BY event_date
ORDER BY event_date ASC
