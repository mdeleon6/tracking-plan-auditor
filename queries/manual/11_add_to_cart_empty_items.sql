-- Q: How many add_to_cart events have an empty items list?

SELECT
  COUNT(*) AS add_to_cart_events,
  COUNTIF(ARRAY_LENGTH(items) = 0) AS events_with_no_items
FROM `bigquery-public-data.ga4_obfuscated_sample_ecommerce.events_*`
WHERE event_name = 'add_to_cart'
