-- Q: How many times did each event fire on each day?

SELECT
  event_date,
  event_name,
  COUNT(*) AS event_count
FROM `{table}`
WHERE _TABLE_SUFFIX BETWEEN '{start_date}' AND '{end_date}'
GROUP BY event_date, event_name
ORDER BY event_date ASC, event_name ASC
