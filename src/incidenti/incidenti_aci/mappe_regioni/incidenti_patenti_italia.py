

import geopandas as gp
import pandas as pd
import matplotlib.pyplot as plt

order = [
    'Piemonte', 'Valle d\'Aosta', 'Liguria', 'Lombardia', 
    'Trentino-Alto Adige', 'Veneto', 'Friuli-Venezia Giulia', 'Emilia Romagna', 
    'Toscana', 'Umbria', 'Marche', 'Lazio', 
    'Abruzzo', 'Molise', 'Campania', 'Puglia', 'Basilicata', 'Calabria', 
    'Sicilia', 'Sardegna'
]

def get_sum_of_fields(data : pd.DataFrame, select_field : str, field_to_sum : str) -> pd.Series: 
    res = {}
    index = 0
    for reg in data[select_field].unique():
        res[index] = [reg, 0]
        index += 1

    index = 0
    for reg in data[select_field].unique():
        for row in data[data[select_field] == reg][field_to_sum]:
            res[index] = [res[index][0], res[index][1] + row]
        index += 1

    return pd.DataFrame(res, index=[select_field, field_to_sum]).transpose()


path = "dataset/regioni/regioni.geojson"
regioni = gp.read_file(path)

data = pd.read_csv('dataset/incidenti/aci/autostrade/mesi_2018.csv') 
data = data[data['TOTALE'] != '0,0'].astype({'TOTALE': int})
incidenti : pd.Series = get_sum_of_fields(data, 'REGIONE', 'TOTALE')

patenti = pd.read_csv("dataset/patenti/patenti_mit.csv")

incidenti.index = incidenti['REGIONE']
incidenti = incidenti['TOTALE']
incidenti = incidenti.reindex(order)

regioni.index = regioni['reg_name']
regioni.reindex(order)

patenti.index = patenti['REGIONE']
patenti = patenti['NUMERO']
patenti = patenti.reindex(order)

rapp = incidenti / patenti
regioni['RAPPORTO'] = rapp

regioni.plot(column='RAPPORTO', cmap='OrRd', legend=False)
plt.axis('off')
plt.show()