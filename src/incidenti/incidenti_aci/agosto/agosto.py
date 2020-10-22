
import pandas as pd
import matplotlib.pyplot as plt

path = "dataset/incidenti/aci/autostrade/mesi_"

agosto = pd.DataFrame()

for year in range(2011, 2019):
    data = pd.read_csv(path + str(year) + ".csv")
    data['Anno'] = [year] * len(data)
    agosto = agosto.append(data[['NOME STRADA', 'Anno', 'Agosto']])


def two_cols_unique(data) -> list: 
    res = []

    field1 = data.columns[0]
    field2 = data.columns[1]

    for d1, d2 in zip(data[field1], data[field2]):
        if not (d1, d2) in res: 
            res.append((d1, d2))

    return res


def filter_with(data, field, comb : str) -> pd.DataFrame: 
    return data[data[field] == comb]


def sum_field(data): 
    res = pd.DataFrame()

    for combination in two_cols_unique(data[['NOME STRADA', 'Anno']]): 
        filtered_data = filter_with(filter_with(data, 'NOME STRADA', combination[0]), 'Anno', combination[1])
        d = {
            'Nome e Anno' : combination,
            'Inc' : sum(filtered_data['Agosto'])
        }
        res = res.append(d, ignore_index=True)

    return res

def f(data):
    res = [] 
    for d in data: 
        res.append('2018' not in str(d))

    return pd.Series(res)


agosto = sum_field(data)
agosto = agosto[f(agosto['Nome e Anno'])]
agosto = agosto.sort_values(by='Inc', ascending=False).head(20)

#print(agosto)

plt.bar(agosto['Nome e Anno'].astype(str), agosto['Inc'])
plt.xticks(rotation=90)
plt.tight_layout()
plt.show()


