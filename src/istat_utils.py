
import pandas as pd

# La funzione restituisce la somma dei mesi 
# (per i dataset che hanno ancora la divisione per mese) in trimestri
def get_trimestre(data : pd.Series) -> pd.Series: 
    res = {
        1 : data.transpose()[0:3].sum(), 
        2 : data.transpose()[3:6].sum(), 
        3 : data.transpose()[6:9].sum(), 
        4 : data.transpose()[9:13].sum()
        }

    return pd.Series(res.values(), res.keys())


# La funzione conta il numero di campi non nulli passati in una colonna e
# restituisce il numero 
def count_people(row, campi, in_vehicles = False) -> int: 
    count = 0
    for field in campi: 
        if in_vehicles: 
            if row[field] != '     ' and row[field] != ' ':
                count += 1
        else: 
            if row[field] != ' ' and row[field] != '': 
                count += 1

    return count

# La funzione restituisce in una pd.Series il numero di campi non nulli in un dataset,
# contando le colonne selezionate 
# Se si vogliono contare i passeggeri nei veicoli, in_vehicle deve essere True
def get_people(dataset : pd.DataFrame, campi, in_vehicles=False): 
    if 'veicolo__a___sesso_conducente' in dataset.columns:
        dataset = dataset[dataset['veicolo__a___sesso_conducente'] != ' ']
    res = {}
    for index in range(0, len(dataset)): 
        res[index] = 0

    for index, row in dataset.iterrows(): 
        res[index] = count_people(row, campi, in_vehicles=in_vehicles)

    return pd.Series(res)

