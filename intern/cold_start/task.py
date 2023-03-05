import pandas as pd


def fillna_with_mean(
    df: pd.DataFrame, target: str, group: str
) -> pd.DataFrame:
    group_means = df.groupby(group)[target].mean().reset_index()
    df_without_na = df.copy()

    df_without_na[target] = df[target].combine_first(
        df[[group, target]].merge(group_means, how='left',
                                  on=group, suffixes=('', '_new'))[f'{target}_new'].round()
    )
    return df_without_na
