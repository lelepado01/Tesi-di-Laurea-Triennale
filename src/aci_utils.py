
import pandas as pd

def sum_columns(data : pd.DataFrame, normalize = False, name=None) -> pd.Series: 
    res = {}
    for col in data.columns: 
        res[col] = sum(data[col])

    if name is None:
        res = pd.Series(res).transpose()
    else: 
        res = pd.Series(res, name=name)

    if normalize: 
        res = res / sum(res)

    return res
