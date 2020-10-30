
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

path = "dataset/area_c/giorno_2015.csv"

data = pd.read_csv(path, sep=';')

# print(data['totale'].mean())

# Ho modificato il dataset per mostrare y;m;d separati
# Manca Novembre

# Agosto e DIcembre sono bassi, mancano dati?

print("Giorni in Agosto: " + str(len(data[data['month'] == 8])))
print("Giorni in Dicembre: " + str(len(data[data['month'] == 12])))

# print(data['month'].unique())
df = pd.Series()
for f in data['month'].unique():
    df = df.append(
        pd.Series(data[data['month'] == f]['totale'].sum()), 
        ignore_index=True
        )

#total = df.sum()
#df = df / total

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

df.plot.bar(width=0.9, color='#dd8d46')
plt.plot(np.array([-1, 12]),np.array([df.mean(), df.mean()]), color='#ddd846')
plt.text(12, df.mean()-0.2, "Media")
plt.xticks(range(0, 12), mesi)
plt.xlabel("Mesi")
plt.ylabel("Traffico mensile in Area C a Milano")
plt.tight_layout()
plt.show()

# Ho metà dei giorni a dicembre, potrei raddoppiarli...
# Non ho dati a novembre, potrei stimare una media...