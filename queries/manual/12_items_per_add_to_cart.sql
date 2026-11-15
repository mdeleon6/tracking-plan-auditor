-- Q: How many products does each add_to_cart event carry?

SELECT
  ARRAY_LENGTH(items) AS items_in_event,
  COUNT(*) AS events
FROM `bigquery-public-data.ga4_obfuscated_sample_ecommerce.events_*`
WHERE event_name = 'add_to_cart'
GROUP BY items_in_event
ORDER BY items_in_event ASC