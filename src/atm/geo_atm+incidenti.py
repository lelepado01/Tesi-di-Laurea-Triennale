
import geopandas as gp
import matplotlib.pyplot as plt
import contextily as cx
import pandas as pd
import sys

sys.path.append("tesi/Tesi/src/")

import utils

path = "tesi/Tesi/dataset/atm/atm_percorsi.geojson"

percorsi_atm = gp.read_file(path).to_crs(epsg=3857)
#print(percorsi_atm)

# MAPPA 1
#layer_percorsi = percorsi_atm.plot(color="red", figsize=(11,9))
#cx.add_basemap(ax=layer_percorsi)
#plt.show()

# facendo cosi, la zona del centro diventa molto piccola perchè do importanza alla periferia 
# (senza linee atm)

# Ho provato a eliminare le linee troppo esterne 

#print(percorsi_atm['geometry'])
#print(type(percorsi_atm['geometry'][0]))

# non ho trovato funzioni / librerie per fare parse di geojson, 
# creo funzioni in file 'utils.py'

#lista_coords = parse_geojson_linestring(percorsi_atm['geometry'][0])
#print(lista_coords)

# Ho tutti i punti della linea atm, ora posso rimuovere le linee del dataset che 
# vanno troppo in periferia 
# guardando la MAPPA 1, voglio togliere le linee che vanno 'sopra' 5.715 * 10^6 
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

#print(len(percorsi_atm))
#print(percorsi_atm[series_from_geodataframe(percorsi_atm['geometry'])])

percorsi_ridotti = percorsi_atm[utils.remove_lines_out_of_range(
    percorsi_atm['geometry'],
    [UPPER_BOUND, LOWER_BOUND, LEFT_BOUND, RIGHT_BOUND]
    )]

# la mappa che ottengo è più 'zoommata'

# MAPPA 2
#layer_percorsi_ridotti = percorsi_ridotti.plot(color="red", figsize=(11,9))
#cx.add_basemap(ax=layer_percorsi_ridotti)
#plt.show()

# ora posso aggiungere il traffico

path_incidenti = "tesi/Tesi/dataset/incidenti/inc_strad_milano_2016.geojson"
incidenti = gp.read_file(path_incidenti).to_crs(epsg=3857)

# MAPPA 3
layer_percorsi_ridotti = percorsi_ridotti.plot(color="red", figsize=(11,9), alpha=0.5)
layer_incidenti = incidenti.plot(ax=layer_percorsi_ridotti, alpha=0.1)
cx.add_basemap(ax=layer_incidenti)
plt.show()

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