
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
patenti = patenti.sort_index()

incidenti_norm = incidenti['TOTALE'] / patenti['NUMERO']
# incidenti_norm.plot.bar()
# plt.show()

from matplotlib.lines import Line2D
import geopandas as gp

regioni = gp.read_file('dataset/regioni/regioni.geojson').to_crs(epsg=3857)
regioni.index = regioni['reg_name']
regioni = regioni.sort_index()

# inc_reg = gp.GeoDataFrame(incidenti_norm, geometry=regioni['geometry'])
# inc_reg.plot(column=0, cmap='OrRd')
# plt.title("Incidenti per regione / Patentati per regione")
# plt.axis('off')
# plt.show()

order = [
    'Piemonte', 'Valle d\'Aosta', 'Liguria', 'Lombardia', 
    'Trentino-Alto Adige', 'Veneto', 'Friuli-Venezia Giulia', 'Emilia Romagna', 
    'Toscana', 'Umbria', 'Marche', 'Lazio', 
    'Abruzzo', 'Molise', 'Campania', 'Puglia', 'Basilicata', 'Calabria', 
    'Sicilia', 'Sardegna'
]

# color_ls = ['#2eaad3'] * 8
# color_ls = color_ls + ['#2e57d3'] * 4
# color_ls = color_ls + ['#2ed3aa'] * 8
# color_ls = [color_ls, color_ls]

# patenti = patenti.reindex(order)
# patenti = patenti['NUMERO'] / patenti['NUMERO'].sum()
# incidenti = incidenti.reindex(order)
# incidenti = incidenti['TOTALE'] / incidenti['TOTALE'].sum()

# df = pd.DataFrame([patenti, incidenti], ['Patentati', 'Incidenti']).transpose()

# df.plot.bar(width=0.9)
# plt.text(2, 0.18, "Nord Italia")
# plt.text(8, 0.13, "Centro Italia")
# plt.text(15, 0.10, "Sud Italia")
# plt.xticks(rotation=90)
# plt.xlabel("")
# plt.ylabel("Percentuale di incidenti e patentati per regione")
# plt.tight_layout()
# plt.show()


nord = incidenti.loc[['Piemonte', 'Valle d\'Aosta', 'Liguria', 'Lombardia', 
    'Trentino-Alto Adige', 'Veneto', 'Friuli-Venezia Giulia', 'Emilia Romagna']]

centro = incidenti.loc[['Toscana', 'Umbria', 'Marche', 'Lazio']]

sud = incidenti.loc[['Abruzzo', 'Molise', 'Campania', 'Puglia', 'Basilicata', 'Calabria', 
    'Sicilia', 'Sardegna']]

# print(nord['TOTALE'].mean())
# print(centro['TOTALE'].mean())
# print(sud['TOTALE'].mean())

ita = pd.DataFrame([nord['TOTALE'], centro['TOTALE'], sud['TOTALE']], ['Nord', 'Centro', 'Sud']).transpose()

nord_p = patenti.loc[['Piemonte', 'Valle d\'Aosta', 'Liguria', 'Lombardia', 
    'Trentino-Alto Adige', 'Veneto', 'Friuli-Venezia Giulia', 'Emilia Romagna']]

centro_p = patenti.loc[['Toscana', 'Umbria', 'Marche', 'Lazio']]

sud_p = patenti.loc[['Abruzzo', 'Molise', 'Campania', 'Puglia', 'Basilicata', 'Calabria', 
    'Sicilia', 'Sardegna']]

# print(nord_p['NUMERO'].mean())
# print(centro_p['NUMERO'].mean())
# print(sud_p['NUMERO'].mean())

ita_p = pd.DataFrame([nord_p['NUMERO'], centro_p['NUMERO'], sud_p['NUMERO']], ['Nord', 'Centro', 'Sud']).transpose()

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