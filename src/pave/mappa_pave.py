
import geopandas as gp
import matplotlib.pyplot as plt
import contextily as cx

pave = gp.read_file("dataset/pave/pave.geojson").to_crs(epsg=3857)

incidenti = gp.read_file("dataset/incidenti/inc_strad_milano_2016.geojson").to_crs(epsg=3857)

# ax = pave.plot(figsize=(11,9), alpha=0.7)
# cx.add_basemap(ax=ax)
# plt.show()

from shapely import geometry

inc_in_pave = 0
for rect in pave['geometry']: 
    rect = geometry.Polygon(rect)

    for point in incidenti['geometry']: 
        if rect.contains(geometry.Point(point)): 
            inc_in_pave += 1

area_pave = 0
for rect in pave['geometry']: 
    area_pave += geometry.Polygon(rect).area

print(area_pave)

#print(inc_in_pave * 10**6 / area_pave) # = 229.45

# Sembra un numero alto, ma bisognerebbe avere un campione di strade normali per vedere se il numero di incidenti è piu alto