
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

path = "dataset/area_c/orari_2013.csv"

data = pd.read_csv(path, sep=';')

ora = pd.Series()
for f in data['hour'].unique():
    ora = ora.append(
        pd.Series(data[data['hour'] == f]['totale'].sum()), 
        ignore_index=True
        )

ora_media = ora.mean()

#ora_perc = ora / ora.sum()
#ora_perc.index = range(1,25)
# ora_perc_inc = ora / ora_media *100 -100

# print(ora_perc)
# print(ora_perc_inc)

# plt.subplot(2,1,1)
# plt.plot(ora_perc)
# # plt.subplot(2,1,2)
# # plt.plot(ora_perc_inc)
# plt.show()


path = "dataset/incidenti/incidenti_2010.txt"

data = pd.read_csv(path, sep="\t")
data = data[data['ora'] != 25]

ora_week_milano = data[data['provincia'] == 15]['ora'].value_counts().sort_index()

#ora_week_milano_norm = ora_week_milano * (1 - ora_perc)
ora_week_milano_norm = ora_week_milano / ora

plt.subplot(3,1,1)
plt.plot(ora, color='#ddbd08')
plt.fill_between(ora.index, ora, color='#ddbd08')
plt.xticks(range(1,25))
plt.ylabel("Percentuale")
plt.title("Percentuale di traffico totale")
plt.tight_layout()
plt.subplot(3,1,2)
plt.plot(ora_week_milano, color='#dd5308', label="Incidenti per orario")
plt.fill_between(ora_week_milano.index, ora_week_milano, color='#dd5308')
plt.subplot(3,1,3)
plt.plot(ora_week_milano_norm, color='#93dd08', label="Incidenti normalizzati")
plt.fill_between(ora_week_milano_norm.index, ora_week_milano_norm, color='#93dd08')
plt.title("Numero di incidenti a Milano")
plt.ylabel("Numero incidenti")
plt.xticks(range(1,25))
plt.tight_layout()
plt.show()

# print(ora_perc.corr(ora_week_milano_norm))

# Non cambia molto, prova a normalizzarlo con percentuale di 
# incremento rispetto alla media