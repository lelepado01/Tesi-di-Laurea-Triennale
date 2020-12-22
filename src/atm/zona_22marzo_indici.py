
import geopandas as gp
from shapely import geometry

scale = pow(10, 6)
bounds = [1.020 * scale, 1.025 * scale, 5.690 * scale, 5.696 * scale]

path_incidenti = "dataset/incidenti/inc_strad_milano_2016.geojson"
incidenti = gp.read_file(path_incidenti).to_crs(epsg=3857)

data = gp.read_file("dataset/zone_milano/zone.geojson").to_crs(epsg=3857)

bianca = data[data['name'] == "Bianca Maria"]['geometry'].iloc[0]
premuda = data[data['name'] == "Premuda"]['geometry'].iloc[0]

bianca_rect = geometry.Polygon(bianca)
premuda_rect = geometry.Polygon(premuda)

inc_a = 0
inc_s = 0
for point in incidenti['geometry']: 
    point = geometry.Point(point)

    if bianca_rect.contains(point): 
        inc_a += 1
    
    if premuda_rect.contains(point): 
        inc_s += 1

print("Incidenti su linea autobus: " + str(inc_s * scale / premuda_rect.area))
# = 93.96
print("Incidenti su strada senza linea: "+ str(inc_a * scale / bianca_rect.area))
# = 254.31