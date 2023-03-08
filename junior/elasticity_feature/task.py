import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression


def elasticity_df(df: pd.DataFrame) -> pd.DataFrame:
    ''' Function returning coefficient of determination as skus' elasticity '''
    model = LinearRegression()

    def get_elasticity(group: pd.Series) -> pd.Series:
        model.fit(group.price.array.reshape(-1, 1), np.log(group.qty.array + 1))
        return pd.Series({
            'elasticity': model.score(group.price.array.reshape(-1, 1), np.log(group.qty.array + 1))
            })

    return df.groupby('sku').apply(get_elasticity).reset_index()
