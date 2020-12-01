
from matplotlib.pyplot import colorbar
import pandas as pd
import matplotlib.pyplot as plt
import sys
sys.path.append("src")
import label_utils
import heatmap as H

path = "dataset/incidenti/incidenti_"

tipo_incidenti = ['Frontale-laterale', 'Tamponamento', 'Investimento pedoni', 'Scontro laterale']

inc_per_anno = pd.DataFrame()
for year in range(2010, 2019): 
    if year == 2017: 
        data = pd.read_csv(path + str(year) + ".txt", sep="\t",  error_bad_lines=False, engine='python')
    else: 
        data = pd.read_csv(path + str(year) + ".txt", sep="\t",  encoding="latin1")

    natura_incidente = data['natura_incidente']

    natura_incidente_labels = label_utils.join_labels(
        natura_incidente, 
        "dataset/incidenti/Classificazioni/natura_incidente.csv"
    ).value_counts(normalize=True)

    natura_incidente_labels = natura_incidente_labels[tipo_incidenti]

    inc_per_anno[str(year)] = pd.Series(natura_incidente_labels)


fig, ax = plt.subplots()

im, cbar = H.heatmap(
    inc_per_anno, 
    inc_per_anno.index, 
    inc_per_anno.columns, 
    ax=ax, cmap="OrRd", cbarlabel="Categorie di incidenti più frequenti per anno")
texts = H.annotate_heatmap(im)

fig.tight_layout()

plt.show()
