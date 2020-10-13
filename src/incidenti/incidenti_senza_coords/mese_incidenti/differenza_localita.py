
import pandas as pd
import matplotlib.pyplot as plt

import sys
sys.path.append('src')

import label_utils

path = "dataset/incidenti/incidenti_2010.txt"
data = pd.read_csv(path, sep="\t")

# Se guardo l'agosto di milano rispetto all'agosto di una località di vacanze, cosa cambia?
# Decido di guardare tutti i mesi

milano = data[data['provincia'] == 15]['mese'].value_counts().sort_index()
rimini = data[data['provincia'] == 99]['mese'].value_counts().sort_index()

uniti = pd.DataFrame(
    [milano, rimini], 
    index=['Milano', 'Rimini']
    ).transpose()

#uniti.plot.bar()
#plt.xlabel("Incidenti nell\'anno 2010")
#plt.show()

# Milano ha decisamente più incidenti in tutti i mesi, 
# mentre rimini ha molti incidenti in Luglio e Agosto
# Si nota il calo di incidenti in Agosto a Milano, ma anche a Rimini il numero di 
# incidenti cala rispetto a Luglio...
# 
# C'è qualche località in cui il numero di incidenti supera quelli di milano?

incidenti_per_provincia = label_utils.join_labels(data['provincia'], "dataset/incidenti/Classificazioni/provincia.csv")

# Ci sono tanti incidenti a Bari e Genova, provo a confrontarli con Milano

genova = data[data['provincia'] == 10]['mese'].value_counts().sort_index()
bari = data[data['provincia'] == 72]['mese'].value_counts().sort_index()

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
napoli = data[data['provincia'] == 63]['mese'].value_counts().sort_index()
firenze = data[data['provincia'] == 48]['mese'].value_counts().sort_index()
siracusa = data[data['provincia'] == 89]['mese'].value_counts().sort_index()

uniti = pd.DataFrame(
    [milano, siracusa], 
    index=['Milano', 'Siracusa']
    ).transpose()

#uniti.plot.bar()
#plt.xlabel("Incidenti nell\'anno 2010")
#plt.show()

# Non sembra cambiare molto, i dati migliori erano quelli su rimini

# Invece in montagna?
aosta = data[data['provincia'] == 7]['mese'].value_counts().sort_index()
#aosta.plot.bar()
#plt.xlabel("Incidenti Valle d'Aosta per mese")
#plt.show()

# Si notano decisamente più incidenti in Gennaio, stagione sciistica
# (Non ho febbraio, non ci sono stati incidenti) 
# Sono comunque pochi dati

# TODO: quando ho pochi dati, controlla la tendenza con gli altri anni