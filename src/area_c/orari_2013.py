
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

# ora_media = ora.mean()

# accessi_area_c_per_ora = ora / ora.sum()
# accessi_area_c_per_ora.index = range(1,25)
# perc_ora_inc = ora / ora_media *100 -100

# print(accessi_area_c_per_ora)
# print(perc_ora_inc)

# plt.subplot(2,1,1)
# plt.plot(accessi_area_c_per_ora)
# # plt.subplot(2,1,2)
# # plt.plot(perc_ora_inc)
# plt.show()


path = "dataset/incidenti/incidenti_2010.txt"

incidenti = pd.read_csv(path, sep="\t")
incidenti = incidenti[incidenti['ora'] != 25]

incidenti_per_ora = incidenti[incidenti['provincia'] == 15]['ora']#.value_counts().sort_index()


#incidenti_per_ora_norm = incidenti_per_ora * (1 - accessi_area_c_per_ora)
#incidenti_per_ora_norm = incidenti_per_ora / ora

#print(accessi_area_c_per_ora.corr(incidenti_per_ora))

print(ora.corr(incidenti_per_ora.value_counts()))


# plt.subplot(3,1,1)
# plt.plot(ora, color='#ddbd08')
# plt.fill_between(ora.index, ora, color='#ddbd08')
# plt.xticks(range(1,25))
# plt.ylabel("Percentuale")
# plt.title("Percentuale di traffico totale")
# plt.tight_layout()
# plt.subplot(3,1,2)
# plt.plot(incidenti_per_ora, color='#dd5308', label="Incidenti per orario")
# plt.fill_between(incidenti_per_ora.index, incidenti_per_ora, color='#dd5308')
# plt.subplot(3,1,3)
# plt.plot(incidenti_per_ora_norm, color='#93dd08', label="Incidenti normalizzati")
# plt.fill_between(incidenti_per_ora_norm.index, incidenti_per_ora_norm, color='#93dd08')
# plt.title("Numero di incidenti a Milano")
# plt.ylabel("Numero incidenti")
# plt.xticks(range(1,25))
# plt.tight_layout()
# plt.show()


# Non cambia molto, prova a normalizzarlo con percentuale di 
# incremento rispetto alla media