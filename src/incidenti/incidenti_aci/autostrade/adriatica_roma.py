
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("dataset/incidenti/aci/autostrade/mesi_2018.csv")

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

mesi = ['Gennaio', 'Febbraio', 'Marzo', 'Aprile', 'Maggio', 'Giugno', 'Luglio', 'Agosto', 'Settembre', 'Ottobre', 'Novembre', 'Dicembre'] 

raccordo = data[data['CODICE'] == 'AA09001']
adriatica = data[data['CODICE'] == 'SS01601']

adriatica = sum_columns(adriatica[mesi])
raccordo = sum_columns(raccordo[mesi])

df = pd.DataFrame([adriatica, raccordo], ['Adriatica', 'Raccordo Anulare Roma']).transpose()

df.plot.bar(width=0.9, color=['#a1cc61', '#61a1cc'])
plt.ylabel("Numero di incidenti al mese (2018)")
plt.tight_layout()
plt.show()

# racc_mean = raccordo.mean()
# print((raccordo['Agosto'] - racc_mean) / racc_mean)