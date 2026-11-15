-- Q: For each event, how many events carried each number of products?

SELECT
  event_name,
  ARRAY_LENGTH(items) AS items_in_event,
  COUNT(*) AS events
FROM `{table}`
WHERE _TABLE_SUFFIX BETWEEN '{start_date}' AND '{end_date}'
  AND ARRAY_LENGTH(items) > 0
GROUP BY event_name, items_in_event
