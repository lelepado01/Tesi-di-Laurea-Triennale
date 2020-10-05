
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

dati_meteo = pd.read_csv(path_meteo, sep=';').fillna("sereno") 

#print(dati_meteo['FENOMENI'].value_counts())

# creo funzione per sapere la percentuale dei giorni in cui sono avvenuti fenomeni particolari

paths = [
    "dataset/meteo/ilmeteo2010/Milano-2010-Gennaio.csv",
    "dataset/meteo/ilmeteo2010/Milano-2010-Febbraio.csv",
    "dataset/meteo/ilmeteo2010/Milano-2010-Marzo.csv",
    "dataset/meteo/ilmeteo2010/Milano-2010-Aprile.csv",
    "dataset/meteo/ilmeteo2010/Milano-2010-Maggio.csv",
    "dataset/meteo/ilmeteo2010/Milano-2010-Giugno.csv",
    "dataset/meteo/ilmeteo2010/Milano-2010-Luglio.csv",
    "dataset/meteo/ilmeteo2010/Milano-2010-Agosto.csv",
    "dataset/meteo/ilmeteo2010/Milano-2010-Settembre.csv",
    "dataset/meteo/ilmeteo2010/Milano-2010-Ottobre.csv",
    "dataset/meteo/ilmeteo2010/Milano-2010-Novembre.csv",
    "dataset/meteo/ilmeteo2010/Milano-2010-Dicembre.csv",
]

def add_values_to_dict(dictionary : dict, df : pd.Series): 
    for index, val in zip(df.index, df.values): 
        if index in dictionary: 
            dictionary[index] = dictionary[index] + val
        else: 
            dictionary[index] = val

    return dictionary

percentuali_annuali = {}
for path in paths: 
    dati_meteo = pd.read_csv(path, sep=';').fillna("sereno") 
    percentuali_annuali = add_values_to_dict(percentuali_annuali, dati_meteo['FENOMENI'].value_counts()) 

#print(percentuali_annuali)

# posso controllare se la funzione è giusta sommando le istanze
#print(sum(list(percentuali_annuali.values())))
# restituisce 365 giorni

# Ora normalizzo
for k, v in zip(percentuali_annuali.keys(), percentuali_annuali.values()): 
    percentuali_annuali[k] = v / 365

print(percentuali_annuali)

# è stato sereno il 40% delle giornate durante il 2010
# IMP: il dataset di ilmeteo non tiene conto di grandine, mentre il dataset istat si

