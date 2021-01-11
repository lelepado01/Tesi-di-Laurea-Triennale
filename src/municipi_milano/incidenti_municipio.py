
import geopandas as gp
import contextily as cx
import matplotlib.pyplot as plt
from shapely import geometry

data = gp.read_file("dataset/milano_municipi/Municipi.shx").to_crs(epsg=3857)
incidenti = gp.read_file("dataset/incidenti/inc_strad_milano_2016.geojson").to_crs(epsg=3857)

incidenti_per_municipio = {}
for m in data['MUNICIPIO']:
    incidenti_per_municipio[m] = 0

for m, poly in zip(data['MUNICIPIO'], data['geometry']):
    poly = geometry.Polygon(poly)

    for point in incidenti['geometry']: 
        point = geometry.Point(point)

        if poly.contains(point): 
            incidenti_per_municipio[m] += 1

data.index = data['MUNICIPIO']

inc = gp.GeoSeries(incidenti_per_municipio).sort_index()
data['Incidenti'] = inc

layer_m = data.plot(column='Incidenti', cmap='OrRd', alpha=0.5, figsize=(9,7))
cx.add_basemap(ax=layer_m)
plt.axis('off')
plt.show()