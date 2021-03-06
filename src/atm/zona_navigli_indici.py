

import geopandas as gp
from shapely import geometry

scale = pow(10, 6)
bounds = [1.020 * scale, 1.025 * scale, 5.690 * scale, 5.696 * scale]

path_incidenti = "dataset/incidenti/inc_strad_milano_2016.geojson"
incidenti = gp.read_file(path_incidenti).to_crs(epsg=3857)

data = gp.read_file("dataset/zone_milano/zone.geojson").to_crs(epsg=3857)

autobus = data[data['name'] == "Navigli Autobus"]
street = data[data['name'] == "Navigli Incidenti"]

autobus_rect = geometry.Polygon(autobus['geometry'].iloc[0])
street_rect = geometry.Polygon(street['geometry'].iloc[0])

inc_a = 0
inc_s = 0
for point in incidenti['geometry']: 
    point = geometry.Point(point)

    if autobus_rect.contains(point): 
        inc_a += 1
    
    if street_rect.contains(point): 
        inc_s += 1

print("Incidenti su linea autobus: " + str(inc_a * scale / autobus_rect.area))
# = 167.09 incidenti per km^2
print("Incidenti su strada senza linea: " + str(inc_s * scale / street_rect.area))
# = 289.32 incidenti per km^2

