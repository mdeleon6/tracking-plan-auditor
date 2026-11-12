-- Q: What share of events have at least one product with quantity filled in?

SELECT
  event_name,
  'quantity' AS field_name,
  SAFE_DIVIDE(
    COUNTIF(EXISTS(SELECT 1 FROM UNNEST(items) AS item WHERE item.quantity IS NOT NULL)),
    COUNT(*)
  ) AS coverage_rate
FROM `bigquery-public-data.ga4_obfuscated_sample_ecommerce.events_*`
WHERE ARRAY_LENGTH(items) > 0
GROUP BY event_name
