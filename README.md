# DE-ads-performance

## Ads Performance Data Pipeline Project Overview
This project builds a complete end-to-end data pipeline to analyze multi-channel advertising performance (TikTok, Meta, Google) for year 2024. It covers infrastructure, orchestration, transformation, and visualization.

## Problem Description
In modern digital marketing, companies run advertising campaigns across multiple platforms such as TikTok Ads, Meta Ads, and Google Ads. However, it is often unclear which platform delivers the best return and what factors drive performance changes over time.

This project builds an end-to-end data pipeline to analyze multi-channel advertising performance for the year 2024. The goal is to:

- Compare the return on ad spend (ROAS) across different platforms
- Analyze how conversion efficiency changes over time
- Identify key periods where performance declines and understand the underlying causes

By integrating data ingestion, transformation, and visualization, this project provides insights into how advertising effectiveness is influenced not just by spending, but by conversion behavior.

The analysis reveals that performance fluctuations are primarily driven by changes in conversion rate rather than advertising spend.

## Tech Stack
Infrastructure: Terraform (GCP BigQuery)
Orchestration: Mage AI
Transformation: dbt (Data Build Tool)
Storage: Google BigQuery
Visualization: Looker Studio

## Architecture

Raw CSV (Kaggle)
→ Mage ETL Pipeline
→ BigQuery (Raw Table)
→ dbt (Staging + Fact Models)
→ Looker Studio Dashboard

## Data Source
The dataset used in this project is sourced from Kaggle: [Ads Performance Dataset.](https://www.kaggle.com/datasets/tahirmohd/global-ads-performance/data)

Local Copy: For your convenience, a copy of the raw CSV is included in the /data directory of this repository.

Note: If you download the data directly from Kaggle, ensure the filename matches global_ads_performance_dataset.csv or update the constant in the Mage loader.

## Step-by-Step Reproduction Guide
1. Prerequisites & Environment Setup
Prerequisites
- Google Cloud account with BigQuery enabled
- Docker Desktop installed and running
- Python 3.9+
- Terraform installed
- dbt (BigQuery adapter) installed

Clone the repository and install the required Python packages:
```bash
git clone https://github.com/0errorszzz/DE-ads-performance.git
cd DE-ads-performance
pip install -r requirements.txt
```

2. Credentials Setup (Critical!)
Create an /auth folder in the root directory.
Place your Google Cloud Service Account JSON key inside and rename it to google_credentials.json.
Note: This folder is ignored by Git for security.

3. Infrastructure as Code (Terraform)
Provision the BigQuery datasets and tables automatically:
```bash
cd terraform
terraform init
terraform apply
```
Ensure you update the project_id in main.tf before running.

4. Data Ingestion (Mage AI)
Ensure Docker Desktop is running, then:
```bash
cd mage
docker-compose up
```
Access Mage UI at http://localhost:6789

Update the project_id and key_path in the pipeline blocks, and run ads_performance_etl.

The raw data is located in the /data directory. Use Mage to load it into BigQuery:

Open the UI and run the ads_performance_etl pipeline.
Important: Update the project_id and key_path in the Data Loader and Data Exporter blocks to match your environment.

5. Data Transformation (dbt)
Ensure you are in the dbt_env virtual environment and located in the project root.
First, verify your BigQuery connection:
```bash
dbt debug --profiles-dir .
```
Then, execute the transformation pipeline:
Installs necessary dbt packages:
```bash
dbt deps
```
Builds models in BigQuery:
```bash
dbt run --profiles-dir .
```
Runs data quality tests:
```bash
dbt test --profiles-dir .
```
6. Dashboard is available in Lookers with the link below:

https://lookerstudio.google.com/s/n8FcKebnHgk

## Dashboard
<img width="1429" height="1069" alt="image" src="https://github.com/user-attachments/assets/c5626a76-3310-4889-b926-4a29051c8754" />

### 1. ROAS by Platform
This chart compares the average return on ad spend (ROAS) across platforms. TikTok Ads shows the highest ROAS, indicating the most efficient use of advertising budget. Meta Ads performs moderately, while Google Ads has the lowest ROAS among the three.

ROAS is defined as revenue divided by spend, and reflects how effectively each dollar of advertising generates revenue.

---

### 2. Conversion Rate over Time
The conversion rate (conversions / clicks) shows fluctuations throughout the year, with a noticeable decline around July and a peak toward the end of the year.

This suggests that user willingness to complete a purchase after clicking ads decreases in mid-year and increases during later months.

---

### 3. ROAS over Time
ROAS follows a similar trend to the conversion rate, reaching its lowest point in July and increasing toward November and December.

The alignment between ROAS and conversion rate indicates that overall advertising performance is strongly influenced by conversion efficiency rather than changes in traffic.

A possible explanation is seasonal behavior: mid-year (summer months) often has lower consumer purchase intent, while late-year peaks may be driven by major shopping events such as Black Friday and holiday promotions.

---

### 4. Spend vs Revenue over Time
Advertising spend remains relatively stable across the year, while revenue shows a clear dip in mid-year and an increase toward the end of the year.

This confirms that the performance drop in July is not due to reduced spending, but rather decreased conversion efficiency. Conversely, higher revenue at the end of the year suggests improved conversion effectiveness rather than increased budget.

---

### Overall Insight
Across all charts, a consistent pattern emerges: performance declines in mid-year and improves toward year-end. 

Since spending remains stable while both conversion rate and ROAS fluctuate, this indicates that changes in performance are primarily driven by user conversion behavior rather than advertising investment.

These findings suggest that improving conversion efficiency during mid-year (e.g., through better targeting or optimized landing pages) could significantly enhance overall advertising performance.

## Conclusion

This project demonstrates how an end-to-end data pipeline can be used to analyze advertising performance across multiple platforms.

The results highlight the importance of conversion efficiency in driving business outcomes. Rather than increasing advertising spend, improving conversion rates may lead to better overall performance.

Future improvements could include:
- Adding more granular data (e.g., campaign-level analysis)
- Automating pipeline scheduling
- Incorporating additional KPIs and anomaly detection
