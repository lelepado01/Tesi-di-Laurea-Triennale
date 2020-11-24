
import pandas as pd
import matplotlib.pyplot as plt
import sys
sys.path.append("src/")

import label_utils

data = pd.read_csv("dataset/incidenti/incidenti_2018.txt", sep="\t")
#print(data)

# Il sesso o l'età del conducente influenza gli incidenti?

#eta = data['veicolo__a___et__conducente'].append(data['veicolo__b___et__conducente']).append(data['veicolo__c___et__conducente'])
#sesso = data['veicolo__a___sesso_conducente'].append(data['veicolo__b___sesso_conducente']).append(data['veicolo__c___sesso_conducente'])
#eta = eta[eta != '  ']
#sesso = sesso[sesso != ' ']
#print(eta.value_counts())
#print(sesso.value_counts())

# GRAFO 1
#eta.value_counts().sort_index().plot(xlabel="Età conducente")
#plt.show()
# la fascia 30-44 anni è quella con più incidenti, successivamente scende, per avere un altro picco
# ai 65+ 

# GRAFO 2
#sesso = label_utils.join_labels(sesso.astype(int), "dataset/incidenti/Classificazioni/veicolo__a___sesso_conducente.csv")
##print(sesso)
#sesso.value_counts(normalize=True).plot.pie()
#plt.show()
# Il numero di conducenti maschi è quasi 75%
# Potrebbe essere dovuto al maggiore volume di guidatori maschi?

# Il numero di passeggeri influenza gli incidenti?

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

# GRAFO 3
#passenger_count = get_people_in_vehicles(data)
#passenger_count.value_counts().sort_index().plot.bar(xlabel="Numero Passeggeri")
#plt.show()

# Il risultato che mi sarei aspettato è una campana tra 1 e 2 per volume, 
# ma sono molto più frequenti incidenti con solo il conducente a bordo
# Il fatto di avere altre persone a bordo rende il conducente più attento?

passenger_count_milano = get_people_in_vehicles(data[data['provincia'] == 15])
passenger_count_milano = passenger_count_milano[passenger_count_milano < 4]
passenger_count_milano = passenger_count_milano.value_counts(normalize=True).sort_index()

passenger_count_rimini = get_people_in_vehicles(data[data['provincia'] == 99])
passenger_count_rimini = passenger_count_rimini[passenger_count_rimini < 4]
passenger_count_rimini = passenger_count_rimini.value_counts(normalize=True).sort_index()

passenger_count_bari = get_people_in_vehicles(data[data['provincia'] == 72])
passenger_count_bari = passenger_count_bari[passenger_count_bari < 4]
passenger_count_bari = passenger_count_bari.value_counts(normalize=True).sort_index()

# plt.subplot(1,2,1)
# plt.pie(passenger_count_milano, labels=passenger_count_milano.index, colors=['#ffcc99','#66b3ff','#99ff99','#ff9999'], autopct='%1.1f%%', pctdistance=0.85)
# plt.gca().add_patch(plt.Circle((0,0), 0.7, color='white'))
# plt.text(-0.2, 0, "Milano")
# plt.tight_layout()

# ls : list = passenger_count_rimini.index.tolist()
# ls[2] = '\n3'
# ls[3] = '  4'

# plt.subplot(1,2,2)
# plt.pie(passenger_count_rimini, labels=ls, colors=['#ffcc99','#66b3ff','#99ff99','#ff9999'], pctdistance=0.85)
# plt.gca().add_patch(plt.Circle((0,0), 0.7, color='white'))
# plt.text(-0.18,0, "Rimini")
# plt.tight_layout()
# plt.show()

color_ls = ['#ffcc99','#66b3ff','#ff9999']

pd.DataFrame(
    [passenger_count_milano, passenger_count_rimini, passenger_count_bari],
    ['Milano', 'Rimini', 'Bari']
).transpose().plot.bar(width=0.95, color=color_ls)
plt.xticks(rotation=0)
plt.savefig("passeggeri_bar")
plt.show()
