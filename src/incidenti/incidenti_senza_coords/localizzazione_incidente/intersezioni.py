
import pandas as pd
import matplotlib.pyplot as plt
import sys 
sys.path.append("src/")

import label_utils

path = "dataset/incidenti/istat/incidenti_2018.txt"

data : pd.DataFrame = pd.read_csv(path, sep="\t", encoding='latin1')

intersezione = data['intersezione_o_non_interse3']
intersezione_labels = label_utils.join_labels(
    intersezione, 
    "dataset/incidenti/istat/Classificazioni/intersezione_o_non_interse3.csv"
    ).value_counts().sort_index()

#print(intersezione_labels)

# intersezione_labels = intersezione_labels[intersezione_labels > 200]

intersezione_labels /= intersezione_labels.sum()
intersezione_labels = intersezione_labels.sort_index()

######################

data = pd.read_csv("dataset/incidenti/istat/incidenti_2018.txt", sep="\t", encoding='latin1')

incr = 'intersezione_o_non_interse3'
morti = ['morti_entro_24_ore', 'morti_entro_30_giorni']

data['morti'] = data[morti[0]] + data[morti[1]]

df = {}
for inc in data[incr].unique(): 
    df[inc] = 0

for inc, morti in zip(data[incr], data['morti']): 
    df[inc] += morti

indice_mort = pd.Series(df.values(),index =  df.keys()).sort_index()

num_incr = data[incr].value_counts().sort_index()

mortalita = pd.DataFrame([indice_mort * 100 / num_incr], 
    index=['indice']
).transpose()

mortalita['incrocio'] = mortalita.index

import sys
sys.path.append("src")
import label_utils

mortalita['incrocio'] = label_utils.join_labels(mortalita['incrocio'], "dataset/incidenti/istat/Classificazioni/intersezione_o_non_interse3.csv")

mortalita['indice'] /= mortalita['indice'].sum()
mortalita.index = mortalita['incrocio']
mortalita = mortalita['indice']

df = pd.DataFrame([intersezione_labels, mortalita], ['Numero di incidenti', 'Indice di mortalità']).transpose()

######################

# GRAFO 4
intersezione_labels.plot.barh(color=['#77aa66'], width=0.9)
plt.xlabel("Percercentuale di incidenti totali per tipo di incrocio (2018)")
plt.ylabel("")
plt.tight_layout()
plt.show()