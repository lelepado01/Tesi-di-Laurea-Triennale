
import pandas as pd
import matplotlib.pyplot as plt
import sys 
sys.path.append("src/")

import label_utils

path = "dataset/incidenti/incidenti_2011.txt"

data : pd.DataFrame = pd.read_csv(path, sep="\t")

intersezione = data['intersezione_o_non_interse1']
intersezione_labels = label_utils.join_labels(
    intersezione, 
    "dataset/incidenti/Classificazioni/intersezione_o_non_interse3.csv"
    ).value_counts().sort_index()

#print(intersezione_labels)

intersezione_labels = intersezione_labels[intersezione_labels > 200]

# GRAFO 4
intersezione_labels.plot.barh(color='#92ba4e', width=0.9)
plt.xlabel("Incidenti all'anno (2011)")
plt.tight_layout()
plt.show()