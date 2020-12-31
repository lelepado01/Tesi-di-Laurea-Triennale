import geopandas as gp
import matplotlib.pyplot as plt
import contextily as cx
import sys
sys.path.append("src/")
import geo_utils

path = "dataset/atm/atm_percorsi.geojson"
percorsi_atm = gp.read_file(path).to_crs(epsg=3857)

# path_incidenti = "dataset/incidenti/inc_strad_milano_2016.geojson"
# incidenti = gp.read_file(path_incidenti).to_crs(epsg=3857)

scale = pow(10, 6)
UPPER_BOUND = 5.708 * scale
LOWER_BOUND = 5.683 * scale
LEFT_BOUND = 1.007 * scale
RIGHT_BOUND = 1.036 * scale

percorsi_ridotti = percorsi_atm[geo_utils.remove_lines_out_of_range(
    percorsi_atm['geometry'],
    [UPPER_BOUND, LOWER_BOUND, LEFT_BOUND, RIGHT_BOUND]
    )]

# fig, (ax1, ax2) = plt.subplots(ncols=2, sharex=True, sharey=True)
# ax1.axis('off')
layer_m = percorsi_ridotti.plot(figsize=(11,9) ,alpha=0.7, color='red', linewidth=0.5)
cx.add_basemap(ax=layer_m)
# inc_layer = incidenti.plot(ax=ax2, alpha=0.02)
# cx.add_basemap(ax=inc_layer)
plt.axis('off')
plt.show()