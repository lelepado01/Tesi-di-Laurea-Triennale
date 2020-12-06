
import pandas as pd
import matplotlib.pyplot as plt
import sys
sys.path.append("src/")
import label_utils
import heatmap as H

data = pd.read_csv("dataset/incidenti/incidenti_2018.txt", sep="\t")

autostrade_veicoli = data[data['localizzazione_incidente'] == 7]['tipo_veicolo_a']
autostrade_veicoli = label_utils.join_labels(autostrade_veicoli, "dataset/incidenti/Classificazioni/tipo_veicoli__b_.csv").value_counts(normalize=True).sort_index()

strade_urbane = data[(data['localizzazione_incidente'] == 1) | (data['localizzazione_incidente'] == 2) | (data['localizzazione_incidente'] == 3)]['tipo_veicolo_a']
strade_urbane = label_utils.join_labels(strade_urbane, "dataset/incidenti/Classificazioni/tipo_veicoli__b_.csv").value_counts(normalize=True).sort_index()

strade_extraurbane = data[(data['localizzazione_incidente'] == 4) | (data['localizzazione_incidente'] == 5) | (data['localizzazione_incidente'] == 6)]['tipo_veicolo_a']
strade_extraurbane = label_utils.join_labels(strade_extraurbane, "dataset/incidenti/Classificazioni/tipo_veicoli__b_.csv").value_counts(normalize=True).sort_index()

uniti = pd.DataFrame([
   autostrade_veicoli, strade_urbane, strade_extraurbane
], index=['Autostrade', 'Strade urbane', 'Strade Extra-Urbane']).transpose().dropna().transpose()

uniti[uniti < 0.02] = 0.0
uniti['altro'] = 1 - uniti.transpose().sum()

autoc= ['#b9c466']*15 
suc = ['#b9c466']*15 
seuc = ['#b9c466']*15
autoc[0] =  '#83c466'
suc[0] =    '#83c466'
seuc[0] =   '#83c466'
autoc[4] =  '#66c4a6'
suc[4] =    '#66c4a6'
seuc[4] =   '#66c4a6'
autoc[9] =  '#a666c4'
suc[9] =    '#a666c4'
seuc[9] =   '#a666c4'
autoc[14] = '#c46683'
suc[14] =   '#c46683'
seuc[14] =  '#c46683'
autoc[11] = '#7166c4'

color_ls = autoc+suc+seuc

colors = ['#83c466', '#66c4a6', '#b9c466', '#a666c4', '#7166c4', '#c46683']
labels =['Auto Privata', 'Autocarro', 'Ciclomotore', 'Motociclo da solo', 'Trattore stradale', 'altro']

from matplotlib.lines import Line2D
lines = [Line2D([], [], color=c, linewidth=4) for c in colors]

uniti.plot.barh(stacked=True, color=color_ls)
plt.legend(lines, labels, bbox_to_anchor=(1,1), loc="upper left")
plt.xlabel("Percentuale della tipologia di veicolo")
plt.tight_layout()
plt.show()