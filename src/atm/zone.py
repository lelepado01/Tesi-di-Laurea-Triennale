
import geopandas as gp
import matplotlib.pyplot as plt
import contextily as cx

scale = pow(10, 6)

path_incidenti = "dataset/incidenti/inc_strad_milano_2016.geojson"
incidenti = gp.read_file(path_incidenti).to_crs(epsg=3857)

# Navigli
bounds = [1.020 * scale, 1.025 * scale, 5.690 * scale, 5.696 * scale]
data = gp.read_file("dataset/zone_milano/zone.geojson").to_crs(epsg=3857)

autobus = data[data['name'] == "Navigli Autobus"]
ax = autobus.plot(alpha=0.5, color='orange')

street = data[data['name'] == "Navigli Incidenti"]
ax2 = street.plot(ax=ax, alpha=0.5, color='yellow')

plt.ylim([bounds[2], bounds[3]])
cx.add_basemap(ax=ax2)
plt.show()
