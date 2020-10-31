
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

path = "dataset/area_c/giorno_2013.csv"

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

df.at[11] = df.iloc[10] * 31/16 # Stimo dicembre
df.at[10] = df.mean()           # Metto novembre = media

# df.plot.bar(width=0.9, color='#dd8d46')
# plt.plot(np.array([-1, 12]),np.array([df.mean(), df.mean()]), color='#ddd846')
# plt.text(12, df.mean()-0.2, "Media")
# plt.xticks(range(0, 12), mesi)
# plt.xlabel("Mesi")
# plt.ylabel("Traffico mensile in Area C a Milano")
# plt.tight_layout()
# plt.show()

total = df.sum()
perc_traffico = df / total

# Ho metà dei giorni a dicembre, potrei raddoppiarli...
# Non ho dati a novembre, potrei stimare una media...

incidenti = pd.read_csv("dataset/incidenti/incidenti_2013.txt", sep='\t', encoding='latin1')
mesi_incidenti = incidenti['mese'].value_counts().sort_index()

# mesi_incidenti.plot.bar()
# plt.show()

perc_traffico = pd.DataFrame(perc_traffico)
perc_traffico.index = range(1,13)
mesi_norm = mesi_incidenti * (1-perc_traffico[0])

# print(mesi_incidenti)
# print(perc_traffico)
# print(mesi_norm)

plt.subplot(3,1,1)
plt.plot(mesi_incidenti)
plt.fill_between(mesi_incidenti.index, mesi_incidenti)
plt.title("Incidenti al Mese")
plt.tight_layout()
plt.subplot(3,1,2)
plt.plot(perc_traffico)
plt.fill_between(perc_traffico.index, perc_traffico[0])
plt.title("Percentuale di traffico nel mese rispetto al totale annuale")
plt.tight_layout()
plt.subplot(3,1,3)
plt.title("Incidenti tenendo conto del traffico")
plt.plot(mesi_norm)
plt.fill_between(mesi_norm.index, mesi_norm)
plt.tight_layout()
plt.show()