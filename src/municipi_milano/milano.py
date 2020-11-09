
import geopandas as gp
import pandas as pd
import contextily as cx
import matplotlib.pyplot as plt
from matplotlib.pyplot import legend
from shapely.geometry import geo


data = gp.read_file("dataset/milano_municipi/Municipi.shx").to_crs(epsg=3857)

incidenti = gp.read_file("dataset/incidenti/inc_strad_milano_2016.geojson").to_crs(epsg=3857)

df = {}

for m in data['MUNICIPIO']:
    df[m] = 0

from shapely import geometry

# for m, poly in zip(data['MUNICIPIO'], data['geometry']):

#     poly = geometry.Polygon(poly)

#     for point in incidenti['geometry']: 
#         point = geometry.Point(point)

#         if poly.contains(point): 
#             df[m] += 1

# inc = gp.GeoSeries(df).sort_index()

# data.index = data['MUNICIPIO']
# data['Incidenti'] = inc

# area = pd.Series(data['AREA'], index=data['MUNICIPIO'])
# area = area / area.sum()
#incidenti = pd.Series(inc, index=inc.index)
# print(area)
# print(incidenti)
#incidenti_per_zona = (incidenti / area) * 1000000
#print(incidenti_per_zona)

# plt.subplot(1,2,1)
# plt.bar(inc.index, inc, color='#5894dd', width=0.9)
# plt.ylabel("Incidenti all'anno per zona")
# plt.xticks(range(1,10))

# plt.subplot(1,2,2)
# plt.bar(incidenti_per_zona.index, incidenti_per_zona, label="incidenti pesati", color='#58d7dd', width=0.9)
# plt.ylabel("Incidenti al chilometro quadrato per zona di Milano")
# plt.xticks(range(1,10))

# plt.show()

# fig, (ax1, ax2) = plt.subplots(ncols=2, sharex=True, sharey=True)
# layer_m = data.plot(ax = ax1, column='Incidenti', cmap='OrRd', alpha=0.5, legend=True)
# cx.add_basemap(ax=layer_m)
# inc_layer = incidenti.plot(ax=ax2, alpha=0.02)
# cx.add_basemap(ax=inc_layer)
# plt.show()

base = 10**6 
up = 5.699 * base
down = 5.698 * base
left = 1.0255 * base
right = 1.027 * base

p1 = geometry.Point(left , up)
p2 = geometry.Point(right, up)
p3 = geometry.Point(left , down)
p4 = geometry.Point(right, down)

loreto = geometry.Polygon([p1, p2, p4, p3])

df = gp.GeoDataFrame(geometry=[loreto]).set_crs(epsg=3857)
ax = df.plot(color='#ff0000')
inc = incidenti.plot(ax = ax, alpha=0.05)
cx.add_basemap(ax=inc)
plt.show()