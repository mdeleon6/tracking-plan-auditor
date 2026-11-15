-- Q: Are the purchases missing shipping_tier the same ones missing transaction_id?

WITH flags AS (
  SELECT
    event_date,
    EXISTS(SELECT 1 FROM UNNEST(event_params) WHERE key = 'shipping_tier') AS has_shipping_tier,
    EXISTS(SELECT 1 FROM UNNEST(event_params) WHERE key = 'transaction_id') AS has_transaction_id
  FROM `bigquery-public-data.ga4_obfuscated_sample_ecommerce.events_*`
  WHERE event_name = 'purchase'
)
SELECT
  has_shipping_tier,
  has_transaction_id,
  COUNT(*) AS purchases
FROM flags
WHERE event_date >= '20201121'
GROUP BY has_shipping_tier, has_transaction_id
ORDER BY purchases DESC
