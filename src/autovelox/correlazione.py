
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

        #print(autovelox_point.distance(inc_point))
        if autovelox_point.distance(inc_point) < MAX_DIST: 
            df[i] += 1
            
autovelox_2014['incidenti_vicini'] = gp.GeoSeries(df)

# print(autovelox_2014)
# print(df)

x = incidenti.plot(alpha=0.01)
ax = autovelox_2014.plot(ax = x, markersize=autovelox_2014['incidenti_vicini'], alpha=0.4, color='orange', legend=True)
cx.add_basemap(ax = ax)
plt.show()

#                            geometry  incidenti_vicini
# 0   POINT (1024096.591 5701313.468)               194
# 1   POINT (1024082.787 5701260.656)               202
# 2   POINT (1016387.327 5700465.856)               208
# 3   POINT (1016422.915 5700131.103)               212
# 4   POINT (1022149.902 5701766.778)               166
# 5   POINT (1013313.951 5693035.129)                95
# 6   POINT (1013459.145 5693117.646)               100
# 7   POINT (1019736.741 5690611.472)               180
# 8   POINT (1021377.846 5685420.950)                23
# 9   POINT (1023707.986 5689096.052)                57
# 10  POINT (1019215.576 5699438.989)               291
# 11  POINT (1019208.953 5699446.595)               290
# 12  POINT (1018599.545 5698878.724)               296
# 13  POINT (1018605.612 5698871.816)               296
# 14  POINT (1028650.638 5700506.610)               149
# 15  POINT (1028636.645 5700511.898)               149


# df = {}
# for i, inc_point in zip(incidenti.index, incidenti['geometry']): 
#     inc_point = geometry.Point(inc_point)
#     point = autovelox_2014['geometry'].iloc[0] 
#     autovelox_point = geometry.Point(point)

#     df[i] = autovelox_point.distance(inc_point) < MAX_DIST
            
# # print(df)


# incidenti['IN'] = gp.GeoSeries(df)

# x = incidenti.plot(alpha=0.03, column='IN')
# #ax = autovelox_2014.plot(ax = x, markersize=autovelox_2014['incidenti_vicini'], alpha=0.4, color='orange')
# cx.add_basemap(ax = x)
# plt.show()

