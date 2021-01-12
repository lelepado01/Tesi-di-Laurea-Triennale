
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

path = "dataset/incidenti/istat/incidenti_2018.txt"

data = pd.read_csv(path, sep="\t")

pedoni_morti = data['pedone_morto_1__et_']
pedoni_morti = pedoni_morti.value_counts().sort_index()

pedoni_feriti = data['pedone_ferito_1__et_']
pedoni_feriti = pedoni_feriti.value_counts().sort_index()

# Ordine corretto, altrimenti '6-9' risulta successivo in ordine alfabetico
correct_order = ['0-5  ','6-9  ','10-14', '15-17', '18-29', '30-44', '45-54', '55-64','65+  ']
numero_anni = np.array([5, 5, 5, 3, 10, 15, 10, 10, 20])

#Pulizia dataset da campi inutli in grafico
pedoni_feriti = pedoni_feriti[pedoni_feriti.index != '     ']
pedoni_feriti = pedoni_feriti[pedoni_feriti.index != 'n.i. ']
pedoni_feriti = pedoni_feriti.reindex(correct_order)

pedoni_morti = pedoni_morti[pedoni_morti.index != '     ']
pedoni_morti = pedoni_morti[pedoni_morti.index != 'n.i. ']
pedoni_morti = pedoni_morti.reindex(correct_order)

# Normalizzazione di risultati in base agli anni presenti in fasce di età
pedoni_feriti_vals = pedoni_feriti.values / numero_anni
pedoni_morti_vals = pedoni_morti.values / numero_anni

pedoni_feriti = pd.Series(pedoni_feriti_vals, index=pedoni_feriti.index)
pedoni_morti = pd.Series(pedoni_morti_vals, index=pedoni_morti.index)

plt.subplot(121)
plt.fill_between(pedoni_feriti.index, pedoni_feriti, color="#5578d1")
plt.xticks(rotation=90)
plt.ylabel("Numero pedoni feriti / anni fascia")
plt.tight_layout()

plt.subplot(122)
plt.xticks(rotation=90)
plt.fill_between(pedoni_morti.index, pedoni_morti, color='#d15578')
plt.ylabel("Numero pedoni morti / anni fascia")
plt.tight_layout()

plt.show()
