
import geopandas as gp
import matplotlib.pyplot as plt
import contextily as cx

scale = pow(10, 6)

path_incidenti = "dataset/incidenti/inc_strad_milano_2016.geojson"
incidenti = gp.read_file(path_incidenti).to_crs(epsg=3857)

bounds = [1.020 * scale, 1.025 * scale, 5.690 * scale, 5.696 * scale]
data = gp.read_file("dataset/zone_milano/zone.geojson").to_crs(epsg=3857)

bianca = data[data['name'] == "Bianca Maria"]
premuda = data[data['name'] == "Premuda"]

providers = {}
def get_providers(provider):
    if "url" in provider:
        providers[provider['name']] = provider
    else:
        for prov in provider.values():
            get_providers(prov)

# Per ottenere delle mappe di background migliori rispetto a quella di default
get_providers(cx.providers)

ax1 = bianca.plot(color='blue', alpha=0.5, figsize=(11,9))
ax2 = premuda.plot(ax = ax1, color='green', alpha=0.5)
plt.ylim([5.693 * scale, 5.697 * scale])
plt.xlim([1.022 * scale, 1.026 * scale])
cx.add_basemap(ax=ax2, source=providers['OpenStreetMap.Mapnik'])
plt.axis('off')
plt.show()
