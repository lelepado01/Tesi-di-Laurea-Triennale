
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