
import pandas as pd
import matplotlib.pyplot as plt

path = "dataset/incidenti/incidenti_2010.txt"
label_path = "dataset/incidenti/Classificazioni/provincia.csv"

dati = pd.read_csv(path, sep='\t')
labels = pd.read_csv(label_path, sep=',')
provincia : pd.Series = dati['provincia']

campi = ['Modalita\'', 'Descrizione']

#print(provincia)
#print(labels[campi])
labels = labels[campi]

def dataframe_to_dict(df : pd.DataFrame) -> dict: 
    dictionary : dict = {} 
    for row in df.values: 
        k, d = row
        dictionary[k] = d
    
    return dictionary

def join_labels(dataframe : pd.DataFrame, path_to_labels) -> pd.DataFrame: 
    labels = pd.read_csv(path_to_labels, sep=',')
    return provincia.replace(dataframe_to_dict(labels))


provincia = provincia.replace(dataframe_to_dict(labels)).value_counts()

provincia[provincia > 500].plot.barh()
plt.show()

