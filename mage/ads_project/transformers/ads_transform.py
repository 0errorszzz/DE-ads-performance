import pandas as pd

if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer

@transformer
def transform(df, *args, **kwargs):
    df.columns = (df.columns
                .str.replace(' ', '_')
                .str.lower()
    )
    if 'date' in df.columns:
        df['date'] = pd.to_datetime(df['date'], errors='coerce')

    fill_values = {'revenue': 0, 'clicks': 0, 'impressions': 0}
    df = df.fillna(value={k: v for k, v in fill_values.items() if k in df.columns})

    print(f"Clean finished, current length: {len(df)}")
    return df