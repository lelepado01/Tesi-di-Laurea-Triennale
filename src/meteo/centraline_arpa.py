
import geopandas as gp
import matplotlib.pyplot as plt
import contextily as cx

path_incidenti = "dataset/incidenti/inc_strad_milano_2016.geojson"
path_sensori = "dataset/meteo/tipologia_sensori.geojson"

sensori = gp.read_file(path_sensori).to_crs(epsg=3857)
incidenti = gp.read_file(path_incidenti).to_crs(epsg=3857)

scale = 10**6

# Per avere una mappa di sfondo migliore rispetto a quella di default
providers = {}
def get_providers(provider):
    if "url" in provider:
        providers[provider['name']] = provider
    else:
        for prov in provider.values():
            get_providers(prov)

get_providers(cx.providers)

layer_sensori = sensori.plot(figsize=(5,4), markersize=10)
layer_incidenti = incidenti.plot(ax=layer_sensori, alpha=0.0)
cx.add_basemap(ax=layer_incidenti, source=providers['OpenStreetMap.Mapnik'])
plt.axis('off')
plt.xlim((1.017 * scale, 1.032 * scale))
plt.ylim((5.69 * scale, 5.705 * scale))
plt.show()