
import geopandas as gp
import matplotlib.pyplot as plt
from shapely import geometry 
import contextily as cx

data = gp.read_file("dataset/pave/asfalto.geojson").to_crs(epsg=3857)

ax = data.plot(figsize=(11,9), alpha=0.7)
cx.add_basemap(ax = ax)
plt.show()

# area = 0
# for shape in data['geometry']: 
#     area += geometry.Polygon(shape).area

# incidenti = gp.read_file("dataset/incidenti/inc_strad_milano_2016.geojson").to_crs(epsg=3857)

# inc = 0
# for shape in data['geometry']: 
#     shape = geometry.Polygon(shape)

#     for point in incidenti['geometry']: 
#         if shape.contains(geometry.Point(point)): 
#             inc += 1


#print(inc * 10**6/ area)# = 220.89


# print(area) 