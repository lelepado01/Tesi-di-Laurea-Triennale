
import geopandas as gp
import contextily as cx
import matplotlib.pyplot as plt
from matplotlib.pyplot import axis

data = gp.read_file("dataset/milano_municipi/Municipi.shx").to_crs(epsg=3857)

incidenti = gp.read_file("dataset/incidenti/inc_strad_milano_2016.geojson").to_crs(epsg=3857)

df = {}

for m in data['MUNICIPIO']:
    df[m] = 0

from shapely import geometry

for m, poly in zip(data['MUNICIPIO'], data['geometry']):

    poly = geometry.Polygon(poly)

    for point in incidenti['geometry']: 
        point = geometry.Point(point)

        if poly.contains(point): 
            df[m] += 1

data.index = data['MUNICIPIO']

inc = gp.GeoSeries(df).sort_index()
data['Incidenti'] = inc

# print(data)

fig, (ax1, ax2) = plt.subplots(ncols=2, sharex=True, sharey=True)
ax1.axis('off')
layer_m = data.plot(ax = ax1, column='Incidenti', cmap='OrRd', alpha=0.5, legend=True)
cx.add_basemap(ax=layer_m)
inc_layer = incidenti.plot(ax=ax2, alpha=0.02)
cx.add_basemap(ax=inc_layer)
plt.axis('off')
# plt.savefig("incidenti_municipio")
plt.show()