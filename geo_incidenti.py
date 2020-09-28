
import geopandas as gpd

path = "/Users/gabrielepadovani/Desktop/Università/Data/tesi/Tesi/dataset/incidenti/inc_strad_milano_2016.geojson"

file = gpd.read_file(path)
print(file)