-- Q What is the coverage rate of fields for each event in the plan?
WITH totals AS (
    SELECT
        event_name,
        COUNT(*) AS total_events
    FROM `bigquery-public-data.ga4_obfuscated_sample_ecommerce.events_*`
    GROUP BY
        event_name
),
fields AS (
    SELECT
        event_name,
        param.key AS field_name,
        COUNT(*) AS times_sent
    FROM `bigquery-public-data.ga4_obfuscated_sample_ecommerce.events_*`,
        UNNEST(event_params) AS param
    GROUP BY event_name, field_name
)
SELECT 
    fields.event_name,
    fields.field_name,
    SAFE_DIVIDE(fields.times_sent, totals.total_events) AS coverage_rate
FROM fields
JOIN totals
    ON fields.event_name = totals.event_name
ORDER BY fields.event_name, coverage_rate DESC