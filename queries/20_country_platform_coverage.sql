-- Q: What share of each event has country, device category and platform filled in?

SELECT
  event_name,
  'country' AS field_name,
  SAFE_DIVIDE(COUNTIF(geo.country IS NOT NULL AND geo.country != '(not set)'), COUNT(*)) AS coverage_rate
FROM `bigquery-public-data.ga4_obfuscated_sample_ecommerce.events_*`
GROUP BY event_name

UNION ALL

SELECT
  event_name,
  'device_category' AS field_name,
  SAFE_DIVIDE(COUNTIF(device.category IS NOT NULL AND device.category != '(not set)'), COUNT(*)) AS coverage_rate
FROM `bigquery-public-data.ga4_obfuscated_sample_ecommerce.events_*`
GROUP BY event_name

UNION ALL

SELECT
  event_name,
  'platform' AS field_name,
  SAFE_DIVIDE(COUNTIF(platform IS NOT NULL), COUNT(*)) AS coverage_rate
FROM `bigquery-public-data.ga4_obfuscated_sample_ecommerce.events_*`
GROUP BY event_name
ORDER BY event_name, field_name
