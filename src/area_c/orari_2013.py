
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

path = "dataset/area_c/orari_2013.csv"

data = pd.read_csv(path, sep=';')

print(data['hour'].value_counts())

ora = pd.Series()
for f in data['hour'].unique():
    ora = ora.append(
        pd.Series(data[data['hour'] == f]['totale'].sum()), 
        ignore_index=True
        )

ora = ora / ora.sum()

# print(ora)

# ora.plot()
# plt.show()

path = "dataset/incidenti/incidenti_2010.txt"

data = pd.read_csv(path, sep="\t")
data = data[data['ora'] != 25]

ora_week = data[data['giorno_settimana'] < 6]
ora_weekend = data[data['giorno_settimana'] > 5]
ora_week = ora_week[ora_week['ora'] != 25]
ora_weekend = ora_weekend[ora_weekend['ora'] != 25]

ora_week = ora_week[ora_week['provincia'] == 15]['ora'].value_counts().sort_index()
ora_weekend = ora_weekend[ora_weekend['provincia'] == 15]['ora'].value_counts().sort_index()

ora_week_norm = ora_week * (1 - ora)
ora_week_norm.plot()
plt.show()

# Non cambia molto, prova a normalizzarlo con percentuale di 
# incremento rispetto alla media