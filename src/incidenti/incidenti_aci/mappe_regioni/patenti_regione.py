
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
incidenti = pd.read_csv("dataset/incidenti/aci/autostrade/mesi_2012.csv")

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

inc_reg = gp.GeoDataFrame(incidenti_norm, geometry=regioni['geometry'])
inc_reg.plot(column=0, cmap='OrRd')
plt.title("Incidenti per regione / Patentati per regione")
plt.axis('off')
plt.show()