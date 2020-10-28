
import geopandas as gp
import matplotlib.pyplot as plt
import contextily as cx

data = gp.read_file("dataset/autostrade/a1/L010204.Shx").to_crs(epsg=3857)

#print(data)

ax = data.plot()
cx.add_basemap(ax=ax)
plt.show()