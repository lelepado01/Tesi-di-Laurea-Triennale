
# IMPORTANTE: dati su tutta ITALIA

import pandas as pd
import matplotlib.pyplot as plt    

path = "dataset/incidenti/incidenti_2010.txt"

bar_width = 0.96

data = pd.read_csv(path, sep="\t")
data = data[data['ora'] != 25]

notte = data[(data['ora'] < 7) | (data['ora'] > 22)]
ora_notte_week = notte[notte['giorno_settimana'] < 6]['ora'].value_counts().sort_index()
ora_notte_weekend = notte[notte['giorno_settimana'] > 5]['ora'].value_counts().sort_index()

ora_notte_week = ora_notte_week.reindex([23,24,1,2,3,4,5,6])
ora_notte_weekend = ora_notte_weekend.reindex([23,24,1,2,3,4,5,6])

ora_notte_week /= 5 * 52 
ora_notte_weekend /= 2 * 52

pd.DataFrame(
    [ora_notte_week, ora_notte_weekend], 
    ['Week', 'Weekend']
).transpose().plot.bar(color=['#d1d162', '#6262d1'], width=bar_width)

# ora_notte_weekend.plot.bar(color='#', width=bar_width)
# ora_notte_week.plot.bar(color='#', width=bar_width)

plt.xlabel("Principali ore della notte")
plt.ylabel("Incidenti per giorno")
plt.legend(['week', 'weekend'])

plt.show()

# Prendendo solo gli incidenti in milano, il grafo coincide
# Non cambia molto in altre località... ma la quantità di dati non è molta