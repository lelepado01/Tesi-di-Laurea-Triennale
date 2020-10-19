
import pandas as pd
import matplotlib.pyplot as plt

import sys
sys.path.append('src')

import label_utils

path = "dataset/incidenti/incidenti_2010.txt"
data = pd.read_csv(path, sep="\t")

# Se guardo l'agosto di milano rispetto all'agosto di una località di vacanze, cosa cambia?
# Decido di guardare tutti i mesi

#milano = data[data['provincia'] == 15]['mese'].value_counts().sort_index()
#rimini = data[data['provincia'] == 99]['mese'].value_counts().sort_index()
#
#uniti = pd.DataFrame(
#    [milano, rimini], 
#    index=['Milano', 'Rimini']
#    ).transpose()

#uniti.plot.bar()
#plt.xlabel("Incidenti nell\'anno 2010")
#plt.show()

# Milano ha decisamente più incidenti in tutti i mesi, 
# mentre rimini ha molti incidenti in Luglio e Agosto
# Si nota il calo di incidenti in Agosto a Milano, ma anche a Rimini il numero di 
# incidenti cala rispetto a Luglio...
# 
# C'è qualche località in cui il numero di incidenti supera quelli di milano?

#incidenti_per_provincia = label_utils.join_labels(data['provincia'], "dataset/incidenti/Classificazioni/provincia.csv")

# Ci sono tanti incidenti a Bari e Genova, provo a confrontarli con Milano

#genova = data[data['provincia'] == 10]['mese'].value_counts().sort_index()
#bari = data[data['provincia'] == 72]['mese'].value_counts().sort_index()

#uniti = pd.DataFrame(
#    [milano, bari], 
#    index=['Milano', 'Bari']
#    ).transpose()
#
#uniti.plot.bar()
#plt.xlabel("Incidenti nell\'anno 2010")
#plt.show()

# Sia per Genova che per Bari non si nota neanche una salta in estate...
#incidenti_per_provincia = incidenti_per_provincia.value_counts()
#incidenti_per_provincia[incidenti_per_provincia > 500].sort_values(ascending=False).plot.barh()
#plt.show()

# Napoli, Firenze, Siracusa
#napoli = data[data['provincia'] == 63]['mese'].value_counts().sort_index()
#firenze = data[data['provincia'] == 48]['mese'].value_counts().sort_index()
#siracusa = data[data['provincia'] == 89]['mese'].value_counts().sort_index()
#
#uniti = pd.DataFrame(
#    [milano, siracusa], 
#    index=['Milano', 'Siracusa']
#    ).transpose()

#uniti.plot.bar()
#plt.xlabel("Incidenti nell\'anno 2010")
#plt.show()

# Non sembra cambiare molto, i dati migliori erano quelli su rimini

# Invece in montagna?
aosta_2010 = data[data['provincia'] == 7]['mese'].value_counts().sort_index()
#aosta.plot.bar()
#plt.xlabel("Incidenti Valle d'Aosta per mese")
#plt.show()

# Si notano decisamente più incidenti in Gennaio, stagione sciistica
# (Non ho febbraio, non ci sono stati incidenti) 
# Sono comunque pochi dati

# TODO: quando ho pochi dati, controlla la tendenza con gli altri anni

# Controllo la  tendenza per tutti gli anni che ho disponibili (AOSTA)

incidenti_2011 = pd.read_csv("dataset/incidenti/incidenti_2011.txt", sep="\t")
incidenti_2012 = pd.read_csv("dataset/incidenti/incidenti_2012.txt", sep="\t")
incidenti_2013 = pd.read_csv("dataset/incidenti/incidenti_2013.txt", sep="\t")
incidenti_2015 = pd.read_csv("dataset/incidenti/incidenti_2015.txt", sep="\t", encoding='latin1')
incidenti_2016 = pd.read_csv("dataset/incidenti/incidenti_2016.txt", sep="\t", encoding='latin1')
incidenti_2018 = pd.read_csv("dataset/incidenti/incidenti_2018.txt", sep="\t", encoding='latin1')

def get_trimestre(data : pd.Series) -> pd.Series: 
    res = {1 : 0, 2 : 0, 3 : 0, 4 : 0}
    index = 0
    for _, row in data.iteritems(): 
        res[(index % 4) + 1] += row
        index += 1

    return pd.Series(res.values(), res.keys())

def get_provincia(prov : int) -> pd.DataFrame: 
    aosta_2010 = get_trimestre(data[data['provincia'] == prov]['mese'].value_counts().sort_index())
    aosta_2011 = get_trimestre(incidenti_2011[incidenti_2011['provincia'] == prov]['mese'].value_counts().sort_index())
    aosta_2012 = get_trimestre(incidenti_2012[incidenti_2012['provincia'] == prov]['mese'].value_counts().sort_index())
    aosta_2013 = get_trimestre(incidenti_2013[incidenti_2013['provincia'] == prov]['mese'].value_counts().sort_index())
    aosta_2015 = incidenti_2015[incidenti_2015['provincia'] == prov]['trimestre'].value_counts().sort_index()
    aosta_2016 = incidenti_2016[incidenti_2016['provincia'] == prov]['trimestre'].value_counts().sort_index()
    aosta_2018 = incidenti_2018[incidenti_2018['provincia'] == prov]['trimestre'].value_counts().sort_index()

    return pd.DataFrame([aosta_2010, aosta_2011, aosta_2012, aosta_2013, aosta_2015, aosta_2016, aosta_2018], ['2010', '2011', '2012', '2013', '2015', '2016', '2018']).transpose()

provs = get_provincia(7)
provs.plot.bar()
plt.xticks(rotation=0)
plt.show()

provs = get_provincia(15)
provs.plot.bar()
plt.xticks(rotation=0)
plt.show()

provs = get_provincia(99)
provs.plot.bar()
plt.xticks(rotation=0)
plt.show()