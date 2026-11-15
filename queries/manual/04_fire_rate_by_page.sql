-- Q: Of all page loads on each page, how often did view_item_list fire?
-- Finding: ~0.03% on the 10 category pages where it fired
--          (71 events / ~247,000 page views). Expected: ~100%.
SELECT
  (SELECT
      value.string_value
    FROM UNNEST(event_params)
    WHERE key = 'page_location') AS page,
  COUNTIF(event_name = 'page_view') AS page_views,
  COUNTIF(event_name = 'view_item_list') AS list_views,
  SAFE_DIVIDE(COUNTIF(event_name = 'view_item_list'), COUNTIF(event_name = 'page_view')) AS fire_rate
FROM `bigquery-public-data.ga4_obfuscated_sample_ecommerce.events_*`
WHERE event_name IN ('view_item_list', 'page_view')
GROUP BY page
ORDER BY list_views DESC
