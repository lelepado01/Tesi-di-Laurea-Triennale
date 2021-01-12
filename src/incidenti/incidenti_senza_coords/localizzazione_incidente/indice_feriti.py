
import pandas as pd
import sys
sys.path.append("src")
import label_utils

data = pd.read_csv("dataset/incidenti/istat/incidenti_2018.txt", sep="\t", encoding='latin1')

incr = 'intersezione_o_non_interse3'

# Somma incidenti per tipo di incrocio
df = {}
for inc in data[incr].unique(): 
    df[inc] = 0

for inc, morti in zip(data[incr], data['feriti']): 
    df[inc] += morti

num_incr = data[incr].value_counts().sort_index()

# Calcolo indice di feriti
indice_feriti = pd.Series(df.values(),index =  df.keys()).sort_index()
indice_feriti = pd.DataFrame([indice_feriti * 100 / num_incr], 
    index=['indice']
).transpose()

indice_feriti['incrocio'] = indice_feriti.index
indice_feriti['incrocio'] = label_utils.join_labels(
    indice_feriti['incrocio'], 
    "dataset/incidenti/istat/Classificazioni/intersezione_o_non_interse3.csv"
    )

print(indice_feriti)
