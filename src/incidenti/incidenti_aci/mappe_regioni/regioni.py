
# Voglio realizzare mappe italia per regione (bubblechart)
# https://github.com/openpolis/geojson-italy
# Download del file geojson con dati della regione

import geopandas as gp
import pandas as pd
import matplotlib.pyplot as plt

path = "dataset/regioni/regioni.geojson"

regioni = gp.read_file(path)

incidenti = pd.read_csv('dataset/incidenti/aci/strade_provinciali/aci_2014.csv')

res = {}
index = 0
for reg in incidenti['REGIONE'].unique():
    res[index] = [reg, 0]
    index += 1

index = 0
for reg in incidenti['REGIONE'].unique():
    for row in incidenti[incidenti['REGIONE'] == reg]['Inc']:
        res[index] = [res[index][0], res[index][1] + row]
    index += 1

#print(regioni)
res = pd.DataFrame(res, index=['Regione', 'Inc']).transpose()
#print(res)
regioni = gp.GeoDataFrame(res, geometry=regioni['geometry'].transpose())

# MAPPA non associa su regione, ma su indice PROBLEMA
#print(regioni[['Regione', 'Inc']])

regioni.plot(column='Inc', cmap='OrRd')
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
