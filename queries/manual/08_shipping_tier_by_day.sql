-- Q: How many purchases have shipping_tier each day?

SELECT
  event_date,
  COUNT(*) as purchases,
  COUNTIF(EXISTS(SELECT 1 FROM UNNEST(event_params) WHERE key = 'shipping_tier')) AS with_shipping_tier,
FROM `bigquery-public-data.ga4_obfuscated_sample_ecommerce.events_*`
WHERE event_name = 'purchase'
GROUP BY event_date
ORDER BY event_date ASC