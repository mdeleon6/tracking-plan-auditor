-- Q: On which pages did the 71 view_item_list events fire?
-- page_location lives inside event_params, so UNNEST it with a subquery.
-- Finding: every page is a category page (where the event should fire).
SELECT
  (SELECT
      value.string_value
    FROM UNNEST(event_params)
    WHERE key = 'page_location') AS page,
  COUNT(*) AS views
FROM `bigquery-public-data.ga4_obfuscated_sample_ecommerce.events_*`
WHERE event_name = 'view_item_list'
GROUP BY page
ORDER BY views DESC
