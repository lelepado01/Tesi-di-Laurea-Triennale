
import geopandas as gp
import matplotlib.pyplot as plt
import contextily as cx

path_incidenti = "dataset/incidenti/inc_strad_milano_2016.geojson"
path_sensori = "dataset/meteo/tipologia_sensori.geojson"

sensori = gp.read_file(path_sensori).to_crs(epsg=3857)
incidenti = gp.read_file(path_incidenti).to_crs(epsg=3857)

# uso gli incidenti in modo da avere la posizione delle centraline 
# relativamente al centro di milano

layer_sensori = sensori.plot(figsize=(11,9))
layer_incidenti = incidenti.plot(ax=layer_sensori, alpha=0.0)
cx.add_basemap(ax=layer_incidenti)
plt.show()