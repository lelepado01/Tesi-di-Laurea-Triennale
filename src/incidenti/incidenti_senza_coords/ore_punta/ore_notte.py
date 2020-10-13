
# IMPORTANTE: dati su tutta ITALIA

import pandas as pd
import matplotlib.pyplot as plt

def get_ore_notte(data, provincia=None, label = None): 
    data = data[data['ora'] != 25]
    notte = data[(data['ora'] < 7) | (data['ora'] > 22)]

    if not provincia is None:
        notte = notte[notte['provincia'] == provincia]

    ora_notte_weekend = notte[notte['giorno_settimana'] > 5]['ora'].value_counts().sort_index()
    ora_notte_week = notte[notte['giorno_settimana'] < 6]['ora'].value_counts().sort_index()

    uniti = pd.DataFrame([
        ora_notte_week / 5, 
        ora_notte_weekend / 2
    ], index=['week', 'weekend']).transpose()

    uniti.plot.bar()
    if not label is None:
        plt.xlabel(label)
    plt.show()

path = "dataset/incidenti/incidenti_2010.txt"

data = pd.read_csv(path, sep="\t")

#get_ore_notte(data, label="Ore Notte")
get_ore_notte(data, 15, label="Ore Notte Milano")
get_ore_notte(data, 99, label="Ore Notte Rimini")

# Prendendo solo gli incidenti in milano, il grafo coincide
# Non cambia molto in altre località... ma la quantità di dati non è molta