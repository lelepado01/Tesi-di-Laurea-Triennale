
import pandas as pd
import matplotlib.pyplot as plt
import sys 
sys.path.append("src/")

import label_utils

path = "dataset/incidenti/incidenti_2011.txt"

data : pd.DataFrame = pd.read_csv(path, sep="\t")

#print(data['tipo_di_strada'].unique())
#print(len(data[data['provincia'] == 15]))

tipo_strada = data['tipo_di_strada']
tipo_strada_labels = label_utils.join_labels(
    tipo_strada, 
    "dataset/incidenti/Classificazioni/tipo_di_strada.csv"
).value_counts()

# GRAFO 1
#tipo_strada_labels.plot.barh()
#plt.show() 

# Numero maggiore di incidenti in strade a una carreggiata

pavimentazione = data['pavimentazione']
#print(pavimentazione.unique())

#pavimentazione.value_counts().sort_index().plot.bar()
#plt.show()

# Per volume le strade pavimentate hanno più incidenti...
# Per caso influisce fatto che alcune strade hanno pavimentazione a blocchi (PAVE')?

# TODO: trovare / creare mappa con pave a milano e confrontare con mappa incidenti

segnaletica = data['segnaletica']
#print(segnaletica.unique())

#segnaletica.value_counts().sort_index().plot.bar()
#plt.show()

# Anche qui immagino il numero maggiore di incidenti sia dovuto al volume maggiore di incroci con 
# segnaletica sia orizzontale che verticale

tronco = data['tronco_di_strada_o_autostrada'].replace('  ', 0).astype(int).value_counts().sort_index()
tronco = tronco[tronco > 200]
#print(tronco.unique())

#tronco.plot.bar()
#plt.show()

# Il caso più frequente è 12 -> 'Altri casi', che non fornisce molte informazioni...

denominazione = data['denominazione_della_strada'].value_counts().sort_values(ascending=False)
#print(denominazione.value_counts())

LOWER_BOUND = 200
UPPER_BOUND = 9000
# GRAFO 2
#denominazione[(denominazione > LOWER_BOUND) & (denominazione < UPPER_BOUND)].plot.bar()
#plt.show()

# TODO: quali sono le strade denominate con indici numerici?
# Ci sono alcune autostrade nella lista, come la A4 e la A14 e la A1

natura_incidente = data['natura_incidente']

natura_incidente_labels = label_utils.join_labels(
    natura_incidente, 
    "dataset/incidenti/Classificazioni/natura_incidente.csv"
    ).value_counts().sort_index()

# GRAFO 3
#natura_incidente_labels.plot.barh()
#plt.show()

# Scontri frontali / laterali sono molto frequenti

intersezione = data['intersezione_o_non_interse1']
intersezione_labels = label_utils.join_labels(
    intersezione, 
    "dataset/incidenti/Classificazioni/intersezione_o_non_interse3.csv"
    ).value_counts().sort_index()

# GRAFO 4
#intersezione_labels.plot.barh()
#plt.show()

# Quali tipi di incroci producono quali tipi di incidenti?
natura_incidente_e_incrocio = data[['natura_incidente', 'intersezione_o_non_interse1']].value_counts()
# GRAFO 5
#natura_incidente_e_incrocio[natura_incidente_e_incrocio > 1500].plot.bar()
#plt.show()

# Di coppie molto frequenti si hanno <2, 1> e <4, 7>
# Che corrispondono rispettivamente a: 
#   scontro frontale-laterale -> incrocio
#   tamponamento -> rettilineo
# A seguire ci sono altre combinazioni con scontro frontale-laterale (rettilineo e intersezione segnalato)

# Una rotatoria dovrebbe ridurre il numero di incidenti (almeno rispetto a un incrocio),
# che tipo di incidenti avvengono?
# Ipotizzo frontale-laterale, tamponamento

incidenti_in_rotatoria = data[data['intersezione_o_non_interse1'] == 2]['natura_incidente']

