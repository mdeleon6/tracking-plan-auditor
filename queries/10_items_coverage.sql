-- Q: How many add_to_cart items have each required field filled in?

SELECT
  COUNT(*) AS total_items,
  COUNTIF(item.item_id IS NOT NULL AND item.item_id != '(not set)') AS with_item_id,
  COUNTIF(item.item_name IS NOT NULL AND item.item_name != '(not set)') AS with_item_name,
  COUNTIF(item.item_category IS NOT NULL AND item.item_category != '(not set)') AS with_item_category,
  COUNTIF(item.price IS NOT NULL) AS with_price,
  COUNTIF(item.quantity IS NOT NULL) AS with_quantity
FROM `bigquery-public-data.ga4_obfuscated_sample_ecommerce.events_*`,
  UNNEST(items) AS item
WHERE event_name = 'add_to_cart'
