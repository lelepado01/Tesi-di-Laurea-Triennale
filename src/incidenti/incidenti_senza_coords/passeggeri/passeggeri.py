
import pandas as pd
import matplotlib.pyplot as plt
import sys
sys.path.append("src/")

data = pd.read_csv("dataset/incidenti/incidenti_2018.txt", sep="\t")


def count_people(row) -> int: 
    campi = ['veicolo__a___et__passegger36', 'veicolo__a___et__passegger39', 'veicolo__a___et__passegger42', 'veicolo__a___et__passegger45']

    count = 0
    for field in campi: 
        if row[field] != '     ' and row[field] != ' ':  
            count += 1

    return count


def get_people_in_vehicles(dataset : pd.DataFrame): 
    dataset = dataset[dataset['veicolo__a___sesso_conducente'] != ' ']
    res = {}
    for index in range(0, len(dataset)): 
        res[index] = 0

    for index, row in dataset.iterrows(): 
        res[index] = count_people(row)

    return pd.Series(res)


passenger_count_milano = get_people_in_vehicles(data[data['provincia'] == 15])
passenger_count_milano = passenger_count_milano[passenger_count_milano < 4]
passenger_count_milano = passenger_count_milano.value_counts(normalize=True).sort_index()

estate = data[data['trimestre'] == 2]
passenger_count_rimini = get_people_in_vehicles(estate[estate['provincia'] == 99])
passenger_count_rimini = passenger_count_rimini[passenger_count_rimini < 4]
passenger_count_rimini = passenger_count_rimini.value_counts(normalize=True).sort_index()

passenger_count_bari = get_people_in_vehicles(data[data['provincia'] == 72])
passenger_count_bari = passenger_count_bari[passenger_count_bari < 4]
passenger_count_bari = passenger_count_bari.value_counts(normalize=True).sort_index()

color_ls = ['#ffcc99','#66b3ff','#ff9999']

pd.DataFrame(
    [passenger_count_milano, passenger_count_rimini, passenger_count_bari],
    ['Milano', 'Rimini', 'Bari']
).transpose().plot.bar(width=0.95, color=color_ls)
plt.xticks(rotation=0)
plt.savefig("passeggeri_bar")
plt.show()
