
from math import pi
from attr import field
import geopandas as gp
import matplotlib.pyplot as plt
import contextily as cx
import sys

from numpy.core.defchararray import index
from shapely import geometry
sys.path.append("src/")
import geo_utils

from shapely.geometry import mapping, Point

path = "dataset/atm/atm_percorsi.geojson"
percorsi_atm = gp.read_file(path).to_crs(epsg=3857)

# scale = pow(10, 6)
# UPPER_BOUND = 5.708 * scale
# LOWER_BOUND = 5.683 * scale
# LEFT_BOUND = 1.007 * scale
# RIGHT_BOUND = 1.036 * scale

# percorsi_ridotti = percorsi_atm[geo_utils.remove_lines_out_of_range(
#     percorsi_atm['geometry'],
#     [UPPER_BOUND, LOWER_BOUND, LEFT_BOUND, RIGHT_BOUND]
#     )]

# layer_m = percorsi_ridotti.plot(color='red', linewidth=0.9, figsize=(11,9))
# cx.add_basemap(ax=layer_m)
# plt.axis('off')
# plt.show()

# import numpy as np

# path_incidenti = "dataset/incidenti/inc_strad_milano_2016.geojson"
# incidenti = gp.read_file(path_incidenti).to_crs(epsg=3857)

# for point in incidenti['geometry']: 
#     point = mapping(point)
#     point['coordinates'] = np.round(point['coordinates'], 6)


# df = {}
# for point in incidenti['geometry'].unique(): 
#     point = mapping(point)
#     df[point['coordinates']] = 0

# for point in incidenti['geometry']: 
#     point = mapping(point)
#     df[point['coordinates']] += 1


# incidenti = gp.GeoDataFrame(df, index=['val']).transpose()
# print(incidenti)

import numpy as np

incidenti = gp.read_file("dataset/incidenti/incidenti_round.csv")
incidenti = gp.GeoDataFrame(incidenti['field_3'], geometry=gp.points_from_xy(incidenti['field_2'], incidenti['field_1'])).set_crs(epsg=4326).to_crs(epsg=3857)
incidenti['field_3'] = incidenti['field_3'].astype(float)

ax = incidenti.plot(
    figsize=(9,7),
    alpha=0.8,
    column='field_3',
    markersize=incidenti['field_3'].astype(int) **1.8,
    cmap='viridis'
    )

cx.add_basemap(ax = ax)
plt.axis('off')
plt.show()