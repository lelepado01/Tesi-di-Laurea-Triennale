
import pandas as pd
import matplotlib.pyplot as plt
import geopandas as gpd
import contextily as cx

path = "dataset/incidenti/inc_strad_milano_2016.geojson"

# to_crs(...) è per fare in modo che la mappa sia in proiezione di Mercatore
# se non lo metto la mappa diventa 'obliqua'

data = gpd.read_file(path).to_crs(epsg=3857)
#print(type(data))
#world = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))
#print(gpd.datasets.available)

#ax = data.plot(figsize=(11,9), alpha=0.05)
#cx.add_basemap(ax, crs=data.crs.to_string())
#plt.savefig("geo_incidenti.png")

# Ci sono dei punti in cui avvengono molti incidenti "sovrapposti", sono errori nei dati o 
# sono punti con alta incidentalità?

incidenti_ripetuti = pd.Series(data['geometry'].astype(str)).value_counts()
#print(incidenti_ripetuti)

# Ci sono molti incidenti che avvengono alle stesse esatte coordinate, sono errori?

