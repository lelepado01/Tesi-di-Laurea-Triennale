
import pandas as pd

# Returns a series result of the sum of all the columns in the given dataframe 
# if normalize is True, the returned values will all be between 0 and 1
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

# the function returns a dataframe where all the values in the column named as column_to_sum 
# are summed according to the selected field
def sum_field_by_column(data : pd.DataFrame, select_field : str, column_to_sum : str) -> pd.DataFrame: 
    res = pd.DataFrame()
    for field in data[select_field].unique(): 
        res = res.append(
            sum_columns(data[data[select_field] == field][column_to_sum], name=field), 
        )
    
    return res

# the function returns a dataframe where all the values in the column named as column_to_sum 
# are summed according to the two selected fields, couple-wise
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

# The function returns a dataframe where two selected columns are summed according to a 
# chosen field
def sum_two_fields_by_column(data, select, field_to_sum1, field_to_sum2): 
    dic = {}
    for f in data[select].unique(): 
        dic[f] = [
            data[data[select] == f][field_to_sum1].sum(), 
            data[data[select] == f][field_to_sum2].sum()
            ]

    return pd.DataFrame(dic).transpose()


# The function converts the first two columns of a dataset in a list of couples 
# without any repetition
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


# The function returns a boolean pd.Series used to filter only the fields 
# which satisfy a property
def filter_by_value(data : pd.Series, value : str, inverted = False) -> pd.Series:
    res = [] 
    for d in data: 
        if inverted: 
            res.append(value not in str(d))
        else: 
            res.append(value in str(d))

    return pd.Series(res)

# The function returns a pd.Dataframe where the column field_to_sum is summed according to 
# the selected field
def get_sum_of_fields(data : pd.DataFrame, select_field : str, field_to_sum : str) -> pd.Series: 
    res = {}
    index = 0
    for reg in data[select_field].unique():
        res[index] = [reg, 0]
        index += 1

    index = 0
    for reg in data[select_field].unique():
        for row in data[data[select_field] == reg][field_to_sum]:
            res[index] = [res[index][0], res[index][1] + row]
        index += 1

    return pd.DataFrame(res, index=[select_field, field_to_sum]).transpose()