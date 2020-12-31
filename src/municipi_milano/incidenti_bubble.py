
import geopandas as gp
import matplotlib.pyplot as plt
import contextily as cx

incidenti = gp.read_file("dataset/incidenti/incidenti_round.csv")
incidenti = gp.GeoDataFrame(incidenti['field_3'], geometry=gp.points_from_xy(incidenti['field_2'], incidenti['field_1'])).set_crs(epsg=4326).to_crs(epsg=3857)
incidenti['field_3'] = incidenti['field_3'].astype(float)

ax = incidenti.plot(
    figsize=(9,7),
    alpha=0.8,
    column='field_3',
    markersize=incidenti['field_3'].astype(int) **1.8,
    cmap='viridis'
    )

cx.add_basemap(ax = ax)
plt.axis('off')
plt.show()