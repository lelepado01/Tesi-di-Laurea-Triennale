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

adriatica = data[data['CODICE'] ==  'SS01601'][mesi]
a1 = data[data['CODICE'] == 'AA00101'][mesi]
aurelia = data[data['CODICE'] ==    'SS00101'][mesi]

a4 = data[data['CODICE'] == 'AA00401'][mesi]
a90 = data[data['CODICE'] == 'AA09001'][mesi]

adriatica = sum_columns(adriatica)
a1 = sum_columns(a1)
aurelia =  sum_columns(aurelia)
a4 = sum_columns(a4)
a90 =  sum_columns(a90)

import sys
sys.path.append("src")
import heatmap as H

df = pd.DataFrame(
    [a1, adriatica, aurelia, a4, a90], 
    ['A1 Milano-Roma-Napoli', 'SS16 Adriatica', 'SS1 Aurelia', 'A4 Torino Trieste', 'A90 Raccordo Anulare']
    )

fig, ax = plt.subplots()
im, cbar = H.heatmap(df, df.index, df.columns, ax=ax, cmap="OrRd", cbarlabel="Incidenti all'anno (2018)", xticks_rotated=True)
texts = H.annotate_heatmap(im, valfmt="{x}")

fig.tight_layout()
plt.show()
