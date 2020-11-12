
import geopandas as gp
import matplotlib.pyplot as plt
from shapely import geometry
import contextily as cx

incidenti = gp.read_file("dataset/incidenti/inc_strad_milano_2016.geojson").to_crs(epsg=3857)
area_c = geometry.Polygon(gp.read_file("dataset/area_c/area_c.geojson").to_crs(epsg=3857)['geometry'].iloc[0])

inc = 0
for point in incidenti['geometry']: 
    if area_c.contains(geometry.Point(point)): 
        inc += 1

#print(inc * 10**6/ area_c.area) # = 46.83 incidenti / km^2

ax = incidenti.plot(alpha = 0.08, figsize=(11,9))
cx.add_basemap(ax = ax)
plt.show()