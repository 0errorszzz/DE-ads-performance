from google.cloud import bigquery
from google.oauth2 import service_account
import pandas as pd

if 'data_exporter' not in globals():
    from mage_ai.data_preparation.decorators import data_exporter

@data_exporter
def export_data(df, *args, **kwargs):
    """
    Instructions for Reproducibility:
    1. Place your GCP service account JSON key in the 'auth/' directory.
    2. Update the 'project_id' and 'table_id' with your BigQuery details.
    """
    project_id = 'your_gcp_project_id'
    table_id = f'{project_id}.ads_data_all.global_ads_performance'
    key_path = "/home/src/auth/your_gcp_service_account_key.json"
    
    credentials = service_account.Credentials.from_service_account_file(key_path)
    client = bigquery.Client(credentials=credentials, project=project_id)
    
    # Partition and Clustering added

    print(f"Currently writing {len(df)} line to BigQuery...(Partition and Clustering)")
    job = client.load_table_from_dataframe(df, table_id, job_config=job_config)
    job.result()  

    print(f"Success! Data saved in: {table_id}")
