
import pandas as pd
import matplotlib.pyplot as plt

path = "dataset/incidenti/istat/incidenti_2018.txt"
# Ordine corretto delle età, altrimenti '6-9' risulta dopo in ordine alfabetico
correct_order = ['0-5  ','6-9  ','10-14', '15-17', '18-29', '30-44', '45-54', '55-64','65+  ']

data = pd.read_csv(path, sep="\t")

pedoni_morti = data['pedone_morto_1__et_']
pedoni_morti = pedoni_morti.value_counts().sort_index()

pedoni_feriti = data['pedone_ferito_1__et_']
pedoni_feriti = pedoni_feriti.value_counts().sort_index()

# Pulizia del dataset da campi non utili
# e sort in base all'ordine corretto
pedoni_feriti = pedoni_feriti[pedoni_feriti.index != '     ']
pedoni_feriti = pedoni_feriti[pedoni_feriti.index != 'n.i. ']
pedoni_feriti = pedoni_feriti.reindex(correct_order)

pedoni_morti = pedoni_morti[pedoni_morti.index != '     ']
pedoni_morti = pedoni_morti[pedoni_morti.index != 'n.i. ']
pedoni_morti = pedoni_morti.reindex(correct_order)

plt.subplot(121)
plt.xticks(rotation=90)
plt.fill_between(pedoni_feriti.index, pedoni_feriti, color='#5578d1')
plt.ylabel("Numero pedoni feriti")
plt.tight_layout()

plt.subplot(122)
plt.xticks(rotation=90)
plt.fill_between(pedoni_morti.index, pedoni_morti, color='#d15578')
plt.ylabel("Numero pedoni morti")
plt.tight_layout()

plt.show()