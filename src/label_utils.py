
import pandas as pd

# Converte il dataframe passato come argomento, con campi <Modalità, Descrizione>
# in un dizionario
# uso la funzione per rimpiazzare gli indici numerici di altri dataframe  
def dataframe_to_dict(df : pd.DataFrame) -> dict: 
    campi = ['Modalita\'', 'Descrizione']
    dictionary : dict = {} 
    for k, d in zip(df[campi[0]], df[campi[1]]): 
        dictionary[k] = d
    
    return dictionary

# dataframe : dati in formato numerico da rimpiazzare
# path_to_labels : path al file di labels
# La funzione restituisce un dataframe modificato
def join_labels(dataframe : pd.DataFrame, path_to_labels : str) -> pd.DataFrame: 
    labels = pd.read_csv(path_to_labels, sep=',')
    return dataframe.replace(dataframe_to_dict(labels))
