-- Q: What are the field names to the events in the plan?
-- Get field names and their usage counts for each event
SELECT
  event_name,
  param.key AS field_name,
  COUNT(*) AS times_sent
FROM `bigquery-public-data.ga4_obfuscated_sample_ecommerce.events_*`,
  UNNEST(event_params) AS param
WHERE _TABLE_SUFFIX BETWEEN '20201201' AND '20201207'
GROUP BY event_name, field_name
ORDER BY event_name, times_sent DESC