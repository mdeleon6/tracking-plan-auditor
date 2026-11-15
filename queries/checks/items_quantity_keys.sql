-- Q: Which add_to_cart events have at least one product with quantity filled in?

SELECT
  event_date,
  event_name,
  IF(EXISTS(SELECT 1 FROM UNNEST(items) AS item WHERE item.quantity IS NOT NULL), ['quantity'], []) AS keys
FROM `{table}`
WHERE _TABLE_SUFFIX BETWEEN '{start_date}' AND '{end_date}'
  AND event_name = 'add_to_cart'
  AND ARRAY_LENGTH(items) > 0
