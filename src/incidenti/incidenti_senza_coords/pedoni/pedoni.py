
import pandas as pd
import matplotlib.pyplot as plt

path = "dataset/incidenti/incidenti_2011.txt"

data = pd.read_csv(path, sep="\t")

fields = ['pedone_morto_1__sesso']#,  'pedone_morto_2__sesso', 'pedone_morto_3__sesso', 'pedone_morto_4__sesso']
pedoni_morti = data[fields]
pedoni_morti = pedoni_morti[pedoni_morti != ' '].value_counts()

#print(pedoni_morti['pedone_morto_1__sesso'].unique())

pedoni_feriti = data['pedone_ferito_1__sesso']
pedoni_feriti = pedoni_feriti[pedoni_feriti != ' '].value_counts()

#plt.subplot(121)
#plt.pie(pedoni_feriti)
#plt.title("Pedoni Feriti")
#plt.subplot(122)
#plt.pie(pedoni_morti)
#plt.title("Pedoni Morti")
#plt.show()

# Mi aspetto 50%, 50%
fields = ['intersezione_o_non_interse1', 'pedone_ferito_1__sesso', 'pedone_ferito_2__sesso', 'pedone_ferito_3__sesso', 'pedone_ferito_4__sesso']
incidenti_pedoni = data[fields]
#incidenti_pedoni = incidenti_pedoni[incidenti_pedoni['pedone_ferito_1__sesso'] != ' ']

def count_people(row, campi) -> int: 
    count = 0
    for field in campi: 
        if row[field] != ' ' and row[field] != '':
            count += 1

    return count

def get_people(dataset : pd.DataFrame, campi): 
    res = {}
    for index in range(0, len(dataset)): 
        res[index] = 0

    for index, row in dataset.iterrows(): 
        res[index] = count_people(row, campi)

    return pd.Series(res)

import sys
sys.path.append('src')
import label_utils

fields.remove('intersezione_o_non_interse1')
pedoni_feriti = get_people(incidenti_pedoni, fields)
incidenti_pedoni = pd.DataFrame([incidenti_pedoni['intersezione_o_non_interse1'], pedoni_feriti], ['tipo_incrocio', 'pedoni_feriti']).transpose()
incidenti_pedoni = incidenti_pedoni[incidenti_pedoni['pedoni_feriti'] != 0].value_counts()
incidenti_pedoni = incidenti_pedoni[incidenti_pedoni > 50]
#incidenti_labels = label_utils.join_labels(incidenti_pedoni['tipo_incrocio'], 'dataset/incidenti/Classificazioni/intersezione_o_non_interse3.csv')
#incidenti_pedoni = pd.DataFrame([incidenti_labels, incidenti_pedoni], ['tipo_incrocio', 'pedoni_feriti']).transpose().value_counts()
#print(incidenti_pedoni)

legend = pd.read_csv('dataset/incidenti/Classificazioni/intersezione_o_non_interse3.csv')
legend = legend['Descrizione']

incidenti_pedoni.plot.bar()
#plt.legend((1, 2, 3, 7, 8), ('Incrocio', 'Rotatoria', 'Intersez. segnalata', 'Rettilineo', 'Curva'))
plt.show()

# Realizza Legenda esterna