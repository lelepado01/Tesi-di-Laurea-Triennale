
import pandas as pd
import matplotlib.pyplot as plt
import sys
sys.path.append("src")
import aci_utils

# Divisione delle regioni tra nord sud e centro
regioni_nord = ['Piemonte', 'Valle d\'Aosta', 'Liguria', 'Lombardia', 
    'Trentino-Alto Adige', 'Veneto', 'Friuli-Venezia Giulia', 'Emilia Romagna']
regioni_centro = ['Toscana', 'Umbria', 'Marche', 'Lazio']
regioni_sud = ['Abruzzo', 'Molise', 'Campania', 'Puglia', 'Basilicata', 'Calabria', 
    'Sicilia', 'Sardegna']

patenti = pd.read_csv("dataset/patenti/patenti_mit.csv")
incidenti = pd.read_csv("dataset/incidenti/aci/autostrade/mesi_2018.csv")

incidenti = aci_utils.get_sum_of_fields(incidenti, 'REGIONE', 'TOTALE')

incidenti.index = incidenti['REGIONE']
patenti.index = patenti['REGIONE']
incidenti = incidenti.sort_index()

nord = incidenti.loc[regioni_nord]
centro = incidenti.loc[regioni_centro]
sud = incidenti.loc[regioni_sud]

nord_p = patenti.loc[regioni_nord]
centro_p = patenti.loc[regioni_centro]
sud_p = patenti.loc[regioni_sud]

plt.subplot(1,2,1)
plt.boxplot(nord['TOTALE'], positions=[1], widths=[0.6])
plt.boxplot(centro['TOTALE'], positions=[2], widths=[0.6])
plt.boxplot(sud['TOTALE'], positions=[3], widths=[0.6])
plt.xticks(range(1,4), ['Nord', 'Centro', 'Sud'], rotation=90)
plt.title("Incidenti all'anno (2018)")
plt.tight_layout()
plt.subplot(1,2,2)
plt.boxplot(nord_p['NUMERO'], positions=[1], widths=[0.6])
plt.boxplot(centro_p['NUMERO'], positions=[2], widths=[0.6])
plt.boxplot(sud_p['NUMERO'], positions=[3], widths=[0.6])
plt.xticks(range(1,4), ['Nord', 'Centro', 'Sud'], rotation=90)
plt.title("Patentati (2019)")
plt.tight_layout()
plt.show()