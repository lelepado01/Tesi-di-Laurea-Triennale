
import geopandas as gp
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import contextily as cx

color_ls = ['#8e50a8', '#506ba8']

path = "dataset/autovelox/autovelox_2014.csv"
autovelox = gp.read_file(path).set_crs(epsg=3857)
autovelox = gp.GeoDataFrame(geometry=gp.points_from_xy(autovelox['field_1'], autovelox['field_2']))

autovelox_tutti = gp.read_file("dataset/autovelox/autovelox_milano.geojson").to_crs(epsg=3857)

patches = [
    mpatches.Patch(color=color_ls[0], label='Installazioni nel 2014'), 
    mpatches.Patch(color=color_ls[1], label='Installazioni ignote')
    ]

# Per ottenere delle mappe di sfondo migliori rispetto a quella di default
providers = {}
def get_providers(provider):
    if "url" in provider:
        providers[provider['name']] = provider
    else:
        for prov in provider.values():
            get_providers(prov)
get_providers(cx.providers)

layer_i = autovelox_tutti.plot(color=color_ls[1],markersize=16, figsize=(7,5))
layer_a = autovelox.plot(ax=layer_i, color=color_ls[0],markersize=20)
plt.legend(handles=patches)
plt.axis('off')
cx.add_basemap(ax=layer_a, source=providers['OpenStreetMap.Mapnik'])
plt.show()

# Le coordinate degli autovelox trovati, che sono stati installati nel 2014, 
# sono state salvate nel file dal path dataset/autovelox/autovelox_2014.csv
