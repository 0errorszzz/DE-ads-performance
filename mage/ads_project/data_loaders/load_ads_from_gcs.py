from google.cloud import storage
import pandas as pd
import io

if 'data_loader' not in globals():
    from mage_ai.data_preparation.decorators import data_loader

@data_loader
def load_from_google_cloud_storage(*args, **kwargs):
  
    key_path = "/home/src/google_credentials.json"
    bucket_name = 'ads-performance-lake-kestra-sandbox-485523'
    object_key = 'global_ads_performance_dataset.csv'

    
    client = storage.Client.from_service_account_json(key_path)
    bucket = client.get_bucket(bucket_name)
    blob = bucket.blob(object_key)
    
    
    content = blob.download_as_bytes()
    df = pd.read_csv(io.BytesIO(content))
    
    return df