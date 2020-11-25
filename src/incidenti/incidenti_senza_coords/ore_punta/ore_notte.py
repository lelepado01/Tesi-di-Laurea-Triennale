
# IMPORTANTE: dati su tutta ITALIA

import pandas as pd
import matplotlib.pyplot as plt    

path = "dataset/incidenti/incidenti_2016.txt"

bar_width = 0.9

data = pd.read_csv(path, sep="\t", encoding='latin1')
data = data[data['Ora'] != 25]

notte = data[(data['Ora'] < 7) | (data['Ora'] > 22)]
ora_notte_week = notte[notte['giorno'] < 6]['Ora'].value_counts().sort_index()
ora_notte_weekend = notte[notte['giorno'] > 5]['Ora'].value_counts().sort_index()

ora_notte_week = ora_notte_week.reindex([23,24,1,2,3,4,5,6])
ora_notte_weekend = ora_notte_weekend.reindex([23,24,1,2,3,4,5,6])

ora_notte_week /= 5 * 52 
ora_notte_weekend /= 2 * 52
print(ora_notte_week.mean())
print(ora_notte_weekend.mean())

ora_notte_week = ora_notte_week.rename(index={24:0})
ora_notte_weekend = ora_notte_weekend.rename(index={24:0})



pd.DataFrame(
    [ora_notte_week, ora_notte_weekend], 
    ['Week', 'Weekend']
).transpose().plot.bar(color=['#d1d162', '#6262d1'], width=bar_width)

# ora_notte_weekend.plot.bar(color='#', width=bar_width)
# ora_notte_week.plot.bar(color='#', width=bar_width)

plt.ylabel("Incidenti per giorno (2016)")
plt.legend(['week', 'weekend'])
plt.xticks(rotation=0)

plt.show()

# Prendendo solo gli incidenti in milano, il grafo coincide
# Non cambia molto in altre località... ma la quantità di dati non è molta