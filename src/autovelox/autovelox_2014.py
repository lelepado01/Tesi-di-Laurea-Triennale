
import geopandas as gp
import matplotlib.pyplot as plt
import contextily as cx

import sys

from matplotlib.pyplot import legend
sys.path.append("src")

color_ls = ['#8e50a8', '#506ba8']

path = "dataset/autovelox/autovelox_2014.csv"
autovelox = gp.read_file(path).set_crs(epsg=3857)
autovelox = gp.GeoDataFrame(geometry=gp.points_from_xy(autovelox['field_1'], autovelox['field_2']))

autovelox_tutti = gp.read_file("dataset/autovelox/autovelox_milano.geojson").to_crs(epsg=3857)

import matplotlib.patches as mpatches
patches = [
    mpatches.Patch(color=color_ls[0], label='Installazioni nel 2014'), 
    mpatches.Patch(color=color_ls[1], label='Installazioni ignote')
    ]

layer_i = autovelox_tutti.plot(color=color_ls[1],markersize=16, figsize=(7,5))
layer_a = autovelox.plot(ax=layer_i, color=color_ls[0],markersize=20)
plt.legend(handles=patches)
plt.axis('off')
cx.add_basemap(ax=layer_a)
plt.show()
