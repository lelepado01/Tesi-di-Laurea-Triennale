
import pandas as pd
import matplotlib.pyplot as plt

path = "dataset/incidenti/incidenti_2011.txt"

data : pd.DataFrame = pd.read_csv(path, sep="\t")

#print(data['tipo_di_strada'].unique())

labels = pd.read_csv("dataset/incidenti/Classificazioni/tipo_di_strada.csv")['Descrizione']
#print(labels)

tipo_strada = data['tipo_di_strada'].value_counts().sort_index()
#tipo_strada.plot.bar(labels)
#plt.show() 

# Numero maggiore di incidenti in strade a una carreggiata

pavimentazione = data['pavimentazione']
#print(pavimentazione.unique())

#pavimentazione.value_counts().sort_index().plot.bar()
#plt.show()

# Per volume le strade pavimentate hanno più incidenti...
# Per caso influisce fatto che alcune strade hanno pavimentazione a blocchi (PAVE')?

segnaletica = data['segnaletica']
#print(segnaletica.unique())

#segnaletica.value_counts().sort_index().plot.bar()
#plt.show()

# Qualcosa non va perchè col.4 dovrebbe essere col.3 + col.2

labels_intersezione = pd.read_csv("dataset/incidenti/Classificazioni/intersezione_o_non_interse3.csv")
#print(labels_intersezione['Descrizione'])

intersezione = data['intersezione_o_non_interse1']
#print("Intersezione: ")
#print(intersezione.unique())

#intersezione.value_counts().sort_index().plot.bar()
#plt.show()

tronco = data['tronco_di_strada_o_autostrada'].replace('  ', 0).astype(int)
#print(tronco.unique())

#tronco.value_counts().sort_index().plot.bar()
#plt.show()

denominazione = data['denominazione_della_strada'].value_counts().sort_index()
#print(denominazione.value_counts())

LOWER_BOUND = 200
#denominazione[(denominazione > LOWER_BOUND) & (denominazione < 9000)].plot.bar()
#plt.show()

natura_incidente = data['natura_incidente']
#print(natura_incidente.unique())

import sys 
sys.path.append("src/")

import label_utils

natura_incidente_labels = label_utils.join_labels(
    natura_incidente, 
    "dataset/incidenti/Classificazioni/natura_incidente.csv"
    ).value_counts().sort_index()

#natura_incidente_labels.plot.barh()
#plt.show()

# Scontri frontali / laterali sono molto frequenti

intersezione_labels = label_utils.join_labels(
    intersezione, 
    "dataset/incidenti/Classificazioni/intersezione_o_non_interse3.csv"
    ).value_counts().sort_index()

#intersezione_labels.plot.barh()
#plt.show()

natura_incidente_e_incrocio = data[['natura_incidente', 'intersezione_o_non_interse1']].value_counts()

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

#investimento_pedoni_labels.plot.barh()
#plt.show()

# La maggior parte degli incidenti con pedoni avvengono in rettilineo, 
# Noto che complessivamente le rotatorie riducono molto il numero di incidenti

#intersezione.value_counts().plot.bar()
#plt.show()

# Ha numero simile a un incrocio con semaforo, ma la rotatoria rende il traffico più fluido
print(investimento_pedoni_labels)
# La rotatoria ha anche la metà di incidenti con pedoni