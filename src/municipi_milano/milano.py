
import geopandas as gp
import contextily as cx
import matplotlib.pyplot as plt


data = gp.read_file("dataset/milano/Municipi.shx").to_crs(epsg=3857)

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

inc = gp.GeoSeries(df)

data.index = data['MUNICIPIO']
data['Incidenti'] = inc

print(data)

data.plot(column='Incidenti', cmap='OrRd')
plt.show()