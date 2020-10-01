
import pandas as pd

path = "dataset/incidenti/incidenti_2010.txt"
label_path = "dataset/incidenti/Classificazioni/provincia.txt"

dati = pd.read_csv(path, sep='\t')
labels = pd.read_csv(label_path)
#print(labels['id'].value_counts().unique())
#print(dati)
#print(labels)

prov = dati['provincia'].value_counts()
#print(prov.index)

def join(values: pd.Series, labels :  pd.Series) -> pd.Series: 
    return values.index.map(lambda x: get_value(x, labels))

def get_value(ID, labels : pd.Series) -> str: 
    return labels[labels['id'] == ID]['value']

joined = join(prov, labels)
print(joined)