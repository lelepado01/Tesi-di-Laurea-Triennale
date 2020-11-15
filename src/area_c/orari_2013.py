
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

path = "dataset/area_c/orari_2016.csv"

data = pd.read_csv(path, sep=';')

ora = pd.Series()
for f in data['hour'].unique():
    ora = ora.append(
        pd.Series(data[data['hour'] == f]['totale'].sum()), 
        ignore_index=True
        )

ora_media = ora.mean()

#accessi_area_c_per_ora = ora / ora.sum()
accessi_area_c_per_ora =  ora.drop(index=24)

path = "dataset/incidenti/incidenti_2016.txt"

incidenti = pd.read_csv(path, sep="\t", encoding='latin1')
incidenti = incidenti[incidenti['Ora'] != 25]

incidenti_per_ora = incidenti[incidenti['provincia'] == 15]['Ora'].value_counts().sort_index()

incidenti_per_ora.index = range(0,24)
#incidenti_per_ora = incidenti_per_ora / incidenti_per_ora.sum()
#incidenti_per_ora_norm = incidenti_per_ora * (1 - accessi_area_c_per_ora)

# plt.subplot(3,1,1)
# plt.plot(accessi_area_c_per_ora, color='#ddbd08')
# plt.fill_between(accessi_area_c_per_ora.index, accessi_area_c_per_ora, color='#ddbd08')
# plt.xticks(range(0,24))
# plt.ylabel("Percentuale")
# plt.title("Percentuale di traffico totale")
# plt.tight_layout()

# plt.subplot(3,1,2)
# plt.plot(incidenti_per_ora, color='#dd5308', label="Incidenti per orario")
# plt.fill_between(incidenti_per_ora.index, incidenti_per_ora, color='#dd5308')
# plt.xticks(range(0,24))

# # plt.subplot(3,1,3)
# plt.plot(incidenti_per_ora_norm, color='#93dd08', label="Incidenti normalizzati")
# plt.fill_between(incidenti_per_ora_norm.index, incidenti_per_ora_norm, color='#93dd08')
# plt.title("Numero di incidenti a Milano")
# plt.ylabel("Numero incidenti")
# plt.xticks(range(0,24))
# plt.tight_layout()
# plt.show()

# Non cambia molto, prova a normalizzarlo con percentuale di 
# incremento rispetto alla media

# Calcolo correlazione: 
# print(ora.corr(incidenti_per_ora.value_counts()))
