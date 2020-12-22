
import geopandas as gp
import matplotlib.pyplot as plt
import contextily as cx

data = gp.read_file("dataset/pave/asfalto.geojson").to_crs(epsg=3857)

ax = data.plot(figsize=(5,4), alpha=0.7, color='orange')
cx.add_basemap(ax = ax)
plt.axis('off')
plt.show()
