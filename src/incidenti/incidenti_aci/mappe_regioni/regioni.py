
# Voglio realizzare mappe italia per regione
# https://geojson-maps.ash.ms/
# Download del file geojson con dati della regione

import geopandas as gp
import matplotlib.pyplot as plt

path = "dataset/regioni/regioni.geojson"

regioni = gp.read_file(path)

print(regioni)

regioni.plot()
plt.show()