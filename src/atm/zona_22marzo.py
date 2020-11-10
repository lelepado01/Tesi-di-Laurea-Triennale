
import geopandas as gp
import matplotlib.pyplot as plt
import contextily as cx

scale = pow(10, 6)

path_incidenti = "dataset/incidenti/inc_strad_milano_2016.geojson"
incidenti = gp.read_file(path_incidenti).to_crs(epsg=3857)

# Navigli
bounds = [1.020 * scale, 1.025 * scale, 5.690 * scale, 5.696 * scale]
data = gp.read_file("dataset/zone_milano/zone.geojson").to_crs(epsg=3857)

bianca = data[data['name'] == "Bianca Maria"]#['geometry'].iloc[0]
premuda = data[data['name'] == "Premuda"]#['geometry'].iloc[0]

ax1 = bianca.plot(color='orange', alpha=0.5)
ax2 = premuda.plot(ax = ax1, color='yellow', alpha=0.5)
plt.ylim([5.693 * scale, 5.697 * scale])
plt.xlim([1.022 * scale, 1.026 * scale])
cx.add_basemap(ax=ax2)
plt.show()

# from shapely import geometry

# bianca_rect = geometry.Polygon(bianca)
# premuda_rect = geometry.Polygon(premuda)

# inc_a = 0
# inc_s = 0
# for point in incidenti['geometry']: 
#     point = geometry.Point(point)

#     if bianca_rect.contains(point): 
#         inc_a += 1
    
#     if premuda_rect.contains(point): 
#         inc_s += 1

# print("Incidenti su linea autobus: " + str(inc_s * scale / premuda_rect.area))
# # = 93.96
# print("Incidenti su strada senza linea: "+ str(inc_a * scale / bianca_rect.area))
# # = 254.31

