
import geopandas as gp
import matplotlib.pyplot as plt
import contextily as cx

import sys
sys.path.append("src")

import geo_utils

path = "dataset/autovelox/autovelox_milano.geojson"

autovelox = gp.read_file(path).to_crs(epsg=3857)
#print(autovelox.columns)
#print(len(autovelox))

# Il dataset contiene alcuni campi superflui
#   id e @id

# print(autovelox[autovelox['id'] != autovelox['@id']])
#   restituisce un dataframe vuoto (sono due colonne uguali)

# controllo se ci sono altri campi tutti uguali: 
#for index in autovelox.columns: 
#    print(str(index) + ":  " + str(len(autovelox[index].unique())))

# questi campi hanno tutti un solo valore != None

#print(autovelox['addr:housenumber'].unique())
#print(autovelox['addr:city'].unique())
#print(autovelox['addr:postcode'].unique())
#print(autovelox['addr:street'].unique())
#print(autovelox['description'].unique())
#print(autovelox['type'].unique())

# I due fix dicono che uno non ha posizione precisa, e l'altro misura solo gli accessi

#print(autovelox['fixme'].unique())
#print(autovelox['fixme:2'].unique())

# questi campi sono removibili

#print(autovelox['surface'].unique())
#print(autovelox['layer'].unique())
#print(autovelox['highway'].unique()) # -> SOLO speed_camera
#print(autovelox['old_name'].unique())
#print(autovelox['alt_name'].unique())
#print(autovelox['direction'].unique())

layer_autovelox = autovelox.plot(figsize=(11,9), color="red")
layer_autovelox.set_title("Autovelox Milano")

index = 0
for lat, lon in geo_utils.parse_geojson_point_list(autovelox['geometry'].astype(str)):
   layer_autovelox.text(lat, lon, s=index)
   index += 1

cx.add_basemap(ax=layer_autovelox)
plt.show()

# Gli indici mi permettono di individuare quali sono gli autovelox installati nel 2014: 
# 46, 50
# 44, 28
# 27
# 47 e 64
# 61, 66, 63
# 40, 41, 42, 43
# 26 ? questa linea non è sicura (alto a destra)
# 

indici_autovelox = [59, 60, 44, 28, 27, 47, 64, 61, 63, 66, 40, 41, 42, 43, 26, 58]
#
#for i in indici_autovelox: 
#    print(autovelox['geometry'].get(i))

installati = gp.read_file("dataset/autovelox/autovelox_2014.csv").set_crs(epsg=3857)
installati = gp.GeoDataFrame(geometry=gp.points_from_xy(installati['field_1'], installati['field_2']))

#print(installati)

ax = installati.plot(figsize=(11,9))
cx.add_basemap(ax=ax)
plt.show()