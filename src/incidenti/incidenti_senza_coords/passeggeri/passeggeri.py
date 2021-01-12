
import pandas as pd
import matplotlib.pyplot as plt
import sys
sys.path.append("src/")
import istat_utils

data = pd.read_csv("dataset/incidenti/istat/incidenti_2018.txt", sep="\t")
campi = ['veicolo__a___et__passegger36', 'veicolo__a___et__passegger39', 'veicolo__a___et__passegger42', 'veicolo__a___et__passegger45']

# Conteggio passeggeri in provincia di milano
passenger_count_milano = istat_utils.get_people(data[data['provincia'] == 15], campi, in_vehicles = True)
passenger_count_milano = passenger_count_milano[passenger_count_milano < 4]
passenger_count_milano = passenger_count_milano.value_counts(normalize=True).sort_index()

# Conteggio passeggeri in prov. di rimini (nel trimestre estivo)
estate = data[data['trimestre'] == 2]
passenger_count_rimini = istat_utils.get_people(estate[estate['provincia'] == 99], campi, in_vehicles = True)
passenger_count_rimini = passenger_count_rimini[passenger_count_rimini < 4]
passenger_count_rimini = passenger_count_rimini.value_counts(normalize=True).sort_index()

# Conteggio passeggeri in prov. di Bari
passenger_count_bari = istat_utils.get_people(data[data['provincia'] == 72], campi, in_vehicles = True)
passenger_count_bari = passenger_count_bari[passenger_count_bari < 4]
passenger_count_bari = passenger_count_bari.value_counts(normalize=True).sort_index()

pd.DataFrame(
    [passenger_count_milano, passenger_count_rimini, passenger_count_bari],
    ['Milano', 'Rimini', 'Bari']
).transpose().plot.bar(width=0.95, color=['#5f64c6', '#c65f64', '#c6c15f'])
plt.xticks(rotation=0)
plt.xlabel("Numero passeggeri")
plt.show()
