
import pandas as pd
import matplotlib.pyplot as plt
import sys
sys.path.append("src/")
import label_utils

path = "dataset/incidenti/istat/incidenti_2018.txt"

data = pd.read_csv(path, sep="\t")

strade_urbane = data[(data['localizzazione_incidente'] == 1) | (data['localizzazione_incidente'] == 2) | (data['localizzazione_incidente'] == 3)]['veicolo__a___sesso_conducente']
strade_extraurbane = data[(data['localizzazione_incidente'] == 4) | (data['localizzazione_incidente'] == 5) | (data['localizzazione_incidente'] == 6)]['veicolo__a___sesso_conducente']
autostrade = data[data['localizzazione_incidente'] == 7]['veicolo__a___sesso_conducente']

strade_urbane = strade_urbane[strade_urbane != ' '].astype(int)
strade_extraurbane = strade_extraurbane[strade_extraurbane != ' '].astype(int)
autostrade = autostrade[autostrade != ' '].astype(int)

strade_extraurbane = label_utils.join_labels(strade_extraurbane, "dataset/incidenti/istat/Classificazioni/veicolo__a___sesso_conducente.csv").value_counts(normalize=True).sort_index()
strade_urbane = label_utils.join_labels(strade_urbane, "dataset/incidenti/istat/Classificazioni/veicolo__a___sesso_conducente.csv").value_counts(normalize=True).sort_index()
autostrade = label_utils.join_labels(autostrade, "dataset/incidenti/istat/Classificazioni/veicolo__a___sesso_conducente.csv").value_counts(normalize=True).sort_index()

pd.DataFrame(
   [strade_extraurbane, strade_urbane, autostrade], 
   index=['Autostrade', 'Strade urbane', 'Strade Extra-Urbane']
   ).transpose().plot.bar(color = ['#5f64c6', '#c65f64', '#c6c15f'])
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()