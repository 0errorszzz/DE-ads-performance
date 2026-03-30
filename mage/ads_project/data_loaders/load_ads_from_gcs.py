from google.cloud import storage
import pandas as pd
import io

if 'data_loader' not in globals():
    from mage_ai.data_preparation.decorators import data_loader

@data_loader
def load_from_google_cloud_storage(*args, **kwargs):
    """
    Instructions for Reproducibility:
    1. Place your GCP service account JSON key in the 'auth/' directory.
    2. Update the placeholders below with your actual GCS details.
    """

    key_path = "/home/src/auth/your_gcp_service_account_key.json"
    bucket_name = 'your_gcs_bucket_name'
    object_key = 'global_ads_performance_dataset.csv'

    
    client = storage.Client.from_service_account_json(key_path)
    bucket = client.get_bucket(bucket_name)
    blob = bucket.blob(object_key)
    
    
    content = blob.download_as_bytes()
    df = pd.read_csv(io.BytesIO(content))
    
    return df
