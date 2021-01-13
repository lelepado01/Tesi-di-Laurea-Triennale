
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("dataset/incidenti/aci/autostrade/comuni_2018.csv")

# Conteggio di incidenti per nome della strada
df = {}
for auto in data['NOME STRADA'].unique(): 
    df[auto] = 0

for k, inc in zip(data['NOME STRADA'], data['INC']): 
    df[k] += inc

incidenti = pd.Series(df.values(), index=df.keys()).sort_values().tail(10)

# Colorazione del grafico
color_ls = ['#9fc4b3'] * 10
color_ls[9] = '#5daf8a'
color_ls[7] = '#5daf8a'

incidenti.plot.barh(width=0.9, color=color_ls)
plt.tight_layout()
plt.show()