-- Q: What share of purchases have purchase_revenue filled in?

SELECT
  event_name,
  'purchase_revenue' AS field_name,
  SAFE_DIVIDE(COUNTIF(ecommerce.purchase_revenue IS NOT NULL), COUNT(*)) AS coverage_rate
FROM `bigquery-public-data.ga4_obfuscated_sample_ecommerce.events_*`
WHERE event_name = 'purchase'
GROUP BY event_name
