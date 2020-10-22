
import pandas as pd

def sum_columns(data, normalize = False, name=None) -> pd.Series: 
    res = {}
    if data is pd.DataFrame: 
        for col in data.columns: 
            res[col] = sum(data[col])
    else: 
        res['val'] = data.sum()

    if name is None:
        res = pd.Series(res).transpose()
    else: 
        res = pd.Series(res, name=name)

    if normalize: 
        res = res / sum(res)

    return res

def sum_field_by_column(data : pd.DataFrame, select_field : str, column_to_sum : str) -> pd.DataFrame: 
    res = pd.DataFrame()
    for field in data[select_field].unique(): 
        res = res.append(
            sum_columns(data[data[select_field] == field][column_to_sum], name=field), 
        )
    
    return res