
import geopandas as gp
import pandas as pd
import matplotlib.pyplot as plt
from shapely import geometry

municipi_data = gp.read_file("dataset/milano_municipi/Municipi.shx").to_crs(epsg=3857)
incidenti = gp.read_file("dataset/incidenti/inc_strad_milano_2016.geojson").to_crs(epsg=3857)

incidenti_per_municipio = {}
for m in municipi_data['MUNICIPIO']:
    incidenti_per_municipio[m] = 0

# Per ogni poligono e per ogni punto, conto gli incidenti contenuti nelle diverse zone
for m, poly in zip(municipi_data['MUNICIPIO'], municipi_data['geometry']):
    poly = geometry.Polygon(poly)

    for point in incidenti['geometry']: 
        point = geometry.Point(point)

        if poly.contains(point): 
            incidenti_per_municipio[m] += 1

inc = gp.GeoSeries(incidenti_per_municipio).sort_index()

municipi_data.index = municipi_data['MUNICIPIO']
municipi_data['Incidenti'] = inc

area = pd.Series(municipi_data['AREA'], index=municipi_data['MUNICIPIO'])
incidenti = pd.Series(inc, index=inc.index)

incidenti_per_zona = (incidenti / area) * 1000000

plt.subplot(1,2,1)
plt.bar(inc.index, inc, color='#5894dd', width=0.9)
plt.ylabel("Incidenti all'anno per zona")
plt.xticks(range(1,10))

plt.subplot(1,2,2)
plt.bar(incidenti_per_zona.index, incidenti_per_zona, label="incidenti pesati", color='#58d7dd', width=0.9)
plt.ylabel("Incidenti al chilometro quadrato per zona di Milano")
plt.xticks(range(1,10))

plt.show()

