-- Q: What share of products have each items field filled in, per event?

WITH item_rows AS (
  SELECT event_name, item
  FROM `bigquery-public-data.ga4_obfuscated_sample_ecommerce.events_*`,
    UNNEST(items) AS item
)
SELECT
  event_name,
  'item_id' AS field_name,
  SAFE_DIVIDE(COUNTIF(item.item_id IS NOT NULL AND item.item_id != '(not set)'), COUNT(*)) AS coverage_rate
FROM item_rows
GROUP BY event_name

UNION ALL

SELECT
  event_name,
  'item_name' AS field_name,
  SAFE_DIVIDE(COUNTIF(item.item_name IS NOT NULL AND item.item_name != '(not set)'), COUNT(*)) AS coverage_rate
FROM item_rows
GROUP BY event_name

UNION ALL

SELECT
  event_name,
  'price' AS field_name,
  SAFE_DIVIDE(COUNTIF(item.price IS NOT NULL), COUNT(*)) AS coverage_rate
FROM item_rows
GROUP BY event_name

UNION ALL

SELECT
  event_name,
  'quantity' AS field_name,
  SAFE_DIVIDE(COUNTIF(item.quantity IS NOT NULL), COUNT(*)) AS coverage_rate
FROM item_rows
GROUP BY event_name

UNION ALL

SELECT
  event_name,
  'item_category' AS field_name,
  SAFE_DIVIDE(COUNTIF(item.item_category IS NOT NULL AND item.item_category != '(not set)'), COUNT(*)) AS coverage_rate
FROM item_rows
GROUP BY event_name
ORDER BY event_name, field_name