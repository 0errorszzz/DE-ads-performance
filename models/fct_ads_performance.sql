{{ config(materialized='table') }}

SELECT
    *,
    SAFE_DIVIDE(clicks, impressions) AS ctr,
    SAFE_DIVIDE(spend, clicks) AS cpc,
    SAFE_DIVIDE(revenue, spend) AS roas,
    SAFE_DIVIDE(spend, conversions) AS cpa
FROM {{ ref('stg_ads_data') }}