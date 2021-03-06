
import pandas as pd
import matplotlib.pyplot as plt    

# Si utilizza il dataset del 2016 perchè l'istogramma è associato al traffico
# stimato tramite accessi in area C (Disponibili al massimo per il 2016)  
path = "dataset/incidenti/istat/incidenti_2016.txt"
data = pd.read_csv(path, sep="\t", encoding='latin1')

# Selezione di orari della notte in settimana e weekend
data = data[data['Ora'] != 25]
notte = data[(data['Ora'] < 7) | (data['Ora'] > 22)]
ora_notte_week = notte[notte['giorno'] < 6]['Ora'].value_counts().sort_index()
ora_notte_weekend = notte[notte['giorno'] > 5]['Ora'].value_counts().sort_index()

# Correzione dell'ordine, altrimenti sarebbe 1,2,3,4,5,6,23,24
ora_notte_week = ora_notte_week.reindex([23,24,1,2,3,4,5,6])
ora_notte_weekend = ora_notte_weekend.reindex([23,24,1,2,3,4,5,6])

# Normalizzazione per giorni nella settimana/weekend
ora_notte_week /= 5 * 52 
ora_notte_weekend /= 2 * 52

# Conversione dell'orario 24:00 in 0:00, più comune
ora_notte_week = ora_notte_week.rename(index={24:0})
ora_notte_weekend = ora_notte_weekend.rename(index={24:0})

pd.DataFrame(
    [ora_notte_week, ora_notte_weekend], 
    ['week', 'weekend']
).transpose().plot.bar(color=['#d1d162', '#6262d1'], width=0.9)

plt.ylabel("Incidenti per giorno (2016)")
plt.legend(['Incidenti in settimana', 'Incidenti nel weekend'])
plt.xticks(rotation=0)
plt.show()