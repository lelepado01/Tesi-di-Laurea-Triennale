
import geopandas as gp
import matplotlib.pyplot as plt
import contextily as cx
import sys

sys.path.append("src/")

import utils

path_incidenti = "dataset/incidenti/inc_strad_milano_2016.geojson"
path_autovelox = "dataset/autovelox/autovelox_milano.geojson"

dati_incidenti = gp.read_file(path_incidenti).to_crs(epsg=3857)
dati_autovelox = gp.read_file(path_autovelox).to_crs(epsg=3857)

# MAPPA 1
#layer_incidenti = dati_incidenti.plot(figsize=(11,9), color="blue", alpha=0.1)
#layer_autovelox = dati_autovelox.plot(ax=layer_incidenti, color="red")
#cx.add_basemap(ax=layer_autovelox)
#plt.show() 

# dovrei togliere i punti in alto (autovelox) che non rientrano nei dati incidenti

scale = pow(10, 6)
UPPER_BOUND = 5.7055 * scale
LOWER_BOUND = 5.687 * scale
LEFT_BOUND = 1.01 * scale
RIGHT_BOUND = 1.032 * scale

autovelox_ridotti = dati_autovelox[utils.remove_points_out_of_range(
    dati_autovelox['geometry'], 
    [UPPER_BOUND, LOWER_BOUND, LEFT_BOUND, RIGHT_BOUND]
)]

#print(len(autovelox_ridotti))

# MAPPA 2
#layer_incidenti = dati_incidenti.plot(figsize=(11,9), color="blue", alpha=0.07)
#layer_autovelox = autovelox_ridotti.plot(ax=layer_incidenti, color="red")
#cx.add_basemap(ax=layer_autovelox)
#plt.show()

# Ho ridotto il numero di autovelox a 45, ma quelli rimossi erano lontani dai 
# principali punti di incidente
# Riduco anche il numero di incidenti in modo da togliere quelli troppo lontani 
# dal centro

#print(dati_incidenti['geometry'])

incidenti_ridotti = dati_incidenti[utils.remove_points_out_of_range(
    dati_incidenti['geometry'], 
    [UPPER_BOUND, LOWER_BOUND, LEFT_BOUND, RIGHT_BOUND]
)]

# Ho rimosso circa 100 incidenti
#print(len(dati_incidenti))     -> 8600
#print(len(incidenti_ridotti))  -> 8500

# MAPPA 3
layer_incidenti = incidenti_ridotti.plot(figsize=(11,9), color="blue", alpha=0.07)
layer_autovelox = autovelox_ridotti.plot(ax=layer_incidenti, color="red")
cx.add_basemap(ax=layer_autovelox)
plt.show()