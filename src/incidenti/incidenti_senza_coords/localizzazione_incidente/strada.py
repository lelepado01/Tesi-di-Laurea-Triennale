
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

natura_incidente = data['natura_incidente'].value_counts().sort_index()
#print(natura_incidente.unique())

natura_incidente.plot.bar()
plt.show()

# Scontri frontali / laterali sono molto frequenti, 
# TODO: c'è correlazione con segnaletica / incroci? 