{{ config(materialized='view') }}

SELECT
    CAST(date AS DATE) AS ad_date,
    platform,
    campaign_type,
    industry,
    country,
    impressions,
    clicks,
    ad_spend AS spend,
    conversions,
    revenue
FROM {{ source('ads_raw_data', 'global_ads_performance') }}