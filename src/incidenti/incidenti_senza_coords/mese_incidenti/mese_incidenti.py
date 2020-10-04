
import pandas as pd
import matplotlib.pyplot as plt

path = "dataset/incidenti/incidenti_2010.txt"
data = pd.read_csv(path, sep="\t")

print(data['mese'].unique())

# GRAFO 1
mese = data['mese']
#print(mese.mean())
#mese.value_counts().sort_index().plot.bar()
#plt.show()

# Noto subito che agosto, gennaio e febbraio hanno valori molto minori rispetto alla media
# Per febbraio, quanto influisce il fatto che ha 3 giorni in meno? -> 28 giorni

# Calcolo numero di incidenti al giorno
incidenti_al_giorno_per_mese = mese.value_counts().sort_index()
giorni_al_mese = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

for index in range(0, len(incidenti_al_giorno_per_mese)): 
    incidenti_al_giorno_per_mese.iloc[index] /= giorni_al_mese[index]

# GRAFO 2 
incidenti_al_giorno_per_mese.plot.bar()
plt.show()