
import geopandas as gp
import matplotlib.pyplot as plt
import contextily as cx

path = "dataset/pave/tram/L010204.Shp"

data = gp.read_file(path).to_crs(epsg=3857)

ax = data.plot()
cx.add_basemap(ax=ax)
plt.ylim((5.69 * pow(10, 6), 5.7 * pow(10,6)))
plt.xlim((1.016 * pow(10, 6), 1.0278 * pow(10,6)))
plt.axis('off')
plt.show()