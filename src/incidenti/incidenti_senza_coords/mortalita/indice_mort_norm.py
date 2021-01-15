
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

data = pd.read_csv("dataset/incidenti/istat/incidenti_2018.txt", sep='\t')

incidenti_per_eta = data['veicolo__a___et__conducente'].value_counts().sort_index()
# Pulizia del dataset dai valori inutili
incidenti_per_eta = incidenti_per_eta.drop('n.i. ')
incidenti_per_eta = incidenti_per_eta.drop('     ')
incidenti_per_eta = incidenti_per_eta.drop('10-14')
incidenti_per_eta = incidenti_per_eta.drop('6-9  ')
incidenti_per_eta = incidenti_per_eta.drop('0-5  ')

morti_per_eta = {}
for c in data['veicolo__a___et__conducente'].unique(): 
    morti_per_eta[c] = 0

for row in data.iterrows(): 
    morti_per_eta[row[1]['veicolo__a___et__conducente']] += row[1]['morti_entro_24_ore'] + row[1]['morti_entro_30_giorni']

morti_per_eta = pd.Series(morti_per_eta).sort_index()
# Pulizia del dataset dai valori inutili
morti_per_eta = morti_per_eta.drop('n.i. ')
morti_per_eta = morti_per_eta.drop('     ')
morti_per_eta = morti_per_eta.drop('10-14')
morti_per_eta = morti_per_eta.drop('6-9  ')
morti_per_eta = morti_per_eta.drop('0-5  ')

# Coversione in percentuale
perc_fascia = np.array( [3.1, 2.8+4+5.3, 19, 18.2, 7.3+6.4, 19.3]) / 100

# Normalizzazione delle percentuali di popolazione
incidenti_per_eta /= perc_fascia
morti_per_eta /= perc_fascia
indice_mortalita = morti_per_eta * 100 / incidenti_per_eta

plt.subplot(1,2,1)
indice_mortalita.plot.bar(width=0.9, color='#69aaa3')
plt.ylabel("Indice di mortalità per\nfascia di età del conducente")
plt.tight_layout()

plt.subplot(1,2,2)
morti_per_eta = morti_per_eta / morti_per_eta.sum()
incidenti_per_eta = incidenti_per_eta / incidenti_per_eta.sum()
morti_per_eta.plot(color='#a369aa', label='Morti')
incidenti_per_eta.plot(color='#aaa469', label='Incidenti totali')
plt.xticks(rotation=90)
plt.legend()
plt.ylabel("Percentuale di incidenti e\nmorti per fascia di età")
plt.tight_layout()

plt.show()