-- Q: Do other events also stop at 12 items?

SELECT
  event_name,
  COUNT(*) AS events,
  MAX(ARRAY_LENGTH(items)) AS max_items,
  COUNTIF(ARRAY_LENGTH(items) = 12) AS events_with_12
FROM `bigquery-public-data.ga4_obfuscated_sample_ecommerce.events_*`
WHERE ARRAY_LENGTH(items) > 0
GROUP BY event_name
ORDER BY events DESC