

import pandas as pd
import matplotlib.pyplot as plt
import sys
sys.path.append('src')
import label_utils

data = pd.read_csv("dataset/incidenti/incidenti_2010.txt", sep='\t')

tipo_incidenti = data[['natura_incidente', 'feriti']]

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
)

df = df[[1,2,3,4]].transpose()

perc = tipo_incidenti['natura_incidente']
perc = label_utils.join_labels(perc, "dataset/incidenti/Classificazioni/natura_incidente.csv")
perc = perc.value_counts(normalize=True)

# Sbandamento                0.097109
# Tamponamento               0.143532
# Scontro frontale           0.061271
# Urto con ostacolo          0.038681

df['tamponamento'] = df['tamponamento'] / 5655
df['frontale'] = df['frontale'] / 2414
df['ostacolo'] = df['ostacolo'] / 1524
df['sbandamento'] = df['sbandamento'] / 3826

color_ls = ['#60c1c1', '#6060c1', '#c16060', '#c1c160']
df.plot.bar(width=0.9, color=color_ls)
plt.xticks(rotation=0)
plt.xlabel("Numero di feriti")
plt.ylabel("Percentuale della categoria di incidente\ncon numero di feriti indicato")
plt.show()
