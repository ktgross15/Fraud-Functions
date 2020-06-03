import pandas as pd

def multiply_cols(df, x, y, new_col_name):
    '''mutliply two columns together and return new dataframe'''
    # added thing
    df[new_col_name] = df[x] * df[y]
    return df
