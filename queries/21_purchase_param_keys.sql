-- Q: Which event_params keys does each purchase event carry?

SELECT
  event_name,
  ARRAY(SELECT key FROM UNNEST(event_params)) AS keys
FROM `{table}`
WHERE _TABLE_SUFFIX BETWEEN '{start_date}' AND '{end_date}'
  AND event_name = 'purchase'
