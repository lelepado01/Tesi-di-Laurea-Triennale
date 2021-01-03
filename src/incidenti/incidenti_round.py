
import geopandas as gp
from shapely.geometry import mapping
import numpy as np

import matplotlib.pyplot as plt
import contextily as cx

incidenti = gp.read_file("dataset/incidenti/inc_strad_milano_2016.geojson")

df = {}
for point in incidenti['geometry']: 
    point = mapping(point)
    rounded_x, rounded_y = np.round(np.array(point['coordinates']),5)

    if (rounded_x, rounded_y) in df.keys(): 
        df[(rounded_x, rounded_y)] += 1
    else: 
        df[(rounded_x, rounded_y)] = 1

rounded = gp.GeoDataFrame(df.values(), geometry=gp.points_from_xy([i[0] for i in df.keys()], [i[1] for i in df.keys()]))

# ax = rounded.plot(
#     figsize=(9,7),
#     alpha=0.8,
#     column=0,
#     markersize=rounded[0].astype(int) **1.8,
#     cmap='viridis'
#     )

# cx.add_basemap(ax = ax)
# plt.axis('off')
# plt.show()