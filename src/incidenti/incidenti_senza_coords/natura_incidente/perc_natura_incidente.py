

import pandas as pd
import matplotlib.pyplot as plt
import sys
sys.path.append('src')
import label_utils

data = pd.read_csv("dataset/incidenti/istat/incidenti_2018.txt", sep='\t')

tipo_incidenti = data[['natura_incidente', 'feriti']]
# Selezione di alcuni campi di tipo incidente
tamponamento = tipo_incidenti[tipo_incidenti['natura_incidente'] == 4]['feriti']
frontale = tipo_incidenti[tipo_incidenti['natura_incidente'] == 1]['feriti']
ostacolo = tipo_incidenti[tipo_incidenti['natura_incidente'] == 8]['feriti']
sbandamento = tipo_incidenti[tipo_incidenti['natura_incidente'] == 10]['feriti']

tamponamento = tamponamento.value_counts()
frontale = frontale.value_counts()
ostacolo = ostacolo.value_counts()
sbandamento = sbandamento.value_counts()

df = pd.DataFrame(
    [tamponamento, frontale, ostacolo, sbandamento], 
    ['tamponamento', 'frontale', 'ostacolo', 'sbandamento']
)[[1,2,3,4]].transpose()

# Conversione di indici numerici per tipologia di incidente 
perc = tipo_incidenti['natura_incidente']
perc = label_utils.join_labels(perc, "dataset/incidenti/istat/Classificazioni/natura_incidente.csv")
perc = perc.value_counts(normalize=False)

# Normalizzazione valori in base alla percentuale del tipo di incidente
df['tamponamento'] = df['tamponamento'] / 32104 # numero di incidenti di questo tipo (da perc)
df['frontale'] = df['frontale'] / 9715
df['ostacolo'] = df['ostacolo'] / 8606
df['sbandamento'] = df['sbandamento'] / 15284

color_ls = ['#60c1c1', '#6060c1', '#c16060', '#c1c160']
df.plot.bar(width=0.9, color=color_ls)
plt.xticks(rotation=0)
plt.xlabel("Numero di feriti")
plt.ylabel("Percentuale della categoria di incidente\ncon numero di feriti indicato (2018)")
plt.show()
