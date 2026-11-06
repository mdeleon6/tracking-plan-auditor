-- Q: How many products in each add_to_cart event have quantity filled in?

WITH per_event AS (
  SELECT
    (SELECT COUNTIF(item.quantity IS NOT NULL) FROM UNNEST(items) AS item) AS items_with_quantity
  FROM `bigquery-public-data.ga4_obfuscated_sample_ecommerce.events_*`
  WHERE event_name = 'add_to_cart'
)
SELECT
  items_with_quantity,
  COUNT(*) AS events
FROM per_event
GROUP BY items_with_quantity
ORDER BY items_with_quantity ASC