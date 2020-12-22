
import geopandas as gp
import matplotlib.pyplot as plt
import contextily as cx

pave = gp.read_file("dataset/pave/pave.geojson").to_crs(epsg=3857)
incidenti = gp.read_file("dataset/incidenti/inc_strad_milano_2016.geojson").to_crs(epsg=3857)

ax = pave.plot(figsize=(5,4), alpha=0.7)
cx.add_basemap(ax=ax)
plt.axis('off')
plt.show()