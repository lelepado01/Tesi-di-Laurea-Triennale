
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

#eta.value_counts().sort_index().plot()
#plt.show()
# la fascia 30-44 anni è quella con più incidenti, successivamente scende, per avere un altro picco
# ai 65+ 

#sesso.value_counts(normalize=True).plot.pie()
#plt.show()
# Il numero di conducenti maschi è quasi 75%
# Potrebbe essere dovuto al maggiore volume di guidatori maschi

# Il numero di passeggeri influenza gli incidenti?
def count_people(row) -> int: 
    campi = ['veicolo__a___sesso_conducente', 'veicolo__a___et__passegger12', 'veicolo__a___et__passegger15', 'veicolo__a___et__passegger18', 'veicolo__a___et__passegger21']

    count = 0
    for field in campi: 
        if row[field] != '  ':  
            count += 1

    return count

def get_people_in_vehicles(dataset : pd.DataFrame): 
    res = {}
    for index in range(0, len(dataset)): 
        res[index] = 0

    for index, row in dataset.iterrows(): 
        res[index] = count_people(row)

    return pd.Series(res)

passenger_count = get_people_in_vehicles(data)

passenger_count.value_counts().sort_index().plot.bar()
plt.show()

# Il risultato che mi sarei aspettato è una campana tra 1 e 2 per volume, ma sono molto più frequenti 
# incidenti con solo il conducente a bordo
# Il fatto di avere altre persone a bordo rende il conducente più attento?

