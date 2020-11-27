import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("dataset/incidenti/aci/autostrade/mesi_2018.csv")

mesi = ['Gennaio', 'Febbraio', 'Marzo', 'Aprile', 'Maggio', 'Giugno', 'Luglio', 'Agosto', 'Settembre', 'Ottobre', 'Novembre', 'Dicembre'] 

def get_sum_fields(data : pd.DataFrame, select_field : str, field_to_sum : str) -> pd.Series: 
    res = {}
    for field in data[select_field].unique(): 
        res[field] = sum(data[data[select_field] == field][field_to_sum])

    return pd.Series(res)

def sum_columns(data : pd.DataFrame, normalize = False) -> pd.Series: 
    res = {}
    for col in data.columns: 
        res[col] = sum(data[col])

    res = pd.Series(res).transpose()

    if normalize: 
        res = res / sum(res)

    return res

adriatica = data[data['CODICE'] == 'SS01601'][mesi]
a1 = data[data['CODICE'] == 'AA00101'][mesi]
aurelia = data[data['CODICE'] == 'SS00101'][mesi]

adriatica = sum_columns(adriatica, normalize=True)
a1 = sum_columns(a1, normalize=True)
aurelia =  sum_columns(aurelia, normalize=True)

pd.DataFrame([a1, adriatica, aurelia], ['A1', 'Adriatica', 'Aurelia']).transpose().plot()
plt.xlabel("Differenza tra incidenti mensili")
plt.show()