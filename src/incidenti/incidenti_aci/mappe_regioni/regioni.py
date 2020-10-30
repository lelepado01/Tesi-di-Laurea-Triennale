
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


path = "dataset/regioni/regioni.geojson"
regioni = gp.read_file(path)

incidenti_2011 = get_sum_of_fields(pd.read_csv('dataset/incidenti/aci/strade_provinciali/aci_2011.csv'), 'REGIONE', 'Inc').sort_values('REGIONE',inplace=False, ascending=True)
incidenti_2012 = get_sum_of_fields(pd.read_csv('dataset/incidenti/aci/strade_provinciali/aci_2012.csv'), 'REGIONE', 'Inc').sort_values('REGIONE',inplace=False, ascending=True)
incidenti_2014 = get_sum_of_fields(pd.read_csv('dataset/incidenti/aci/strade_provinciali/aci_2014.csv'), 'REGIONE', 'Inc').sort_values('REGIONE',inplace=False, ascending=True)
incidenti_2015 = get_sum_of_fields(pd.read_csv('dataset/incidenti/aci/strade_provinciali/aci_2015.csv'), 'REGIONE', 'Inc').sort_values('REGIONE',inplace=False, ascending=True)
incidenti_2016 = get_sum_of_fields(pd.read_csv('dataset/incidenti/aci/strade_provinciali/aci_2016.csv'), 'REGIONE', 'Inc').sort_values('REGIONE',inplace=False, ascending=True)
incidenti_2017 = get_sum_of_fields(pd.read_csv('dataset/incidenti/aci/strade_provinciali/aci_2017.csv'), 'REGIONE', 'Inc').sort_values('REGIONE',inplace=False, ascending=True)
incidenti_2018 = get_sum_of_fields(pd.read_csv('dataset/incidenti/aci/strade_provinciali/aci_2018.csv'), 'REGIONE', 'Inc').sort_values('REGIONE',inplace=False, ascending=True)

incidenti_2011.set_index(incidenti_2011['REGIONE'], inplace=True)
incidenti_2012.set_index(incidenti_2012['REGIONE'], inplace=True)
incidenti_2014.set_index(incidenti_2014['REGIONE'], inplace=True)
incidenti_2015.set_index(incidenti_2015['REGIONE'], inplace=True)
incidenti_2016.set_index(incidenti_2016['REGIONE'], inplace=True)
incidenti_2017.set_index(incidenti_2017['REGIONE'], inplace=True)
incidenti_2018.set_index(incidenti_2018['REGIONE'], inplace=True)

# incidenti_2011 = incidenti_2011['Inc']
# incidenti_2012 = incidenti_2012['Inc']
# incidenti_2014 = incidenti_2014['Inc']
# incidenti_2015 = incidenti_2015['Inc']
# incidenti_2016 = incidenti_2016['Inc']
# incidenti_2017 = incidenti_2017['Inc']
# incidenti_2018 = incidenti_2018['Inc']

df = pd.DataFrame([
    incidenti_2011['Inc'],
    incidenti_2012['Inc'],
    incidenti_2014['Inc'],
    incidenti_2015['Inc'],
    incidenti_2016['Inc'],
    incidenti_2017['Inc'],
    incidenti_2018['Inc']
], [2011,2012,2014,2015,2016,2017,2018])

df = df.transpose()

import sys
sys.path.append('src')
import heatmap as H

fig, ax = plt.subplots()

im, cbar = H.heatmap(df, df.index, [2011,2012,2014,2015,2016,2017,2018], ax=ax, cmap="YlGn", xticks_rotated=True, cbarlabel="Incidenti all'anno per regione")
#texts = H.annotate_heatmap(im, valfmt="{x}")

plt.show()

#print(res)
# regioni = gp.GeoDataFrame(res, geometry=regioni['geometry'].transpose())

# MAPPA non associa su regione, ma su indice PROBLEMA
#print(regioni[['Regione', 'Inc']])

# from matplotlib.lines import Line2D

# regioni.plot(column='Inc', cmap='OrRd', legend=True)
# #plt.title("Incidenti per regione nel 2014")
# plt.axis('off')
# plt.legend([
#     Line2D([],[],color=(214/255, 0,0,1),linewidth=5), 
#     Line2D([],[],color=(1, 168/255,150/255,1),linewidth=5), 
#     Line2D([],[],color=(1, 221/255,171/255,1),linewidth=5)
# ], [max(regioni['Inc']), '1000', min(regioni['Inc'])])
# plt.show()

