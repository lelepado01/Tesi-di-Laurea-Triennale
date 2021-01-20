
import pandas as pd
import matplotlib.pyplot as plt
import sys 
sys.path.append("src/")
import label_utils

path = "dataset/incidenti/istat/incidenti_2018.txt"

data : pd.DataFrame = pd.read_csv(path, sep="\t", encoding='latin1')

intersezione = data['intersezione_o_non_interse3']
intersezione_labels = label_utils.join_labels(
    intersezione, 
    "dataset/incidenti/istat/Classificazioni/intersezione_o_non_interse3.csv"
    ).value_counts().sort_index()

# Tengo scala in decine di migliaia
intersezione_labels /= 1000
intersezione_labels = intersezione_labels.sort_index()

intersezione_labels.plot.barh(color=['#77aa66'], width=0.9)
plt.xlabel("Incidenti totali, in migliaia, per tipo di incrocio (2018)")
plt.ylabel("")
plt.tight_layout()
plt.show()