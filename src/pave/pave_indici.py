
from shapely import geometry
import geopandas as gp

pave = gp.read_file("dataset/pave/pave.geojson").to_crs(epsg=3857)
incidenti = gp.read_file("dataset/incidenti/inc_strad_milano_2016.geojson").to_crs(epsg=3857)
asfalto = gp.read_file("dataset/pave/asfalto.geojson").to_crs(epsg=3857)

# Conteggio incidenti all'interno della figura (per ogni figura) raffigurante pavé
inc_in_pave = 0
for rect in pave['geometry']: 
    rect = geometry.Polygon(rect)

    for point in incidenti['geometry']: 
        if rect.contains(geometry.Point(point)): 
            inc_in_pave += 1

area_pave = 0
for rect in pave['geometry']: 
    area_pave += geometry.Polygon(rect).area

print(inc_in_pave * 10**6 / area_pave) 
# = 229.45 incidenti per km^2

area = 0
for shape in asfalto['geometry']: 
    area += geometry.Polygon(shape).area

incidenti = gp.read_file("dataset/incidenti/inc_strad_milano_2016.geojson").to_crs(epsg=3857)

# Conteggio incidenti all'interno della figura (per ogni figura) raffigurante asfalto
inc = 0
for shape in asfalto['geometry']: 
    shape = geometry.Polygon(shape)

    for point in incidenti['geometry']: 
        if shape.contains(geometry.Point(point)): 
            inc += 1

print(inc * 10**6/ area)
# = 220.89 incidenti per km^2
