
import pandas as pd
import matplotlib.pyplot as plt

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

patenti = pd.read_csv("dataset/patenti/patenti_mit.csv")
incidenti = pd.read_csv("dataset/incidenti/aci/autostrade/mesi_2018.csv")

incidenti = get_sum_of_fields(incidenti, 'REGIONE', 'TOTALE')

incidenti.index = incidenti['REGIONE']
patenti.index = patenti['REGIONE']
incidenti = incidenti.sort_index()

regioni_nord = ['Piemonte', 'Valle d\'Aosta', 'Liguria', 'Lombardia', 
    'Trentino-Alto Adige', 'Veneto', 'Friuli-Venezia Giulia', 'Emilia Romagna']
regioni_centro = ['Toscana', 'Umbria', 'Marche', 'Lazio']
regioni_sud = ['Abruzzo', 'Molise', 'Campania', 'Puglia', 'Basilicata', 'Calabria', 
    'Sicilia', 'Sardegna']

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