

import geopandas as gp
import sys
sys.path.append("src/")
import geo_utils

path = "dataset/atm/atm_percorsi.geojson"

percorsi_atm = gp.read_file(path).to_crs(epsg=3857)

scale = pow(10, 6)
UPPER_BOUND = 5.708 * scale
LOWER_BOUND = 5.683 * scale
LEFT_BOUND = 1.007 * scale
RIGHT_BOUND = 1.036 * scale

percorsi_ridotti = percorsi_atm[geo_utils.remove_lines_out_of_range(
    percorsi_atm['geometry'],
    [UPPER_BOUND, LOWER_BOUND, LEFT_BOUND, RIGHT_BOUND]
    )]

path_incidenti = "dataset/incidenti/inc_strad_milano_2016.geojson"
incidenti = gp.read_file(path_incidenti).to_crs(epsg=3857)


import map_utils

scale = pow(10, 6)
bounds = [1.024 * scale, 1.028 * scale, 5.693 * scale, 5.697 * scale]
mappa = map_utils.CustomMap(bounds=bounds)
mappa.add_layer(incidenti)
mappa.add_layer(percorsi_ridotti, alpha=0.5, color = "orange")
mappa.set_label("Linee Autobus e Incidenti")
mappa.draw()