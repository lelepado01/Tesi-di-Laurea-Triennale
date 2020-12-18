
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

path = "dataset/incidenti/incidenti_2018.txt"

data = pd.read_csv(path, sep="\t")

pedoni_morti = data['pedone_morto_1__et_']
pedoni_morti = pedoni_morti.value_counts().sort_index()

pedoni_feriti = data['pedone_ferito_1__et_']
pedoni_feriti = pedoni_feriti.value_counts().sort_index()

pedoni_morti = pedoni_morti[pedoni_morti.index != '     ']
pedoni_morti = pedoni_morti[pedoni_morti.index != 'n.i. ']
pedoni_feriti = pedoni_feriti[pedoni_feriti.index != '     ']
pedoni_feriti = pedoni_feriti[pedoni_feriti.index != 'n.i. ']

correct_order =         ['0-5  ', '6-9  ', '10-14', '15-17', '18-29', '30-44', '45-54', '55-64','65+  ']
perc_fascia = np.array( [3.9, 4.5, 4.8, 3.1, 2.8+4+5.3, 19, 18.2, 7.3+6.4, 19.3]) / 100

pedoni_feriti_vals = pedoni_feriti.values / perc_fascia
pedoni_morti_vals = pedoni_morti.values / perc_fascia

pedoni_feriti = pd.Series(pedoni_feriti_vals, index=pedoni_feriti.index)
pedoni_morti = pd.Series(pedoni_morti_vals, index=pedoni_morti.index)

pedoni_feriti = pedoni_feriti.reindex(correct_order)
pedoni_morti = pedoni_morti.reindex(correct_order)

plt.subplot(121)
plt.fill_between(pedoni_feriti.index, pedoni_feriti, color="#5578d1")
plt.xticks(rotation=90)
plt.ylabel("Pedoni feriti per\npercentuale di età")
plt.tight_layout()

plt.subplot(122)
plt.xticks(rotation=90)
plt.fill_between(pedoni_morti.index, pedoni_morti, color='#d15578')
plt.ylabel("Pedoni morti per\npercentuale di età")
plt.tight_layout()
plt.show()
