
import geopandas as gp
import matplotlib.pyplot as plt
import contextily as cx

path_atm = "tesi/Tesi/dataset/atm/atm_percorsi.geojson"
path_incidenti = "tesi/Tesi/dataset/incidenti/inc_strad_milano_2016.geojson"

percorsi_atm = gp.read_file(path_atm).to_crs(epsg=3857)
incidenti = gp.read_file(path_incidenti).to_crs(epsg=3857)

layer_percorsi = percorsi_atm.plot(color="red", figsize=(11,9))
layer_incidenti = incidenti.plot(ax=layer_percorsi, alpha=0.05)
cx.add_basemap(ax=layer_incidenti)
plt.show()

# PROBLEMA: la mappa degli autobus è più alta rispetto a quella degli incidenti 
#   in geo_atm+incidenti.py ho risolto 