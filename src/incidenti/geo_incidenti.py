
import pandas as pd
import matplotlib.pyplot as plt
import geopandas as gpd
import contextily as cx

import sys
sys.path.append('src')

import geo_utils

path = "dataset/incidenti/inc_strad_milano_2016.geojson"

# to_crs(...) è per fare in modo che la mappa sia in proiezione di Mercatore
# se non lo metto la mappa diventa 'obliqua'

data = gpd.read_file(path).to_crs(epsg=3857)
#print(type(data))
#world = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))
#print(gpd.datasets.available)

#ax = data.plot(figsize=(11,9), alpha=0.05)
#cx.add_basemap(ax, crs=data.crs.to_string())
#plt.show()

# Ci sono dei punti in cui avvengono molti incidenti "sovrapposti", sono errori nei dati o 
# sono punti con alta incidentalità?

def print_zoomed_graph(data : gpd.GeoDataFrame, bounds : list, label=""): 
    ax = data.plot(figsize=(11,9), alpha=0.5, xlabel = label)
    ax.set_xlim([bounds[0], bounds[1]])
    ax.set_ylim([bounds[2], bounds[3]])
    cx.add_basemap(ax, crs=data.crs.to_string(), zoom=14)
    plt.show()


scale = pow(10, 6)
UPPER_BOUND = 5.690 * scale
LOWER_BOUND = 5.687 * scale
LEFT_BOUND = 1.028 * scale
RIGHT_BOUND = 1.030 * scale

#zoom_tangenziale = data[geo_utils.remove_points_out_of_range(
#    data['geometry'], 
#    [UPPER_BOUND, LOWER_BOUND, LEFT_BOUND, RIGHT_BOUND]
#)]#['geometry'].astype(str).value_counts()
#
#print(zoom_tangenziale)

#print_zoomed_graph(data, [LEFT_BOUND, RIGHT_BOUND, LOWER_BOUND, UPPER_BOUND])

# Ho 22 incidenti con le stesse coordinate, mi sembra un errore più che un punto pericoloso
# (Tangenziale est)
# Un punto in cui avvengono molti incidenti, come piazzale Loreto, ha molti incidenti, 
# ma tutti hanno coordinate diverse: 

UPPER_BOUND = 5.699 * scale
LOWER_BOUND = 5.698 * scale
LEFT_BOUND = 1.025 * scale
RIGHT_BOUND = 1.027 * scale

#zoom_loreto = data[geo_utils.remove_points_out_of_range(
#    data['geometry'], 
#    [UPPER_BOUND, LOWER_BOUND, LEFT_BOUND, RIGHT_BOUND]
#)]['geometry'].astype(str).value_counts()

#print(zoom_loreto)

#print_zoomed_graph(data, [LEFT_BOUND, RIGHT_BOUND, LOWER_BOUND, UPPER_BOUND], label="Loreto")

# Loreto ha alcuni punti sovrapposti, ma la maggior parte sono omogeneamente distribuiti
# Ho un punto simile sulla tangenziale ovest: 

UPPER_BOUND = 5.695 * scale
LOWER_BOUND = 5.693 * scale
LEFT_BOUND = 1.010 * scale
RIGHT_BOUND = 1.012 * scale
#print_zoomed_graph(data, [LEFT_BOUND, RIGHT_BOUND, LOWER_BOUND, UPPER_BOUND])

# E anche a <5.697, 1.013>

UPPER_BOUND = 5.698 * scale
LOWER_BOUND = 5.696 * scale
LEFT_BOUND = 1.012 * scale
RIGHT_BOUND = 1.014 * scale
print_zoomed_graph(data, [LEFT_BOUND, RIGHT_BOUND, LOWER_BOUND, UPPER_BOUND])
