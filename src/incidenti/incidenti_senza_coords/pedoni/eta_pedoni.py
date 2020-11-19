
import pandas as pd
import matplotlib.pyplot as plt
import sys
sys.path.append('src')
import label_utils

path = "dataset/incidenti/incidenti_2011.txt"

data = pd.read_csv(path, sep="\t")

pedoni_morti = data['pedone_morto_1__et_']
pedoni_morti = pedoni_morti[pedoni_morti != '  '].astype(int)
pedoni_morti = label_utils.join_labels(pedoni_morti, 'dataset/incidenti/Classificazioni/veicolo__a___et__conducente.csv')
pedoni_morti = pedoni_morti.value_counts().sort_index()

pedoni_feriti = data['pedone_ferito_1__et_']
pedoni_feriti = pedoni_feriti[pedoni_feriti != '  '].astype(int)
pedoni_feriti = label_utils.join_labels(pedoni_feriti, 'dataset/incidenti/Classificazioni/veicolo__a___et__conducente.csv')
pedoni_feriti = pedoni_feriti.value_counts().sort_index()

anni_per_fascia_feriti = pd.Series([5,5,3,3,4,5,15,10,5,5,5,20,1])
anni_per_fascia_morti = pd.Series([5,5,3,4,5,15,10,5,5,20,1])

# print(pedoni_morti)
# print(popolazione_std)

import numpy as np

pedoni_feriti_vals = pedoni_feriti.values / np.array(anni_per_fascia_feriti)
pedoni_morti_vals = pedoni_morti.values / np.array(anni_per_fascia_morti)

pedoni_feriti_norm = pd.Series(pedoni_feriti_vals, index=pedoni_feriti.index)
pedoni_morti_norm = pd.Series(pedoni_morti_vals, index=pedoni_morti.index)

pedoni_feriti = pedoni_feriti[:-1]
pedoni_morti = pedoni_morti[:-1]
pedoni_feriti_norm = pedoni_feriti_norm[:-1]
pedoni_morti_norm = pedoni_morti_norm[:-1]

plt.subplot(221)
plt.xticks(rotation=90)
plt.fill_between(pedoni_feriti.index, pedoni_feriti, color='#a1ce71')
plt.title("Pedoni feriti")
plt.tight_layout()

plt.subplot(222)
plt.xticks(rotation=90)
plt.fill_between(pedoni_morti.index, pedoni_morti, color='#ce9e71')
plt.title("Pedoni morti")
plt.tight_layout()

plt.subplot(223)
plt.fill_between(pedoni_feriti_norm.index, pedoni_feriti_norm, color="#a1ce71")
plt.xticks(rotation=90)
plt.title("Pedoni feriti normalizzati")
plt.tight_layout()

plt.subplot(224)
plt.xticks(rotation=90)
plt.fill_between(pedoni_morti_norm.index, pedoni_morti_norm, color='#ce9e71')
plt.title("Pedoni morti normalizzati")
plt.tight_layout()

plt.show()
