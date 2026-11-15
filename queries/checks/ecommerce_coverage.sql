-- Q: What share of purchases have purchase_revenue filled in?

SELECT
  event_name,
  'purchase_revenue' AS field_name,
  SAFE_DIVIDE(COUNTIF(ecommerce.purchase_revenue IS NOT NULL), COUNT(*)) AS coverage_rate
FROM `{table}`
WHERE _TABLE_SUFFIX BETWEEN '{start_date}' AND '{end_date}'
  AND event_name = 'purchase'
GROUP BY event_name
