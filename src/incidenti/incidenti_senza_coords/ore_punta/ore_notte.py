
# IMPORTANTE: dati su tutta ITALIA

import pandas as pd
import matplotlib.pyplot as plt

path = "dataset/incidenti/incidenti_2010.txt"

data = pd.read_csv(path, sep="\t")
data = data[data['ora'] != 25]
#print(data.unique())

notte = data[(data['ora'] < 7) | (data['ora'] > 22)]
#notte = notte[notte['provincia'] == 15]
ora_notte_weekend = notte[notte['giorno_settimana'] > 5]['ora'].value_counts().sort_index()
ora_notte_week = notte[notte['giorno_settimana'] < 6]['ora'].value_counts().sort_index()

uniti = pd.DataFrame([
    ora_notte_week / 5, 
    ora_notte_weekend / 2
], index=['week', 'weekend']).transpose()

#print(uniti)

uniti.plot.bar()
plt.xlabel("Ore Notturne")
plt.show()

# Prendendo solo gli incidenti in milano, il grafo coincide

