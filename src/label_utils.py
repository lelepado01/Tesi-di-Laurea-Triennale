
import pandas as pd

def dataframe_to_dict(df : pd.DataFrame) -> dict: 
    campi = ['Modalita\'', 'Descrizione']
    dictionary : dict = {} 
    for k, d in zip(df[campi[0]], df[campi[1]]): 
        dictionary[k] = d
    
    return dictionary

def join_labels(dataframe : pd.DataFrame, path_to_labels) -> pd.DataFrame: 
    labels = pd.read_csv(path_to_labels, sep=',')
    return dataframe.replace(dataframe_to_dict(labels))
