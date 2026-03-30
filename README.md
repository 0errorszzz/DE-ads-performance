# DE-ads-performance
Zoomcamp project
Ads Performance Data Pipeline Project Overview
This project builds a complete end-to-end data pipeline to analyze multi-channel advertising performance (TikTok, Meta, Google) for year 2024. It covers infrastructure, orchestration, transformation, and visualization.
Tech Stack
Infrastructure: Terraform (GCP BigQuery)
Orchestration: Mage AI
Transformation: dbt (Data Build Tool)
Storage: Google BigQuery
Visualization: Looker Studio

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
git clone [<your-repo-link>](https://github.com/0errorszzz/DE-ads-performance.git)
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
Access Mage UI at localhost:6789, update the project_id in the pipeline blocks, and run ads_performance_etl.
The raw data is located in the /data directory. Use Mage to load it into BigQuery:
Start Mage: 
```bash
mage start ads_project
```
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

