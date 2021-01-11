
import geopandas as gp
import pandas as pd
import matplotlib.pyplot as plt
import sys
sys.path.append("src")
import aci_utils

# L'ordine utilizzato raggruppa le regioni del nord, centro e sud
order = [
    'Piemonte', 'Valle d\'Aosta', 'Liguria', 'Lombardia', 
    'Trentino-Alto Adige', 'Veneto', 'Friuli-Venezia Giulia', 'Emilia Romagna', 
    'Toscana', 'Umbria', 'Marche', 'Lazio', 
    'Abruzzo', 'Molise', 'Campania', 'Puglia', 'Basilicata', 'Calabria', 
    'Sicilia', 'Sardegna'
]

path = "dataset/regioni/regioni.geojson"
regioni = gp.read_file(path)

data = pd.read_csv('dataset/incidenti/aci/autostrade/mesi_2018.csv') 
data = data[data['TOTALE'] != '0,0'].astype({'TOTALE': int})
incidenti : pd.Series = aci_utils.get_sum_of_fields(data, 'REGIONE', 'TOTALE')

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