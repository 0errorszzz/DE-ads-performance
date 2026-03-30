terraform {
  required_providers {
    google = {
      source  = "hashicorp/google"
      version = "5.6.0"
    }
  }
}

provider "google" {
  # 替换成你自己的 GCP Project ID
  project = "kestra-sandbox-485523" 
  region  = "us-west1"
}

# 创建数据湖 Bucket
resource "google_storage_bucket" "ads_lake" {
  name          = "ads-performance-lake-kestra-sandbox-485523" 
  location      = "US"
  force_destroy = true
}

# 创建数据仓库 Dataset
resource "google_bigquery_dataset" "ads_dataset" {
  dataset_id = "ads_performance"
  location   = "US"
}