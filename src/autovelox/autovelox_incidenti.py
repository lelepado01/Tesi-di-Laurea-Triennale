
import geopandas as gp
import matplotlib.pyplot as plt
from shapely import geometry
import contextily as cx

path = "dataset/autovelox/autovelox_2014.csv"
autovelox_2014 = gp.read_file(path).set_crs(epsg=3857)
autovelox_2014 = gp.GeoDataFrame(geometry=gp.points_from_xy(
    autovelox_2014['field_1'], 
    autovelox_2014['field_2']
    ))

incidenti = gp.read_file("dataset/incidenti/inc_strad_milano_2016.geojson").to_crs(epsg=3857)

MAX_DIST = 1500 # -> ~= 1 Km

df = {}
for i in autovelox_2014.index: 
    df[i] = 0

for i, point in zip(autovelox_2014.index, autovelox_2014['geometry']): 
    autovelox_point = geometry.Point(point)
    for inc_point in incidenti['geometry']: 
        inc_point = geometry.Point(inc_point)

        if autovelox_point.distance(inc_point) < MAX_DIST: 
            df[i] += 1
            
autovelox_2014['incidenti_vicini'] = gp.GeoSeries(df)
autovelox_2014['incidenti_pesati'] = autovelox_2014['incidenti_vicini'] / 3.14

x = incidenti.plot(alpha=0.0, figsize=(11,9))
ax = autovelox_2014.plot(
    ax = x, 
    column='incidenti_pesati',
    alpha=0.5, 
    markersize=(autovelox_2014['incidenti_vicini']/4) ** 2, 
    legend=True
    )

plt.axis('off')
cx.add_basemap(ax = ax)
plt.show()