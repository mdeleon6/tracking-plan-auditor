-- Q 6: How many purchase events have a transaction_id in event_params vs ecommerce.transaction_id?

SELECT
  event_date,
  COUNT(*) as purchases,
  COUNTIF(EXISTS(SELECT 1 FROM UNNEST(event_params) WHERE key = 'transaction_id')) AS with_params_id,
  COUNTIF(ecommerce.transaction_id IS NOT NULL AND ecommerce.transaction_id != '(not set)') AS with_ecommerce_id
FROM `bigquery-public-data.ga4_obfuscated_sample_ecommerce.events_*`
WHERE event_name = 'purchase'
GROUP BY event_date
ORDER BY event_date ASC