
import pandas as pd
import matplotlib.pyplot as plt
import sys
sys.path.append("src/")

import label_utils

data = pd.read_csv("dataset/incidenti/incidenti_2010.txt", sep="\t")
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
    campi = ['veicolo__a___sesso_conducente', 'veicolo__a___et__passegger12', 'veicolo__a___et__passegger15', 'veicolo__a___et__passegger18', 'veicolo__a___et__passegger21']

    count = 0
    for field in campi: 
        if row[field] != '  ' and row[field] != ' ':  
            count += 1

    return count

def get_people_in_vehicles(dataset : pd.DataFrame): 
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
passenger_count_milano = passenger_count_milano[passenger_count_milano != 0]
passenger_count_milano = passenger_count_milano.value_counts(normalize=True).sort_index()#.plot.bar(xlabel="Numero Passeggeri")
passenger_count_rimini = get_people_in_vehicles(data[data['provincia'] == 99])
passenger_count_rimini = passenger_count_rimini[passenger_count_rimini != 0]
passenger_count_rimini = passenger_count_rimini.value_counts(normalize=True).sort_index()#.plot.bar(xlabel="Numero Passeggeri")

plt.subplot(1,2,1)
plt.pie(passenger_count_milano, labels=passenger_count_milano.index, colors=['#ffcc99','#66b3ff','#99ff99','#ff9999'])
plt.gca().add_patch(plt.Circle((0,0), 0.7, color='white'))
plt.text(-0.2, 0, "Milano")
plt.tight_layout()

ls : list = passenger_count_rimini.index.tolist()
ls[2] = '\n3'
ls[3] = '  4'

plt.subplot(1,2,2)
plt.pie(passenger_count_rimini, labels=ls, colors=['#ffcc99','#66b3ff','#99ff99','#ff9999'])
plt.gca().add_patch(plt.Circle((0,0), 0.7, color='white'))
plt.text(-0.18,0, "Rimini")
plt.tight_layout()
plt.show()

#eta = data[data['provincia'] == 15]['veicolo__a___et__conducente']
#eta = label_utils.join_labels(eta, 'dataset/incidenti/Classificazioni/veicolo__a___et__conducente.csv').value_counts().sort_index()
#eta.plot()
#plt.show()


# fig1, ax1 = plt.subplots()
# ax1.pie(passenger_count_milano, autopct='%1.1f%%')
# #draw circle
# centre_circle = plt.Circle((0,0),0.70,fc='white')
# fig = plt.gcf()
# fig.gca().add_artist(centre_circle)
# # Equal aspect ratio ensures that pie is drawn as a circle
# ax1.axis('equal')  
# plt.tight_layout()
# plt.show()