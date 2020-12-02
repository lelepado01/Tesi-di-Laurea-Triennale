
import pandas as pd
import matplotlib.pyplot as plt
import sys
sys.path.append('src')
import label_utils

path = "dataset/incidenti/incidenti_2018.txt"

data = pd.read_csv(path, sep="\t")

pedoni_morti = data['pedone_morto_1__et_']
pedoni_morti = pedoni_morti.value_counts().sort_index()

pedoni_feriti = data['pedone_ferito_1__et_']
pedoni_feriti = pedoni_feriti.value_counts().sort_index()

anni_per_fascia_feriti = pd.Series([5,5,3,3,4,5 ,15,10,5,5 ,5,20,1])
anni_per_fascia_morti = pd.Series( [5,5,3,4,5,15,10,5, 5,20,1])

# print(pedoni_morti)
# print(popolazione_std)

# import numpy as np

# pedoni_feriti_vals = pedoni_feriti.values / np.array(anni_per_fascia_feriti)
# pedoni_morti_vals = pedoni_morti.values / np.array(anni_per_fascia_morti)

# pedoni_feriti_norm = pd.Series(pedoni_feriti_vals, index=pedoni_feriti.index)
# pedoni_morti_norm = pd.Series(pedoni_morti_vals, index=pedoni_morti.index)

correct_order = ['0-5  ','6-9  ','10-14', '15-17', '18-29', '30-44', '45-54', '55-64','65+  ']

pedoni_feriti = pedoni_feriti[pedoni_feriti < 10000]
pedoni_feriti = pedoni_feriti[pedoni_feriti.index != 'n.i. ']
pedoni_feriti = pedoni_feriti.reindex(correct_order)

pedoni_morti = pedoni_morti[pedoni_morti < 1000]
pedoni_morti = pedoni_morti[pedoni_morti.index != 'n.i. ']
pedoni_morti = pedoni_morti.reindex(correct_order)
# pedoni_feriti_norm = pedoni_feriti_norm[:-1]
# pedoni_morti_norm = pedoni_morti_norm[:-1]

# 
# plt.subplot(223)
# plt.fill_between(pedoni_feriti_norm.index, pedoni_feriti_norm, color="#a1ce71")
# plt.xticks(rotation=90)
# plt.title("Pedoni feriti normalizzati")
# plt.tight_layout()

# plt.subplot(224)
# plt.xticks(rotation=90)
# plt.fill_between(pedoni_morti_norm.index, pedoni_morti_norm, color='#ce9e71')
# plt.title("Pedoni morti normalizzati")
# plt.tight_layout()

plt.show()
