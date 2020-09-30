
import matplotlib.pyplot as plt
import geopandas as gp
import contextily as cx

path = "/Users/gabrielepadovani/Desktop/Università/Data/tesi/Tesi/dataset/ciclabili/bike_ciclabili.shp"

# to_crs(...) è per fare in modo che la mappa sia in proiezione di Mercatore
# se non lo metto la mappa diventa 'obliqua'

data = gp.read_file(path).to_crs(epsg=3857) 
#print(data)

ax = data.plot(color="red", figsize=(11,9))
cx.add_basemap(ax, crs=data.crs.to_string())
plt.show()