
# IMPORTANTE: dati su tutta ITALIA

import pandas as pd
import matplotlib.pyplot as plt

path = "dataset/incidenti/incidenti_2010.txt"

data = pd.read_csv(path, sep="\t")
data = data[data['ora'] != 25]
#print(data.unique())

# Quanto influiscono le data di punta sugli incidenti?

#data['ora'].value_counts().sort_index().plot()
#plt.show()

# Ora di punta serale -> 17 - 19
ora_punta = data[(data['ora'] > 16) & (data['ora'] < 20)]
ora_punta_weekend = ora_punta[ora_punta['giorno_settimana'] > 5]['ora'].value_counts().sort_index()
ora_punta_week = ora_punta[ora_punta['giorno_settimana'] < 6]['ora'].value_counts().sort_index()

#print(ora_punta_weekend['ora'])

uniti_sera = pd.DataFrame(
    [ora_punta_week, ora_punta_weekend], 
    index=['week', 'weekend']).transpose()

#uniti.plot.bar()
#plt.xlabel("Incidenti in ore di Punta")
#plt.show()

# Aggiusto per il fatto che la settimana è 5 giorni e il weekend è 2
uniti_sera = pd.DataFrame([
    uniti_sera['week'] / 5, 
    uniti_sera['weekend'] / 2
], index=['week', 'weekend']).transpose()

# In ogni ora  c'è comunque una differenza di più di 100 incidenti tra week e weekend

# Per la mattina?

ora_punta = data[(data['ora'] > 6) & (data['ora'] < 11)]
ora_punta_weekend = ora_punta[ora_punta['giorno_settimana'] > 5]['ora'].value_counts().sort_index()
ora_punta_week = ora_punta[ora_punta['giorno_settimana'] < 6]['ora'].value_counts().sort_index()

uniti_mattina = pd.DataFrame([
    ora_punta_week / 5, 
    ora_punta_weekend / 2
], index=['week', 'weekend']).transpose()

#plt.figure(1)
#plt.bar(uniti_sera.columns, uniti_sera)
#plt.figure(2)
#plt.bar(uniti_mattina.columns, uniti_mattina)
#plt.show()

# Si nota ancora di  più la differenza tra le 8 e le 9 (probabilmente perchè la gente dorme)
# Alle 10 la situazione è già diversa

# Se guardo solo in milano?

ora_punta = data[(data['ora'] > 6) & (data['ora'] < 11)]
ore_punta_milano = ora_punta[ora_punta['provincia'] == 15]
#print(ore_punta_milano)
ora_punta_weekend = ore_punta_milano[ore_punta_milano['giorno_settimana'] > 5]['ora'].value_counts().sort_index()
ora_punta_week = ore_punta_milano[ore_punta_milano['giorno_settimana'] < 6]['ora'].value_counts().sort_index()

uniti = pd.DataFrame([
    ora_punta_week / 5, 
    ora_punta_weekend / 2
], index=['week', 'weekend']).transpose()

#uniti.plot.bar()
#plt.xlabel("Incidenti in ore di Punta in Milano")
#plt.show()

# Si nota differenza anche alle 7, anche se su taglia di campione molto piccola...

ora_week = data[data['giorno_settimana'] < 6]
ora_weekend = data[data['giorno_settimana'] > 5]#['ora'].value_counts().sort_index()

ora_week = ora_week[ora_week['provincia'] == 15]['ora'].value_counts().sort_index()
ora_weekend = ora_weekend[ora_weekend['provincia'] == 15]['ora'].value_counts().sort_index()

uniti = pd.DataFrame([
    ora_week / 5, 
    ora_weekend / 2
], index=['week', 'weekend']).transpose()

uniti.plot()
plt.show()