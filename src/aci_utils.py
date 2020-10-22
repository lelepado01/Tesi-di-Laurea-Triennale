
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

def two_cols_unique(data) -> list: 
    res = []

    field1 = data.columns[0]
    field2 = data.columns[1]

    for d1, d2 in zip(data[field1], data[field2]):
        if not (d1, d2) in res: 
            res.append((d1, d2))

    return res


def filter_with(data : pd.DataFrame, field, comb : str) -> pd.DataFrame: 
    return data[data[field] == comb]


def sum_field_by_two_columns(data : pd.DataFrame, field1 : str, field2 : str, field_to_sum : str) -> pd.DataFrame: 
    res = pd.DataFrame()

    for combination in two_cols_unique(data[[field1, field2]]): 
        filtered_data = filter_with(filter_with(data, field1, combination[0]), field2, combination[1])
        d = {
            (field1 + "_" + field2) : combination,
            'Value' : sum(filtered_data[field_to_sum])
        }
        res = res.append(d, ignore_index=True)

    return res


def filter_by_value(data : pd.Series, value : str, inverted = False) -> pd.Series:
    res = [] 
    for d in data: 
        if inverted: 
            res.append(value not in str(d))
        else: 
            res.append(value in str(d))

    return pd.Series(res)

