
import geopandas as gp
import matplotlib.pyplot as plt
import contextily as cx

scale = pow(10, 6)
bounds = [1.020 * scale, 1.025 * scale, 5.690 * scale, 5.696 * scale]

path_incidenti = "dataset/incidenti/inc_strad_milano_2016.geojson"
incidenti = gp.read_file(path_incidenti).to_crs(epsg=3857)

data = gp.read_file("dataset/zone_milano/zone.geojson").to_crs(epsg=3857)

autobus = data[data['name'] == "Navigli Autobus"]
street = data[data['name'] == "Navigli Incidenti"]

# Per ottenere delle mappe di background migliori rispetto a quella di default
providers = {}
def get_providers(provider):
    if "url" in provider:
        providers[provider['name']] = provider
    else:
        for prov in provider.values():
            get_providers(prov)

get_providers(cx.providers)


ax = autobus.plot(alpha=0.5, color='blue', figsize=(11,9))
ax2 = street.plot(ax=ax, alpha=0.5, color='green')
plt.ylim([bounds[2], bounds[3]])
cx.add_basemap(ax=ax2, source=providers['OpenStreetMap.Mapnik'])
plt.axis('off')
plt.show()


