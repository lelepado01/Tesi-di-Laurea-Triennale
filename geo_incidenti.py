
import matplotlib.pyplot as plt
import geopandas as gpd
import contextily as cx

path = "/Users/gabrielepadovani/Desktop/Università/Data/tesi/Tesi/dataset/incidenti/inc_strad_milano_2016.geojson"

data = gpd.read_file(path)
#print(type(data))
#world = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))
#print(gpd.datasets.available)

ax = data.plot(color="red", figsize=(13,10), alpha=0.05)
cx.add_basemap(ax, crs=data.crs.to_string())
plt.show()