-- Q: How many times did each event fire on each day?

SELECT
  event_date,
  event_name,
  COUNT(*) AS event_count
FROM `bigquery-public-data.ga4_obfuscated_sample_ecommerce.events_*`
GROUP BY event_date, event_name
ORDER BY event_date ASC, event_name ASC
