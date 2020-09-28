
import matplotlib.pyplot as plt
import geopandas as gpd
import contextily as cx

path = "/Users/gabrielepadovani/Desktop/Università/Data/tesi/Tesi/dataset/incidenti/inc_strad_milano_2016.geojson"

# to_crs(...) è per fare in modo che la mappa sia in proiezione di Mercatore
# se non lo metto la mappa diventa 'obliqua'

data = gpd.read_file(path).to_crs(epsg=3857)
#print(type(data))
#world = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))
#print(gpd.datasets.available)

ax = data.plot(color="red", figsize=(11,9), alpha=0.05)
cx.add_basemap(ax, crs=data.crs.to_string())
plt.show()