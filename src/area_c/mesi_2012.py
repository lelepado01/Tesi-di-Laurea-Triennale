
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

# perc_traffico.plot.bar(width=0.9, color=color_ls)
# plt.plot(np.array([-1, 12]),np.array([perc_traffico.mean(), perc_traffico.mean()]), color='#ddd846')
# plt.text(11, df.mean()-0.2, "Media")
# plt.xlabel("Mesi")
# plt.ylabel("Traffico mensile in Area C a Milano")
# plt.xticks(range(0, 12), mesi)
# plt.tight_layout()
# plt.show()

incidenti = pd.read_csv("dataset/incidenti/incidenti_2012.txt", sep='\t')
mesi_incidenti = incidenti['mese'].value_counts().sort_index()

perc_traffico = pd.DataFrame(perc_traffico)
perc_traffico.index = range(1,13)
#mesi_norm = mesi_incidenti * (1-perc_traffico[0])

# print(mesi_incidenti)
# print(perc_traffico)
# print(mesi_norm)

# plt.subplot(2,1,1)
# plt.plot(perc_traffico, color='#ddbd08')
# plt.fill_between(perc_traffico.index, perc_traffico[0], color='#ddbd08')
# plt.title("Percentuale di traffico nel mese rispetto al totale annuale")
# plt.xticks(range(1,13))
# plt.tight_layout()

# plt.subplot(2,1,2)
# plt.plot(mesi_incidenti, color='#dd5308', label="Incidenti al mese")
# plt.fill_between(mesi_incidenti.index, mesi_incidenti, color='#dd5308')
# plt.title("Incidenti normalizzati per traffico mensile")
# plt.plot(mesi_norm, color='#93dd08', label="Incidenti normalizzati")
# plt.fill_between(mesi_norm.index, mesi_norm, color='#93dd08')
# plt.title("Incidenti al mese")
# plt.legend()
# plt.xticks(range(1,13))
# plt.tight_layout()
# plt.show()



plt.subplot(2,1,1)
plt.plot(perc_traffico, color='#ddbd08')
plt.fill_between(perc_traffico.index, perc_traffico[0], color='#ddbd08')
plt.title("Percentuale di traffico nel mese rispetto al totale annuale")
plt.xticks(range(1,13))
plt.tight_layout()

plt.subplot(2,1,2)

plt.tight_layout()
plt.show()
