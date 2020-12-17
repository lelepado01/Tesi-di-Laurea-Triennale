
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

autoc= ['#8755d1']*15 
suc = ['#8755d1']*15 
seuc = ['#8755d1']*15
autoc[0] =  '#559fd1'
suc[0] =    '#559fd1'
seuc[0] =   '#559fd1'
autoc[4] =  '#d18755'
suc[4] =    '#d18755'
seuc[4] =   '#d18755'
autoc[9] =  '#9fd155'
suc[9] =    '#9fd155'
seuc[9] =   '#9fd155'
autoc[14] = '#d1559f'
suc[14] =   '#d1559f'
seuc[14] =  '#d1559f'
autoc[11] = '#55d187'

color_ls = autoc+suc+seuc
print(uniti.transpose())
colors = ['#559fd1', '#d18755', '#8755d1', '#9fd155', '#55d187', '#d1559f']
labels =['Auto Privata', 'Autocarro', 'Ciclomotore', 'Motociclo da solo', 'Trattore stradale', 'altro']

from matplotlib.lines import Line2D
lines = [Line2D([], [], color=c, linewidth=4) for c in colors]

uniti.plot.barh(stacked=True, color=color_ls)
plt.legend(lines, labels, bbox_to_anchor=(1,1), loc="upper left")
plt.xlabel("Percentuale della tipologia di veicolo")
plt.tight_layout()
plt.show()