-- Q: Which events does the Google Merchandise Store send, and how often?
-- Data: GA4 obfuscated sample ecommerce, Nov 1, 2020 - Jan 31, 2021 (all daily tables)
SELECT
  event_name,
  COUNT(*) AS event_count
FROM `bigquery-public-data.ga4_obfuscated_sample_ecommerce.events_*`
GROUP BY event_name
ORDER BY event_count DESC
