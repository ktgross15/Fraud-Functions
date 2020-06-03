import pandas as pd

def multiply_cols(df, x, y, new_col_name):
    df[new_col_name] = df[x] * df[y]
    return df
