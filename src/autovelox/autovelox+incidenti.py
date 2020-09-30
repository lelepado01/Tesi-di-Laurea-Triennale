
import geopandas as gp
import matplotlib.pyplot as plt
import contextily as cx

path_incidenti = "tesi/Tesi/dataset/incidenti/inc_strad_milano_2016.geojson"
path_autovelox = "tesi/Tesi/dataset/autovelox/autovelox_milano.geojson"

dati_incidenti = gp.read_file(path_incidenti).to_crs(epsg=3857)
dati_autovelox = gp.read_file(path_autovelox).to_crs(epsg=3857)

#layer_incidenti = dati_incidenti.plot(figsize=(11,9), color="blue", alpha=0.1)
#layer_autovelox = dati_autovelox.plot(ax=layer_incidenti, color="red")
#cx.add_basemap(ax=layer_autovelox)
#plt.show() 

# dovrei togliere i punti in alto (autovelox) che non rientrano nei dati incidenti

print(dati_autovelox['geometry'])