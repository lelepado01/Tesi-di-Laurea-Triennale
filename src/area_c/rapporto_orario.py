
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

path = "dataset/incidenti/incidenti_2016.txt"

incidenti = pd.read_csv(path, sep="\t", encoding='latin1')
incidenti = incidenti[incidenti['Ora'] != 25]

incidenti_per_ora = incidenti[incidenti['provincia'] == 15]['Ora'].value_counts().sort_index()

incidenti_per_ora.index = range(0,24)

ora_media = ora.mean()

accessi_area_c_per_ora =  ora.drop(index=24)

plt.subplot(1,2,1)
plt.fill_between(accessi_area_c_per_ora.index, accessi_area_c_per_ora / accessi_area_c_per_ora.sum(), color='#66ad9f')
plt.xticks(range(0,24, 2))
plt.ylabel("Percentuale di traffico in Area C")
plt.tight_layout()

rapp_inc_traff = incidenti_per_ora / accessi_area_c_per_ora

plt.subplot(1,2,2)
plt.fill_between(rapp_inc_traff.index, rapp_inc_traff, color='#9f66ad')
plt.ylabel("Rapporto tra incidenti e traffico")
plt.xticks(range(0,24, 2))
plt.tight_layout()

plt.show()