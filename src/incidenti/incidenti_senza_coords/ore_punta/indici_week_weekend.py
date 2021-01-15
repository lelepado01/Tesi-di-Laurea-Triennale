
import pandas as pd

path = "dataset/incidenti/istat/incidenti_2018.txt"
data = pd.read_csv(path, sep="\t")

orario_selezionato = 9

# Selezione di orari della notte
data = data[data['Ora'] != 25]
ora_weekend = data[data['giorno'] > 5]['Ora'].value_counts().sort_index()
ora_week = data[data['giorno'] < 6]['Ora'].value_counts().sort_index()

# Normalizzazione dati per giorni della settimana /weekend
ora_week /= 5 * 52
ora_weekend /= 2 * 52

print((ora_week[orario_selezionato] / ora_week.mean()) * 100 -100)
print((ora_weekend[orario_selezionato] / ora_weekend.mean()) * 100 -100)

# L'indice 6 indica il settimo giorno della settimana (Domenica)
domenica = data[data['giorno'] == 6]['Ora'].value_counts().sort_index()

print((domenica[18] / domenica.mean()) * 100 -100)