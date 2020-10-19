
import pandas as pd
import matplotlib.pyplot as plt
import sys
sys.path.append('src')
import label_utils

path = "dataset/incidenti/incidenti_2011.txt"

data = pd.read_csv(path, sep="\t")

fields = ['pedone_morto_1__sesso']#,  'pedone_morto_2__sesso', 'pedone_morto_3__sesso', 'pedone_morto_4__sesso']
pedoni_morti = data[fields]
pedoni_morti = pedoni_morti[pedoni_morti != ' '].value_counts()
#pedoni_morti = label_utils.join_labels(pedoni_morti, 'dataset/incidenti/Classificazioni/pedone_ferito_1__sesso.csv').value_counts()

#print(pedoni_morti['pedone_morto_1__sesso'].unique())

pedoni_feriti = data['pedone_ferito_1__sesso']
pedoni_feriti = pedoni_feriti[pedoni_feriti != ' '].value_counts()
#pedoni_feriti = label_utils.join_labels(pedoni_morti, 'dataset/incidenti/Classificazioni/pedone_ferito_1__sesso.csv').value_counts()
#print(pedoni_feriti.value_counts())
#plt.subplot(121)
#plt.pie(pedoni_feriti)
#plt.title("Sesso Pedoni Feriti")
#plt.subplot(122)
#plt.pie(pedoni_morti)
#plt.legend(('Maschi', 'Femmine'))
#plt.tight_layout()
#plt.title("Sesso Pedoni Morti")
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

fields.remove('intersezione_o_non_interse1')
pedoni_feriti = get_people(incidenti_pedoni, fields)
incidenti_pedoni = pd.DataFrame([incidenti_pedoni['intersezione_o_non_interse1'], pedoni_feriti], ['tipo_incrocio', 'pedoni_feriti']).transpose()
incidenti_pedoni = incidenti_pedoni[incidenti_pedoni['pedoni_feriti'] != 0].value_counts()
incidenti_pedoni = incidenti_pedoni[incidenti_pedoni > 50]
#incidenti_labels = label_utils.join_labels(incidenti_pedoni['tipo_incrocio'], 'dataset/incidenti/Classificazioni/intersezione_o_non_interse3.csv')
#incidenti_pedoni = pd.DataFrame([incidenti_labels, incidenti_pedoni], ['tipo_incrocio', 'pedoni_feriti']).transpose().value_counts()
#print(incidenti_pedoni)

#legend = pd.read_csv('dataset/incidenti/Classificazioni/intersezione_o_non_interse3.csv')
#legend = legend['Descrizione']

from matplotlib.lines import Line2D

custom_lines = [Line2D([0], [0], color=(0, 0, 0, 0), lw=4),
                Line2D([0], [0], color=(0.5,0,0,0), lw=4),
                Line2D([0], [0], color=(0.5,0,0,0), lw=4),
                Line2D([0], [0], color=(1,0,0,0), lw=4)]

#fig, ax = plt.subplots()
#lines = ax.plot(data)
#ax.legend(custom_lines, ['Cold', 'Medium', 'Hot'])

incidenti_pedoni.plot.bar()
plt.tight_layout()
plt.xticks(rotation=0)
plt.xlabel("(Tipo Incrocio, Numero di pedoni)")
plt.legend(custom_lines, ['Incrocio - 7', 'Rotatoria - 2', 'Intersez. segnalata - 3',  'Incrocio - 1'])
plt.show()

# Età dei pedoni feriti?

#pedoni_morti = data['pedone_morto_1__et_']
#pedoni_morti = pedoni_morti[pedoni_morti != '  '].astype(int)
#pedoni_morti = label_utils.join_labels(pedoni_morti, 'dataset/incidenti/Classificazioni/veicolo__a___et__conducente.csv')
#pedoni_morti = pedoni_morti.value_counts().sort_index()
#
#pedoni_feriti = data['pedone_ferito_1__et_']
#pedoni_feriti = pedoni_feriti[pedoni_feriti != '  '].astype(int)
#pedoni_feriti = label_utils.join_labels(pedoni_feriti, 'dataset/incidenti/Classificazioni/veicolo__a___et__conducente.csv')
#pedoni_feriti = pedoni_feriti.value_counts().sort_index()

#plt.subplot(121)
#plt.tight_layout()
#plt.plot(pedoni_feriti)
#plt.xticks(rotation=90)
#plt.title("Età Pedoni Feriti")
#plt.subplot(122)
#plt.tight_layout()
#plt.xticks(rotation=90)
#plt.plot(pedoni_morti)
#plt.title("Età Pedoni Morti")
#plt.show()

