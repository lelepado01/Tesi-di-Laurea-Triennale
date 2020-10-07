
# TODO: non è un file necessario
# Ci sono prove che ho fatto per realizzare label_utils.py 

import pandas as pd
import matplotlib.pyplot as plt
import sys

sys.path.append("src/")

import label_utils

path = "dataset/incidenti/incidenti_2010.txt"
label_path = "dataset/incidenti/Classificazioni/provincia.csv"

dati = pd.read_csv(path, sep='\t')
labels = pd.read_csv(label_path, sep=',')
provincia : pd.Series = dati['provincia']
#print(provincia)
#print(labels[campi])
provincia = label_utils.join_labels(provincia, label_path).value_counts()

provincia[provincia > 500].plot.barh()
plt.show()

