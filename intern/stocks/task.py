import pandas as pd


def limit_gmv(df: pd.DataFrame) -> pd.DataFrame:
    corrected_df = df.copy()
    corrected_df['gmv'] = ((df.gmv/df.price).astype(int).clip(upper=df.stock) *
                            df.price).astype(float)
    return corrected_df
