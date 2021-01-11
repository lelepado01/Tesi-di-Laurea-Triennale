

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

patenti = pd.read_csv("dataset/patenti/patenti_mit.csv")
incidenti = pd.read_csv("dataset/incidenti/aci/autostrade/mesi_2018.csv")

incidenti = aci_utils.get_sum_of_fields(incidenti, 'REGIONE', 'TOTALE')

incidenti.index = incidenti['REGIONE']
patenti.index = patenti['REGIONE']
incidenti = incidenti.sort_index()
patenti = patenti.sort_index()


patenti = patenti.reindex(order)
patenti = patenti['NUMERO'] / patenti['NUMERO'].sum()
incidenti = incidenti.reindex(order)
incidenti = incidenti['TOTALE'] / incidenti['TOTALE'].sum()

df = pd.DataFrame([patenti, incidenti], ['Patentati', 'Incidenti']).transpose()

# Colorazione del grafico
color_ls2 = ['#ce717a'] * 8
color_ls2 = color_ls2 + ['#ce717a'] * 4
color_ls2 = color_ls2 + ['#ce717a'] * 8

color_ls = ['#cec571'] * 8
color_ls = color_ls + ['#cec571'] * 4
color_ls = color_ls + ['#cec571'] * 8
color_ls = [color_ls, color_ls2]

df.plot.bar(width=0.9, color=color_ls)
plt.text(2, 0.18, "Nord Italia")
plt.text(8, 0.13, "Centro Italia")
plt.text(15, 0.10, "Sud Italia")
plt.xticks(rotation=90)
plt.xlabel("")
plt.ylabel("Percentuale di incidenti e patentati per regione")
plt.tight_layout()
plt.show()
