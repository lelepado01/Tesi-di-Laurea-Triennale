
import geopandas as gp
import matplotlib.pyplot as plt
import contextily as cx

import sys
sys.path.append("src")

path = "dataset/autovelox/autovelox_2014.csv"
autovelox = gp.read_file(path).set_crs(epsg=3857)
autovelox = gp.GeoDataFrame(geometry=gp.points_from_xy(autovelox['field_1'], autovelox['field_2']))

incidenti = gp.read_file("dataset/incidenti/inc_strad_milano_2016.geojson").to_crs(epsg=3857)

layer_i = incidenti.plot(color='blue', alpha=0.07, figsize=(11,9))
layer_a = autovelox.plot(ax=layer_i, color='red')
cx.add_basemap(ax=layer_a)
plt.show()
