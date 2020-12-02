
import pandas as pd
import matplotlib.pyplot as plt
import sys
sys.path.append('src')
import label_utils

path = "dataset/incidenti/incidenti_2018.txt"

data = pd.read_csv(path, sep="\t")

fields = ['intersezione_o_non_interse3', 'pedone_ferito_1__sesso', 'pedone_ferito_2__sesso', 'pedone_ferito_3__sesso', 'pedone_ferito_4__sesso']
incidenti_pedoni = data[fields]
incidenti_pedoni = incidenti_pedoni[incidenti_pedoni['pedone_ferito_1__sesso'] != ' ']

def count_people(row, campi) -> int: 
    count = 0
    for field in campi: 
        if row[field] != ' ' and row[field] != '':
            count += 1

    return count

def get_people(dataset : pd.DataFrame, campi): 
    res = {}
    for index in range(0, len(dataset)): 
        res[index] = 0

    for index, row in dataset.iterrows(): 
        res[index] = count_people(row, campi)

    return pd.Series(res)

fields.remove('intersezione_o_non_interse3')
pedoni_feriti = get_people(incidenti_pedoni, fields)
incidenti_pedoni = pd.DataFrame([incidenti_pedoni['intersezione_o_non_interse3'], pedoni_feriti], ['tipo_incrocio', 'pedoni_feriti']).transpose()
incidenti_pedoni = incidenti_pedoni[incidenti_pedoni['pedoni_feriti'] != 0]

incidenti_labels = label_utils.join_labels(incidenti_pedoni['tipo_incrocio'], 'dataset/incidenti/Classificazioni/intersezione_o_non_interse3.csv')
incidenti_pedoni = pd.DataFrame([incidenti_labels, incidenti_pedoni['pedoni_feriti']], ['tipo_incrocio', 'pedoni_feriti']).transpose()

tab = pd.DataFrame(pd.crosstab(incidenti_pedoni['tipo_incrocio'], incidenti_pedoni['pedoni_feriti'])).transpose()
tab.index = tab.index.astype(int)

import heatmap as H

fig, ax = plt.subplots()

im, cbar = H.heatmap(tab, tab.index, tab.columns, ax=ax, xticks_rotated=True,
                   cmap="YlGn", cbarlabel="Incidenti all'anno (2018)")
texts = H.annotate_heatmap(im, valfmt="{x}")
fig.tight_layout()
plt.show()