

import geopandas as gp
import contextily as cx
import matplotlib.pyplot as plt
from shapely import geometry

data = gp.read_file("dataset/milano_municipi/Municipi.shx").to_crs(epsg=3857)
incidenti = gp.read_file("dataset/incidenti/inc_strad_milano_2016.geojson").to_crs(epsg=3857)

base = 10**6 
up = 5.699 * base
down = 5.6976 * base
left = 1.0255 * base
right = 1.0265 * base

p1 = geometry.Point(left , up)
p2 = geometry.Point(right, up)
p3 = geometry.Point(left , down)
p4 = geometry.Point(right, down)

loreto = geometry.Polygon([p1, p2, p4, p3])

loreto_incidenti = 0
for point in incidenti['geometry']: 
    point = geometry.Point(point)

    if loreto.contains(point): 
        loreto_incidenti += 1

area_loreto = loreto.area * data['AREA'].iloc[0] / geometry.Polygon(data['geometry'].iloc[0]).area
area_loreto_inc = loreto_incidenti * 1000000 / area_loreto

# Numero di incidenti per km^2 in zona piazzale loreto
#print(area_loreto_inc)# = 231.06

# per avere una mappa di sfondo migliore rispetto a quella di default
providers = {}
def get_providers(provider):
    if "url" in provider:
        providers[provider['name']] = provider
    else:
        for prov in provider.values():
            get_providers(prov)
get_providers(cx.providers)

df = gp.GeoDataFrame(geometry=[loreto]).set_crs(epsg=3857)

ax = df.plot(alpha=0.4)
inc = incidenti.plot(ax = ax, alpha=0.0)
cx.add_basemap(ax=inc, source=providers['OpenStreetMap.Mapnik'])
plt.xlim((1.02 * base, 1.03 * base))
plt.ylim((5.692 * base, 5.702 * base))
plt.axis('off')
plt.show()