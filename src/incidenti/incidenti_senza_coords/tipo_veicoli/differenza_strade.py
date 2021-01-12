
import pandas as pd
import matplotlib.pyplot as plt
import sys
sys.path.append("src/")
import label_utils

data = pd.read_csv("dataset/incidenti/istat/incidenti_2018.txt", sep="\t")

# Selezione dati per localizzazione incidente
autostrade_veicoli = data[data['localizzazione_incidente'] == 7]['tipo_veicolo_a']
autostrade_veicoli = label_utils.join_labels(autostrade_veicoli, "dataset/incidenti/istat/Classificazioni/tipo_veicoli__b_.csv").value_counts(normalize=True).sort_index()

strade_urbane = data[(data['localizzazione_incidente'] == 1) | (data['localizzazione_incidente'] == 2) | (data['localizzazione_incidente'] == 3)]['tipo_veicolo_a']
strade_urbane = label_utils.join_labels(strade_urbane, "dataset/incidenti/istat/Classificazioni/tipo_veicoli__b_.csv").value_counts(normalize=True).sort_index()

strade_extraurbane = data[(data['localizzazione_incidente'] == 4) | (data['localizzazione_incidente'] == 5) | (data['localizzazione_incidente'] == 6)]['tipo_veicolo_a']
strade_extraurbane = label_utils.join_labels(strade_extraurbane, "dataset/incidenti/istat/Classificazioni/tipo_veicoli__b_.csv").value_counts(normalize=True).sort_index()

uniti = pd.DataFrame([
   autostrade_veicoli, strade_urbane, strade_extraurbane
], index=['Autostrade', 'Strade urbane', 'Strade Extra-Urbane']).transpose().dropna().transpose()

# eliminazione di vari campi troppo piccoli per essere mostrati
uniti[uniti < 0.02] = 0.0
# Raggruppamento dei campi rimossi in 'altro'
uniti['altro'] = 1 - uniti.transpose().sum()

# Colorazione del grafico in modo che sia consistente
c1 = '#d8cb88'
c2 = '#8895d8'
c3 = '#cb88d8'
c4 = '#95d888'
c5 = '#d88895'
c6 = '#88d8cb'

autoc= [c1]*15 
suc = [c1]*15 
seuc = [c1]*15
autoc[0] =  c2
suc[0] =    c2
seuc[0] =   c2
autoc[4] =  c3
suc[4] =    c3
seuc[4] =   c3
autoc[9] =  c4
suc[9] =    c4
seuc[9] =   c4
autoc[14] = c5
suc[14] =   c5
seuc[14] =  c5
autoc[11] = c6

color_ls = autoc+suc+seuc
colors = [c2, c3, c1, c4, c6, c5]
labels =['Auto Privata', 'Autocarro', 'Ciclomotore', 'Motociclo da solo', 'Trattore stradale', 'altro']

from matplotlib.lines import Line2D
lines = [Line2D([], [], color=c, linewidth=4) for c in colors]

uniti.plot.barh(stacked=True, color=color_ls)
plt.legend(lines, labels, bbox_to_anchor=(1,1), loc="upper left")
plt.xlabel("Percentuale della tipologia di veicolo")
plt.tight_layout()
plt.show()