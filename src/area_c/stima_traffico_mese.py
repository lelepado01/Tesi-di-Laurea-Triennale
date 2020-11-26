
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

path = "dataset/area_c/orari_2012.csv"

data = pd.read_csv(path, sep=';')

# print(data['totale'].mean())

# Ho modificato il dataset per mostrare y;m;d separati
# Manca Novembre

# Agosto e DIcembre sono bassi, mancano dati?

# print("Giorni in Agosto: " + str(len(data[data['month'] == 8])))
# print("Giorni in Dicembre: " + str(len(data[data['month'] == 12])))

# print(data['month'].unique())
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

perc_traffico = df / df.sum()

# print(perc_traffico)

color_ls = ['#dbad85']*12
color_ls[5:7] = ['#dd8d46']*3

perc_traffico.plot.bar(width=0.9, color=color_ls)
plt.plot(np.array([-1, 12]),np.array([perc_traffico.mean(), perc_traffico.mean()]), color='#ddd846')
plt.text(3, df.mean(), "Media")
plt.xlabel("")
plt.ylabel("Percentuale di traffico al mese in Area C")
plt.xticks(range(0, 12), mesi)
plt.tight_layout()
plt.show()

