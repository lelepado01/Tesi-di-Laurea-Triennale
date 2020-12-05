
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

path = "dataset/area_c/orari_2012.csv"

data = pd.read_csv(path, sep=';')

df = pd.Series()
for f in data['month'].unique():
    df = df.append(
        pd.Series(data[data['month'] == f]['totale'].sum()), 
        ignore_index=True
        )

mesi = [
    'Gennaio',
    'Febbraio',
    'Marzo',
    'Aprile',
    'Maggio',
    'Giugno',
    'Luglio',
    'Agosto',
    'Settembre',
    'Ottobre',
    'Novembre',
    'Dicembre'
]

incidenti = pd.read_csv("dataset/incidenti/incidenti_2012.txt", sep='\t')
mesi_incidenti = incidenti['mese'].value_counts().sort_index()

df.index = range(1,13)
perc_traffico = df / df.sum()

# print(mesi_incidenti)
# print(df)
rapp = mesi_incidenti / df


plt.subplot(1,2,1)
plt.fill_between(perc_traffico.index, perc_traffico, color='#66ad9f')
plt.ylabel("Percentuale di traffico in Area C")
plt.xticks(range(1,13))
plt.tight_layout()

plt.subplot(1,2,2)
plt.fill_between(rapp.index, rapp, color='#9f66ad')
plt.xticks(range(1, 13))
plt.ylabel("Rapporto tra incidenti e traffico")
plt.tight_layout()
plt.show()
