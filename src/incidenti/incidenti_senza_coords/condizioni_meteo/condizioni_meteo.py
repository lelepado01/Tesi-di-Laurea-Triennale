
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

# Sostituisco tutti i valori "" con 'sereno' 
dati_meteo_ilmeteo = pd.read_csv(path_meteo, sep=';').fillna("sereno")['FENOMENI']

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
    "dataset/meteo/ilmeteo2010/Milano-2010-Dicembre.csv"
]

def add_values_to_dict(dictionary : dict, df : pd.Series): 
    indici = ['sereno', 'pioggia', 'temporale', 'neve', 'nebbia']
    for index, val in zip(df.index, df.values): 
        if index in dictionary: 
            dictionary[index] = dictionary[index] + val
        elif index in indici: 
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

#print(percentuali_annuali)

# è stato sereno il 40% delle giornate durante il 2010
# IMP: il dataset di ilmeteo non tiene conto di grandine, mentre il dataset istat si

# Se moltiplico percentuali_annuali per i dati del meteo: 
# Mi interessano sereno, pioggia, neve e nebbia

number_to_label = {
    1 : "sereno", 
    2 : "nebbia", 
    3 : "pioggia", 
    5 : "neve"
}

#print(percentuali_annuali)
#print(meteo.value_counts())

incidenti_pesati = {}
for index, val in zip(meteo.value_counts().index, meteo.value_counts()):
    if index in number_to_label.keys(): 
        incidenti_pesati[number_to_label.get(index)] = val * (1- percentuali_annuali[number_to_label.get(index)])

#print(incidenti_pesati)

#pd.Series(incidenti_pesati).plot.bar()
#plt.show()

# Il grafo non mi dice molto... potrei calcolare il coeff. di pearson delle due variabili
# ma devo fare in modo che sia possibile calcolare la covarianza tra i due set

# Devo trasfrormare gli indici str in valori numerici per poter calcolare 
# varianza e covarianza

meteo_2010 = pd.Series()
for path in paths: 
    m = pd.read_csv(path, sep=";")['FENOMENI']
    meteo_2010 = meteo_2010.append(m)

meteo_2010 = meteo_2010.fillna(1).replace("nebbia", 2).replace("pioggia nebbia", 2).replace("pioggia neve nebbia", 2).replace("pioggia temporale nebbia", 3).replace("pioggia", 3).replace("temporale", 3).replace("pioggia temporale", 3).replace("neve", 5).replace("pioggia neve", 5).replace("neve nebbia", 5)

# Ora posso calcolare la varianza: 

#print(meteo_2010.var())
#print(meteo.var())
#print(meteo_2010.cov(meteo))
#print(meteo_2010.cov(meteo) / (meteo.var() * meteo_2010.var()))

# Il coeff. di Pearson tende a 0, le variabili sono non correlate

# Siamo sicuri? 
# Tento di calcolare la percentiale di incidenti in giorni sereni vs giorni di pioggia

incidenti_con_condizioni = meteo[(meteo != 4) & (meteo < 6)]
print(incidenti_con_condizioni.value_counts().sort_index()) # numero di incidenti
print(meteo_2010.value_counts().sort_index())               # numero di giorni con le condizioni

# Se divido le due serie trovo il numero di incidenti al giorno per la rispettiva giornata

incidenti_per_condizione = incidenti_con_condizioni.value_counts().sort_index() / meteo_2010.value_counts().sort_index()
print(incidenti_per_condizione)

# Concluderei che non c'è molta correlazione tra meteo e incidenti, almeno a milano, 
# dove è sereno spesso e ci sono molti altri fattori in gioco 