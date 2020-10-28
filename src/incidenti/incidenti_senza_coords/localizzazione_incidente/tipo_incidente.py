
import pandas as pd
import matplotlib.pyplot as plt
import sys 
sys.path.append("src/")

import label_utils

path = "dataset/incidenti/incidenti_2011.txt"

data : pd.DataFrame = pd.read_csv(path, sep="\t")

natura_incidente = data['natura_incidente']

natura_incidente_labels = label_utils.join_labels(
    natura_incidente, 
    "dataset/incidenti/Classificazioni/natura_incidente.csv"
    ).value_counts().sort_index()

# GRAFO 3
natura_incidente_labels.plot.barh(color='#ba754e', width=0.9)
plt.xlabel("Incidenti all'anno (2011)")
plt.tight_layout()
plt.show()