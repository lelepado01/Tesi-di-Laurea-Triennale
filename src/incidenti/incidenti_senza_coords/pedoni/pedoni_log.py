
import pandas as pd
import matplotlib.pyplot as plt
import sys
sys.path.append('src')
import label_utils
import istat_utils

path = "dataset/incidenti/istat/incidenti_2018.txt"
fields = ['intersezione_o_non_interse3', 'pedone_ferito_1__sesso', 'pedone_ferito_2__sesso', 'pedone_ferito_3__sesso', 'pedone_ferito_4__sesso']

data = pd.read_csv(path, sep="\t")

incidenti_pedoni = data[fields]
fields.remove('intersezione_o_non_interse3')
# Pulizia di campi nulli
incidenti_pedoni = incidenti_pedoni[incidenti_pedoni['pedone_ferito_1__sesso'] != ' ']

# Conteggio incidenti per tipo di strada
pedoni_feriti = istat_utils.get_people(incidenti_pedoni, fields)
incidenti_pedoni = pd.DataFrame([incidenti_pedoni['intersezione_o_non_interse3'], pedoni_feriti], ['tipo_incrocio', 'pedoni_feriti']).transpose()
incidenti_pedoni = incidenti_pedoni[incidenti_pedoni['pedoni_feriti'] != 0]

# Conversione di indici numerici per tipo di strada in testo
incidenti_labels = label_utils.join_labels(incidenti_pedoni['tipo_incrocio'], 'dataset/incidenti/istat/Classificazioni/intersezione_o_non_interse3.csv')
incidenti_pedoni = pd.DataFrame([incidenti_labels, incidenti_pedoni['pedoni_feriti']], ['tipo_incrocio', 'pedoni_feriti']).transpose()

tab = pd.DataFrame(pd.crosstab(incidenti_pedoni['tipo_incrocio'], incidenti_pedoni['pedoni_feriti']))
media = tab[1].mean()

tab = tab.transpose()
tab.index = tab.index.astype(int)

# Eliminazione delle tipologie con minor numero di incidenti
pedone_log = tab[tab.index == 1].transpose()
pedone_log = pd.Series(pedone_log[1], index=pedone_log.index)
pedone_log = pedone_log[pedone_log > 150]

pedone_log.plot.barh(width=0.8, color='#cead65')
plt.plot([media, media], [-1,10], color='#ce7865')
plt.text(media, 7.8, "Media (tutti gli incroci)")
plt.ylabel("")
plt.xscale('log')
plt.xticks([100,1000,10000])
plt.xlabel("Numero di incidenti su scala logaritmica per anno (2018)")
plt.tight_layout()
plt.show()
