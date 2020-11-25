
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("dataset/incidenti/aci/autostrade/mesi_2014.csv")

lombardia = data[data['REGIONE'] == 'Lombardia'][['PROVINCIA', 'TOTALE']]

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


adriatica = data[data['CODICE'] == 'SS01601']
a1 = data[data['CODICE'] == 'AA00101']
a1_milano = a1[a1['PROVINCIA'] == 'Milano'][mesi]

a1 = sum_columns(a1[mesi], normalize=True)
a1_milano = sum_columns(a1_milano[mesi], normalize=True)
adriatica = sum_columns(adriatica[mesi], normalize=True)

df = pd.DataFrame([a1, adriatica], ['A1 Milano', 'Adriatica']).transpose().plot.bar(width=0.9, color=['#a1cc61', '#61a1cc'])
plt.ylabel("Percentuale di incidenti al mese (2014)")
plt.tight_layout()
plt.savefig("milano_adriatica_2014")
# plt.show()