
import geopandas as gp
import sys

sys.path.append("src/")
import map_utils

path = "dataset/atm/atm_percorsi.geojson"
percorsi_atm = gp.read_file(path).to_crs(epsg=3857)

path = "dataset/incidenti/inc_strad_milano_2016.geojson"
incidenti = gp.read_file(path).to_crs(epsg=3857)

scale = pow(10, 6) 
bounds = [1.020 * scale, 1.025 * scale, 5.691 * scale, 5.695 * scale]
mappa = map_utils.CustomMap(bounds=bounds)
mappa.add_layer(incidenti)
mappa.add_layer(percorsi_atm, alpha=0.5, color = "orange")
mappa.set_label("Linee Autobus e Incidenti")
mappa.draw() 

# ##########################################
# Creazione di un rettangolo su zona navigli 
# from shapely import geometry
#
# rect = geometry.Polygon([
#     geometry.Point(1.020 * scale, 5.695 * scale), 
#     geometry.Point(1.025 * scale, 5.695 * scale), 
#     geometry.Point(1.025 * scale, 5.691 * scale), 
#     geometry.Point(1.020 * scale, 5.691 * scale), 
# ])

# inc = 0
# for point in incidenti['geometry']: 
#     point = geometry.Point(point)
#     if rect.contains(point):
#         inc += 1

# Numero di incidenti per area in zona Navigli
#print("Incidenti per km in zona: " + str(inc * 1000000 / rect.area))# = 59.25 incidenti/km