
import pandas as pd
import matplotlib.pyplot as plt

path = "dataset/incidenti/incidenti_2010.txt"
data = pd.read_csv(path, sep="\t")

#print(data['mese'].unique())

# GRAFO 1
mese = data['mese']
#print(mese.mean())
incidenti_al_mese = mese.value_counts().sort_index()
#incidenti_al_mese.plot.bar()
#plt.show()

# Noto subito che agosto, gennaio e febbraio hanno valori molto minori rispetto alla media
# Per febbraio, quanto influisce il fatto che ha 3 giorni in meno? -> 28 giorni

# Calcolo numero di incidenti al giorno
incidenti_al_giorno_per_mese = mese.value_counts().sort_index()
giorni_al_mese = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

for index in range(0, len(incidenti_al_giorno_per_mese)): 
    incidenti_al_giorno_per_mese.iloc[index] /= giorni_al_mese[index]

# GRAFO 2 
#incidenti_al_giorno_per_mese.plot.bar(xlabel="incidenti al giorno ogni mese")
#plt.show()

# Si notano dicembre, gennaio, febbraio e dicembre hanno un numero di incidenti per giorno bassi
# I mesi dopo febbraio, hanno numero di incidenti per giorno in salita, fino ad Agosto.

def get_incidenti_al_giorno_per_mese(file_path : str): 
    dati = pd.read_csv(file_path, sep="\t")
    giorni_al_mese = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    incidenti_al_giorno = dati['mese'].value_counts().sort_index()
    
    for index in range(0, len(incidenti_al_giorno)): 
        incidenti_al_giorno.iloc[index] /= giorni_al_mese[index]

    return incidenti_al_giorno

incidenti_2013 = get_incidenti_al_giorno_per_mese("dataset/incidenti/incidenti_2013.txt")
#incidenti_2013.plot.bar()
#plt.show()

# 2011 non ha basso numero in agosto, 2013 si, 
# in tutti però il numero di incidenti in gennaio, febbraio è basso, mentre 
# Maggio giugno e luglio sono sempre molto alti.

# Per 2014, 2015, 2016, 2017, 2018 non ho il dato sul mese preciso, ma ho solo il trimestre

def get_incidenti_al_giorno_per_trimestre(file_path : str): 
    dati = pd.read_csv(file_path, sep="\t", encoding='cp1252')

    giorni_al_trimestre = [31 +28+ 31, 30+ 31+30, 31+ 31+ 30, 31+ 30+ 31]

    incidenti_al_giorno = dati['trimestre'].value_counts().sort_index()
    
    for index in range(0, len(incidenti_al_giorno)): 
        incidenti_al_giorno.iloc[index] /= giorni_al_mese[index]

    return incidenti_al_giorno

# TODO: fix dei dataset 2014 e 2017

df = pd.DataFrame([
    #get_incidenti_al_giorno_per_trimestre("dataset/incidenti/incidenti_2014.txt"),
    get_incidenti_al_giorno_per_trimestre("dataset/incidenti/incidenti_2015.txt"),
    get_incidenti_al_giorno_per_trimestre("dataset/incidenti/incidenti_2016.txt"),
    #get_incidenti_al_giorno_per_trimestre("dataset/incidenti/incidenti_2017.txt"),
    get_incidenti_al_giorno_per_trimestre("dataset/incidenti/incidenti_2018.txt")
    ], index = [
        #"2014", 
        "2015", 
        "2016", 
        #"2017", 
        "2018"
    ]).transpose()

# GRAFO 3
df.plot.bar(xlabel="incidenti per trimestre")
plt.show()

# Ho omesso 2014 e 2017 perchè davano problemi durante il parsing
# Anche utilizzando i trimestri però è confermata la tendenza, Gennaio, Febbraio, Marzo con basso 
# volume, mentre Aprile, Maggio e Giugno più alti 

# Perchè?
# Il primo trimestre ha un basso numero di incidenti probabilmente perchè è inverno