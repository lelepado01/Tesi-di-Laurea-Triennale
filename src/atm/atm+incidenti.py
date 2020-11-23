
import geopandas as gp
import matplotlib.pyplot as plt
import contextily as cx
import pandas as pd
import sys

sys.path.append("src/")

import geo_utils

path = "dataset/atm/atm_percorsi.geojson"

percorsi_atm = gp.read_file(path).to_crs(epsg=3857)
#print(percorsi_atm)

# Ho tutti i punti della linea atm, ora posso rimuovere le linee del dataset che 
# vanno troppo in periferia 
# voglio togliere le linee che vanno 'sopra' 5.715 * 10^6 
# e quelle che vanno 'sotto' 5.68 * 10^6 
scale = pow(10, 6)
UPPER_BOUND = 5.708 * scale
LOWER_BOUND = 5.683 * scale
LEFT_BOUND = 1.007 * scale
RIGHT_BOUND = 1.036 * scale

# 'remove_lines_out_of_range()' esegue per ogni linea del dataframe la funzione precedente, 
# e aggiunge il risultato a una lista 
# al termine dell'esecuzione converto la lista in pandas.Series in modo da poter 
# fare il filtraggio delle linee che fuoriescono dal range 

percorsi_ridotti = percorsi_atm[geo_utils.remove_lines_out_of_range(
    percorsi_atm['geometry'],
    [UPPER_BOUND, LOWER_BOUND, LEFT_BOUND, RIGHT_BOUND]
    )]

path_incidenti = "dataset/incidenti/inc_strad_milano_2016.geojson"
incidenti = gp.read_file(path_incidenti).to_crs(epsg=3857)

# volendo potrei ridurre ancora il range dei percorsi, visto che ci sono molte linee atm 
# che non si sovrappongono a strade con molti incidenti 

# Ho ridotto i range UP e DOWN e ho introdotto range LEFT e RIGHT
#print(len(percorsi_ridotti))
# Rimangono 291 linee rispetto alle 393 iniziali

# Ho trovato tre zone 
#   Navigli: 
#       viale col di lana       (con tram)
#       viale bligny            (con tram)
#       viale coni zugna        ('')
#       viale gorizia           ('')
# Una cosa che ho notato è che queste sono tutte delle vie parallele a 
#       viale Papiniano (molto trafficato) 
#       viale gabriele d'annunzio
#       viale gian galeazzo
#       viale beatrice d'este
# 
#   Zona 2:                     Tutti anche tram
#       viale premuda
#       viale corsica
#       viale 22 marzo
# 
# Anche in questo caso, viale premuda è una parallela di un'altro viale trafficato, 
#       viale bianca maria 
# 
#   Zona Monumentale: 
#       viale farini            (con tram) -> è anche una via trafficata
#       viale stelvio 
# 
# Inoltre a saltare all'occhio è anche piazzale Loreto, che è intersezione di tre linee

# import map_utils

# scale = pow(10, 6)
# # Navigli
# bounds = [1.020 * scale, 1.025 * scale, 5.691 * scale, 5.695 * scale]
# mappa = map_utils.CustomMap(bounds=bounds)
# mappa.add_layer(incidenti)
# mappa.add_layer(percorsi_ridotti, alpha=0.5, color = "orange")
# mappa.set_label("Linee Autobus e Incidenti")
# #mappa.draw() 

# bounds = [1.025 * scale, 1.027 * scale, 5.697 * scale, 5.700 * scale]
# mappa.set_bounds(bounds)
# mappa.draw()