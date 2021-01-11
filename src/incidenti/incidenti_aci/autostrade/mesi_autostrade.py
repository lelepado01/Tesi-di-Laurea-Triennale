import pandas as pd
import matplotlib.pyplot as plt
import sys
sys.path.append("src")
import aci_utils
import heatmap as H

data = pd.read_csv("dataset/incidenti/aci/autostrade/mesi_2018.csv")

mesi = ['Gennaio', 'Febbraio', 'Marzo', 'Aprile', 'Maggio', 'Giugno', 'Luglio', 'Agosto', 'Settembre', 'Ottobre', 'Novembre', 'Dicembre'] 

adriatica = data[data['CODICE'] ==  'SS01601'][mesi]
a1 = data[data['CODICE'] == 'AA00101'][mesi]
aurelia = data[data['CODICE'] ==    'SS00101'][mesi]

a4 = data[data['CODICE'] == 'AA00401'][mesi]
a90 = data[data['CODICE'] == 'AA09001'][mesi]

adriatica = aci_utils.sum_columns(adriatica)
a1 = aci_utils.sum_columns(a1)
aurelia =  aci_utils.sum_columns(aurelia)
a4 = aci_utils.sum_columns(a4)
a90 =  aci_utils.sum_columns(a90)

df = pd.DataFrame(
    [a1, adriatica, aurelia, a4, a90], 
    ['A1 Milano-Roma-Napoli', 'SS16 Adriatica', 'SS1 Aurelia', 'A4 Torino Trieste', 'A90 Raccordo Anulare']
    )

fig, ax = plt.subplots()
im = H.heatmap(df, df.index, df.columns, ax=ax, cmap="OrRd", xticks_rotated=True, cbar_visible=False)
texts = H.annotate_heatmap(im, valfmt="{x}")
fig.tight_layout()
plt.show()
