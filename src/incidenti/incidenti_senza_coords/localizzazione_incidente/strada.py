
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

pavimentazione.value_counts().sort_index().plot.bar()
plt.show()

# Per volume le strade pavimentate hanno più incidenti...
# Per caso influisce fatto che alcune strade hanno pavimentazione a blocchi (PAVE')?