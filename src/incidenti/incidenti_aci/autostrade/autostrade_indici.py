import pandas as pd

data = pd.read_csv("dataset/incidenti/aci/autostrade/mesi_2018.csv")

def sum_columns(data : pd.DataFrame, normalize = False) -> pd.Series: 
    res = {}
    for col in data.columns: 
        res[col] = sum(data[col])

    res = pd.Series(res).transpose()

    if normalize: 
        res = res / sum(res)

    return res

mesi = ['Gennaio', 'Febbraio', 'Marzo', 'Aprile', 'Maggio', 'Giugno', 'Luglio', 'Agosto', 'Settembre', 'Ottobre', 'Novembre', 'Dicembre'] 

raccordo = data[data['CODICE'] == 'AA09001']
raccordo = sum_columns(raccordo[mesi])
racc_mean = raccordo.mean()
print((raccordo['Agosto'] - racc_mean) / racc_mean) # -0.46