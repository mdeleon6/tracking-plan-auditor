-- Q: Which event_params keys, plus purchase_revenue, does each purchase event carry?

SELECT
  event_date,
  event_name,
  ARRAY_CONCAT(
    ARRAY(SELECT key FROM UNNEST(event_params)),
    IF(ecommerce.purchase_revenue IS NOT NULL, ['purchase_revenue'], [])
  ) AS keys
FROM `{table}`
WHERE _TABLE_SUFFIX BETWEEN '{start_date}' AND '{end_date}'
  AND event_name = 'purchase'
