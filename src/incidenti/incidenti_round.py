
import geopandas as gp
from shapely.geometry import mapping
import numpy as np

incidenti = gp.read_file("dataset/incidenti/inc_strad_milano_2016.geojson")

df = {}
for point in incidenti['geometry']: 
    # Le coordinate sono arrotondate a cinque punti decimali
    point = mapping(point)
    rounded_x, rounded_y = np.round(np.array(point['coordinates']),5)

    # Le coordinate sono aggiunte al dizionario
    if (rounded_x, rounded_y) in df.keys(): 
        df[(rounded_x, rounded_y)] += 1
    else: 
        df[(rounded_x, rounded_y)] = 1

rounded = gp.GeoDataFrame(df.values(), geometry=gp.points_from_xy([i[0] for i in df.keys()], [i[1] for i in df.keys()]))
# Il Dataframe è stato salvato nella cartella dataset
