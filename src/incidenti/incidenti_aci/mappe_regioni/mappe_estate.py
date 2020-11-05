
import geopandas as gp
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

field_incidenti = 'Agosto'
path = "dataset/regioni/regioni.geojson"
regioni = gp.read_file(path)

data = pd.read_csv('dataset/incidenti/aci/autostrade/mesi_2018.csv')
data = data[data['TOTALE'] != '0,0'].astype({'TOTALE': int})

incidenti = get_sum_of_fields(data, 'REGIONE', field_incidenti)

incidenti.index = incidenti['REGIONE']
regioni.index = regioni['reg_name']
# print(regioni)

regioni = gp.GeoDataFrame(incidenti[field_incidenti], geometry=regioni['geometry'].transpose())

from matplotlib.lines import Line2D

# regioni.plot(column=field_incidenti, cmap='OrRd', legend=True)
# # plt.title("Incidenti per regione nel 2014")
# plt.axis('off')
# plt.legend([
#     Line2D([],[],color='#a52317',linewidth=5), 
#     Line2D([],[],color='#d6584d',linewidth=5), 
#     Line2D([],[],color='#f7aca5',linewidth=5)
# ], [max(regioni[field_incidenti]), '1000', min(regioni[field_incidenti])])
# plt.show()

agosto = get_sum_of_fields(data, 'REGIONE', 'Agosto')
gennaio = get_sum_of_fields(data, 'REGIONE', 'Gennaio')

agosto.index = agosto['REGIONE']
gennaio.index = gennaio['REGIONE']
agosto = agosto['Agosto']
gennaio = gennaio['Gennaio']

red_ls = ['#f65578']*20
blue_ls = ['#70b8ff']*20

order = [
    'Piemonte', 'Valle d\'Aosta', 'Liguria', 'Lombardia', 
    'Trentino-Alto Adige', 'Veneto', 'Friuli-Venezia Giulia', 'Emilia Romagna', 
    'Toscana', 'Umbria', 'Marche', 'Lazio', 
    'Abruzzo', 'Molise', 'Campania', 'Puglia', 'Basilicata', 'Calabria', 
    'Sicilia', 'Sardegna'
]

nord = incidenti.loc[['Piemonte', 'Valle d\'Aosta', 'Liguria', 'Lombardia', 
    'Trentino-Alto Adige', 'Veneto', 'Friuli-Venezia Giulia', 'Emilia Romagna']]

centro = incidenti.loc[['Toscana', 'Umbria', 'Marche', 'Lazio']]

sud = incidenti.loc[['Abruzzo', 'Molise', 'Campania', 'Puglia', 'Basilicata', 'Calabria', 
    'Sicilia', 'Sardegna']]

agosto = agosto.reindex(order)
gennaio = gennaio.reindex(order)

pd.DataFrame([agosto, gennaio], ['Agosto', 'Gennaio']).transpose().plot.bar(width=0.9, color=[red_ls, blue_ls])

plt.text(2, 490, "Nord Italia")
plt.text(8, 320, "Centro Italia")
plt.text(15, 230, "Sud Italia")

plt.xticks(rotation=90)
plt.ylabel("Incidenti al mese (2018)")
plt.legend()
plt.tight_layout()
plt.show()