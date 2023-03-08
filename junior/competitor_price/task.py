import numpy as np
import pandas as pd


def agg_comp_price(X: pd.DataFrame) -> pd.DataFrame:
    ''' Function to calculate final price depending on competitors' prices '''

    agg_funcs = {
        'min': np.min,
        'max': np.max,
        'med': np.median,
        'avg': np.mean,
    }

    def agg_func(group: pd.Series) -> pd.Series:
        func = group['agg'].iloc[0]

        if func == 'rnk':
            return pd.Series({
                'comp_price': group.loc[group['rank'] == group['rank'].min(), 'comp_price'].min()
                })

        return pd.Series({'comp_price': group.comp_price.agg(agg_funcs[func])})

    copy_X = X.groupby(['sku', 'agg', 'base_price']).apply(agg_func).reset_index()

    copy_X['new_price'] = copy_X['base_price']
    copy_X.loc[abs(copy_X['comp_price']/copy_X['base_price'] - 1) <= 0.2, 'new_price'] = \
        copy_X.loc[abs(copy_X['comp_price']/copy_X['base_price'] - 1) <= 0.2, 'comp_price']

    return copy_X.sort_values(by='sku').reset_index(drop=True)
