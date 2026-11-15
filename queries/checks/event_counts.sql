-- Q: Which events were received in the period, and how often?

SELECT
  event_name,
  COUNT(*) AS event_count
FROM `{table}`
WHERE _TABLE_SUFFIX BETWEEN '{start_date}' AND '{end_date}'
GROUP BY event_name
ORDER BY event_count DESC
