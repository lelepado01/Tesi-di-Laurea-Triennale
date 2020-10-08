
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("dataset/incidenti/incidenti_2010.txt", sep="\t")
#print(data)

# Il sesso o l'età del conducente influenza gli incidenti?

eta = data['veicolo__a___et__conducente'].append(data['veicolo__b___et__conducente']).append(data['veicolo__c___et__conducente'])
sesso = data['veicolo__a___sesso_conducente'].append(data['veicolo__b___sesso_conducente']).append(data['veicolo__c___sesso_conducente'])
eta = eta[eta != '  ']
sesso = sesso[sesso != ' ']
#print(eta.value_counts())
#print(sesso.value_counts())

eta.value_counts().sort_index().plot()
plt.show()
# la fascia 30-44 anni è quella con più incidenti, successivamente scende, per avere un altro picco
# ai 65+ 

#sesso.value_counts(normalize=True).plot.pie()
#plt.show()
# Il numero di conducenti maschi è quasi 75%
# Potrebbe essere dovuto al maggiore volume di guidatori maschi

# Il numero di passeggeri influenza gli incidenti?
# TODO: per ogni campo veicoli, sommo il numero di passeggeri delle diverse colonne
def get_people_in_vehicle(num: int): 
    field_list = []