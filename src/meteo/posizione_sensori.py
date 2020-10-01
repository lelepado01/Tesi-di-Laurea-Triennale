
import matplotlib.pyplot as plt
import geopandas as gp 
import contextily as cx
import pandas as pd

#path = "dataset/meteo/tipologia_sensori.csv"
path = "dataset/meteo/tipologia_sensori.geojson"

sensori = gp.read_file(path).to_crs(epsg=3857)
print(sensori)

#geodf = gp.GeoDataFrame(data, geometry=gp.points_from_xy(data['lat'], data['lng'])).set_crs(epsg=4326).to_crs(epsg=3857)
#print(geodf.columns)
#print(geodf)

#sensori = geodf[['IdSensore', 'Tipologia', 'Unità_DiMisura', 'IdStazione','NomeStazione', 'Quota', 'Provincia','UTM_Nord', 'UTM_Est', 'geometry']]
#print(sensori)

#print(sensori['geometry'].unique())

layer_sensori = sensori.plot(figsize=(11,9), color="blue")
cx.add_basemap(ax=layer_sensori)
plt.show()