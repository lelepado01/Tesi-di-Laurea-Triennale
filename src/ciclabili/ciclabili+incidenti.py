
import geopandas as gp
import matplotlib.pyplot as plt
import contextily as cx

path_incidenti = "dataset/incidenti/inc_strad_milano_2016.geojson"
path_ciclabili = "dataset/ciclabili/bike_ciclabili.shp"

dati_incidenti = gp.read_file(path_incidenti).to_crs(epsg=3857)
dati_ciclabili  = gp.read_file(path_ciclabili).to_crs(epsg=3857)

# per fare overlap di due mappe, plot di M1 -> plot di M2 con ax=M1

layer_ciclabili = dati_ciclabili.plot(color="red", figsize=(11,9), alpha=0.5)
layer_incidenti = dati_incidenti.plot(ax=layer_ciclabili, color="blue", figsize=(11, 9), alpha=0.05)
cx.add_basemap(layer_incidenti)
plt.show()

# IMPORTANTE: il dataset delle piste ciclabili è del 2018 
# (non ho trovato notizie di nuove piste costruite tra 2016 e 2018)
# IMP: ci sono 2 nuove piste nel 2020 (35km e 23 km)

# ci sono riscontri su alcune piste ciclabili: 
#   viale sempione       (ma non ho trovato la pista ciclabile, non è segnata?)
#   incrovcio tra viale marche e via zara (in particolare viale marche)
#   via  melchiorre Gioia
#   Piazzale Loreto
#   viale Tunisia
#   Bastioni di porta Venezia
#   piazza della repubblica
#   via Olona

# Altre ciclabili hanno alta concentrazione di incidenti: 
#   viale romagna (anche qui non ho trovato la ciclabile)
#   viale famagosta
#   viale lodovico il moro
# la maggior parte di queste ho notato essere in periferia