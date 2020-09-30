
# Ho trovato un dataset di incidenti creato da un giornale di milano, ma ha solo 
# il nome della via degli incidenti, preferisco usare i dati istat che hanno anche 
# la data precisa

import geopandas as gp
import matplotlib.pyplot as plt
import contextily as cx

path_1 = "dataset/incidenti_geojson/v_11_3_parte_1.geojson"

parte_1 = gp.read_file(path_1)#.to_crs(epsg=3857)

print(parte_1['Name'].value_counts())

#l = parte_1.plot(figsize=(11,9))
#cx.add_basemap(ax=l)
#plt.show()