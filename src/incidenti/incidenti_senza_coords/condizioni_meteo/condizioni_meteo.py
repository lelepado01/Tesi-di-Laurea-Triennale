
import pandas as pd
import matplotlib.pyplot as plt

path = "dataset/incidenti/incidenti_2010.txt"

data = pd.read_csv(path, sep="\t")
meteo = data['condizioni_meteorologiche']
#print(data['condizioni_meteorologiche'].unique())

#print(meteo.value_counts())

#meteo.value_counts().plot.bar()
#plt.show()

# Ho bisogno di sapere quanto tempo c'è stato sereno a milano nel 2010, altrimenti non ho contesto
# ilmeteo.it ha un archivio del meteo di milano per giorno del mese
# https://www.ilmeteo.it/portale/archivio-meteo/Milano/2010/

path_meteo = "dataset/meteo/ilmeteo2010/Milano-2010-Luglio.csv"

dati_meteo = pd.read_csv(path_meteo, sep=';')
dati_meteo
print(dati_meteo['FENOMENI'].value_counts())

# creo funzione per sapere la percentuale dei giorni in cui sono avvenuti fenomeni particolari