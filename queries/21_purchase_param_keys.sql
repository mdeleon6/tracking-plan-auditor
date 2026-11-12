-- Q: Which event_params keys does each purchase event carry?

SELECT
  event_name,
  ARRAY(SELECT key FROM UNNEST(event_params)) AS keys
FROM `bigquery-public-data.ga4_obfuscated_sample_ecommerce.events_*`
WHERE event_name = 'purchase'
