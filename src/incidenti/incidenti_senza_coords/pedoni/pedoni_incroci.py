
import pandas as pd
import matplotlib.pyplot as plt
import sys
sys.path.append('src')
import label_utils
import istat_utils
import heatmap as H

path = "dataset/incidenti/istat/incidenti_2018.txt"
data = pd.read_csv(path, sep="\t")

fields = ['intersezione_o_non_interse3', 'pedone_ferito_1__sesso', 'pedone_ferito_2__sesso', 'pedone_ferito_3__sesso', 'pedone_ferito_4__sesso']
incidenti_pedoni = data[fields]
fields.remove('intersezione_o_non_interse3')

# Pulizia dataset da valori nulli
incidenti_pedoni = incidenti_pedoni[incidenti_pedoni['pedone_ferito_1__sesso'] != ' ']

# Conteggio pedoni e conversione degli indici numerici degli incroci in testo
pedoni_feriti = istat_utils.get_people(incidenti_pedoni, fields)
incidenti_pedoni = pd.DataFrame([incidenti_pedoni['intersezione_o_non_interse3'], pedoni_feriti], ['tipo_incrocio', 'pedoni_feriti']).transpose()
incidenti_pedoni = incidenti_pedoni[incidenti_pedoni['pedoni_feriti'] != 0]

incidenti_labels = label_utils.join_labels(incidenti_pedoni['tipo_incrocio'], 'dataset/incidenti/istat/Classificazioni/intersezione_o_non_interse3.csv')
incidenti_pedoni = pd.DataFrame([incidenti_labels, incidenti_pedoni['pedoni_feriti']], ['tipo_incrocio', 'pedoni_feriti']).transpose()

pedoni_contati = pd.DataFrame(pd.crosstab(incidenti_pedoni['tipo_incrocio'], incidenti_pedoni['pedoni_feriti'])).transpose()
pedoni_contati.index = pedoni_contati.index.astype(int)

fig, ax = plt.subplots()
im = H.heatmap(
    pedoni_contati, 
    pedoni_contati.index, 
    pedoni_contati.columns, 
    ax=ax, 
    xticks_rotated=True,
    cmap="YlGn", 
    cbar_visible=False
    )
texts = H.annotate_heatmap(im, valfmt="{x}")
plt.ylabel("Numero di pedoni coinvolti")
fig.tight_layout()
plt.show()