-- Q: What share of add_to_cart events have a product with quantity, by day?

WITH per_event AS (
  SELECT
    event_date,
    (SELECT COUNTIF(item.quantity IS NOT NULL) FROM UNNEST(items) AS item) AS items_with_quantity
  FROM `bigquery-public-data.ga4_obfuscated_sample_ecommerce.events_*`
  WHERE event_name = 'add_to_cart'
)
SELECT
  event_date,
  COUNT(*) AS add_to_cart_events,
  COUNTIF(items_with_quantity = 1) AS events_with_quantity
FROM per_event
GROUP BY event_date
ORDER BY event_date ASC