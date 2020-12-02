
import pandas as pd
import matplotlib.pyplot as plt

path = "dataset/incidenti/incidenti_2018.txt"

data = pd.read_csv(path, sep="\t")

pedoni_morti = data['pedone_morto_1__et_']
pedoni_morti = pedoni_morti.value_counts().sort_index()

pedoni_feriti = data['pedone_ferito_1__et_']
pedoni_feriti = pedoni_feriti.value_counts().sort_index()

correct_order = ['0-5  ','6-9  ','10-14', '15-17', '18-29', '30-44', '45-54', '55-64','65+  ']

pedoni_feriti = pedoni_feriti[pedoni_feriti.index != '     ']
pedoni_feriti = pedoni_feriti[pedoni_feriti.index != 'n.i. ']
pedoni_feriti = pedoni_feriti.reindex(correct_order)

pedoni_morti = pedoni_morti[pedoni_morti.index != '     ']
pedoni_morti = pedoni_morti[pedoni_morti.index != 'n.i. ']
pedoni_morti = pedoni_morti.reindex(correct_order)

plt.subplot(121)
plt.xticks(rotation=90)
plt.fill_between(pedoni_feriti.index, pedoni_feriti, color='#a1ce71')
plt.ylabel("Numero pedoni feriti")
plt.tight_layout()

plt.subplot(122)
plt.xticks(rotation=90)
plt.fill_between(pedoni_morti.index, pedoni_morti, color='#ce9e71')
plt.ylabel("Numero pedoni morti")
plt.tight_layout()

plt.show()