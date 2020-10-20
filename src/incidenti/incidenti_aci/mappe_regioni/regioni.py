
# Voglio realizzare mappe italia per regione (bubblechart)
# https://github.com/openpolis/geojson-italy
# Download del file geojson con dati della regione

import geopandas as gp
import pandas as pd
import matplotlib.pyplot as plt

def get_sum_of_fields(data : pd.DataFrame, select_field : str, field_to_sum : str) -> pd.Series: 
    res = {}
    index = 0
    for reg in incidenti[select_field].unique():
        res[index] = [reg, 0]
        index += 1

    index = 0
    for reg in incidenti[select_field].unique():
        for row in incidenti[incidenti[select_field] == reg][field_to_sum]:
            res[index] = [res[index][0], res[index][1] + row]
        index += 1

    return pd.DataFrame(res, index=[select_field, field_to_sum]).transpose()


path = "dataset/regioni/regioni.geojson"
regioni = gp.read_file(path)

incidenti = pd.read_csv('dataset/incidenti/aci/strade_provinciali/aci_2014.csv')

res = get_sum_of_fields(incidenti, 'REGIONE', 'Inc')
#print(res)
regioni = gp.GeoDataFrame(res, geometry=regioni['geometry'].transpose())

# MAPPA non associa su regione, ma su indice PROBLEMA
#print(regioni[['Regione', 'Inc']])

#regioni.plot(column='Inc', cmap='OrRd')
#plt.show()

prov = gp.read_file("dataset/regioni/provincia.geojson")#.sort_values(by='prov_name')
print(prov.columns)

res = get_sum_of_fields(incidenti, "PROVINCIA", 'Inc')#.sort_values(by='PROVINCIA')
prov = gp.GeoDataFrame(res, geometry=prov['geometry'].transpose())

print(prov['Inc'])

prov.plot(column='Inc', cmap='OrRd')
plt.show()

# Voglio avere un punto centrale per ogni regione in modo da poter fare plot
# di una 'bubble'


#def parse_polygon(data : str) -> list: 
#    res = []
#    if "MULTI" in data: 
#        str(point)[16:][:-3].split(" ")
#    else: 
#        str(point)[10:][:-2].split(" ")
#
#
#def parse_polygons(data : gp.GeoDataFrame) -> list: 
#    res = []
#    for row in data.iterrows():
#        poly = parse_polygon(row['geometry'].astype(str))
#        res.append(get_center(poly))
#    
#    return res
#
#from shapely.geometry import Polygon
#centers = parse_polygons(regioni)
