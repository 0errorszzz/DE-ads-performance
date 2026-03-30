import io
import pandas as pd
import requests
if 'data_loader' not in globals():
    from mage_ai.data_preparation.decorators import data_loader

@data_loader
def load_data_from_api(*args, **kwargs):
    # 这是一个公开的广告数据集示例（如果是你自己的 CSV 链接请替换）
    url = 'https://raw.githubusercontent.com/datasets/investor-flow/master/data/investor-flow.csv' 
    
    response = requests.get(url)
    df = pd.read_csv(io.StringIO(response.text))
    
    # 打印前几行看看对不对
    print(df.head())
    return df