incidenti_in_rotatoria_labels = label_utils.join_labels(
    incidenti_in_rotatoria, 
    "dataset/incidenti/Classificazioni/natura_incidente.csv"
).value_counts()

#incidenti_in_rotatoria_labels.sort_values().plot.barh()
#plt.show()

# I dato confermano che gli incidenti più frequenti sono frontale-laterale, laterale, tamponamento
# e fuoriuscita 
# Ho un numero alto di investimento di pedoni, succede anche negli incroci?

investimento_pedoni = data[data['natura_incidente'] == 5]['intersezione_o_non_interse1']
investimento_pedoni_labels = label_utils.join_labels(
    investimento_pedoni, 
    "dataset/incidenti/Classificazioni/intersezione_o_non_interse3.csv"
).value_counts().sort_values()

# GRAFO 6
#investimento_pedoni_labels.plot.barh()
#plt.show()

# La maggior parte degli incidenti con pedoni avvengono in rettilineo, 
# Noto che complessivamente le rotatorie riducono molto il numero di incidenti

#intersezione.value_counts().plot.bar()
#plt.show()

# Ha numero simile a un incrocio con semaforo, ma la rotatoria rende il traffico più fluido
#print(investimento_pedoni_labels)
# La rotatoria ha anche la metà di incidenti con pedoni

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

campi = ['intersezione_o_non_interse1', 'pedone_morto_1__sesso', 'pedone_morto_2__sesso', 'pedone_morto_3__sesso', 'pedone_morto_4__sesso']
pedoni = data[data['natura_incidente'] == 5][campi]
campi.remove('intersezione_o_non_interse1')
num_pedoni_per_zona = pd.DataFrame([
    pedoni['intersezione_o_non_interse1'], 
    get_people(
        pedoni, 
        campi
        )], ['zona', 'numero_pedoni']
    ).transpose().dropna()
#print(num_pedoni_per_zona[num_pedoni_per_zona['numero_pedoni'] > 0.0].value_counts())

# GRAFO 7
num_pedoni_per_zona = num_pedoni_per_zona[num_pedoni_per_zona['numero_pedoni'] > 0.0].value_counts().sort_values()
num_pedoni_per_zona = num_pedoni_per_zona[num_pedoni_per_zona > 4]
#num_pedoni_per_zona.plot.barh()
#plt.show()

# Di nuovo si nota che gli incidenti più frequenti sono quelli in 
# rettilineo dove è coinvolto un solo pedone
# Avere più di un pedone coinvolto è molto raro -> 4 istanze in totale

# DUBBIO: questi sono campi con pedoni morti, ma gli indici indicano anche feriti,
# però ho altre colonne dedicate a pedoni feriti, cambia qualcosa?

campi_pedoni_feriti = ['intersezione_o_non_interse1', 'pedone_ferito_1__sesso', 'pedone_ferito_2__sesso', 'pedone_ferito_3__sesso', 'pedone_ferito_4__sesso']
pedoni = data[data['natura_incidente'] == 5][campi_pedoni_feriti]
campi_pedoni_feriti.remove('intersezione_o_non_interse1')

num_pedoni_per_zona = pd.DataFrame([
    pedoni['intersezione_o_non_interse1'], 
    get_people(
        pedoni, 
        campi_pedoni_feriti
        )], ['zona', 'numero_pedoni']
    ).transpose().dropna()

# GRAFO 8
num_pedoni_per_zona = num_pedoni_per_zona[num_pedoni_per_zona['numero_pedoni'] > 0.0].value_counts()
num_pedoni_per_zona = num_pedoni_per_zona[num_pedoni_per_zona > 100]
#num_pedoni_per_zona.sort_values().plot.barh()
#plt.show()

# Cambiano decisamente (in volume), ci sono molti più feriti che morti
# confermano comunque il trend di rettilineo, intersezione e incrocio