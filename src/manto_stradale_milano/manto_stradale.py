
# File usato per controllare se nei vari layer esistessero info 
# su pave (file di geoportale comune di milano) 

import geopandas as gp
import matplotlib.pyplot as plt
import contextily as cx


# data = gp.read_file("dataset/manto_stradale_milano/L010105.Shx").to_crs(epsg=3857)

incidenti = gp.read_file("dataset/incidenti/inc_strad_milano_2016.geojson").to_crs(epsg=3857)

# print(data.columns)

# data = data[data['ID_ZRIL'] == 'MI_2012_0922']

# ax = data.plot(figsize=(11,9))
ax2 = incidenti.plot(alpha=0.1, figsize=(11,9))
cx.add_basemap(ax=ax2)
plt.show()

# A010101 Area di circolazione veicolare, 
# A010102 Area di circolazione pedonale, 
# A010103 Area di circolazione ciclabile, 
# A010104 Area stradale, 
# A010105 Viabilità mista secondaria, 
# L010105 Viabilità mista secondaria, 
# L010107 Elemento stradale, 
# L010202 Elemento ferroviario, 
# L010204 Elemento tranviario, 
# L010206 Elemento di metropolitana, 
# L010210 Binario industriale, 
# P010108 Giunzione stradale, 
# P010203 Giunzione ferroviaria, 
# P010205 Giunzione tranviaria, 
# P010207 Giunzione di metropolitana, 
# LIM010102 Contorno area di circolazione pedonale, 
# LIM010103 Contorno area di circolazione ciclabile, 
# LIM010104 Contorno area stradale, 
# LIM010105 Contorno viabilità mista secondaria. 

# ID_ZRIL = identificatore univoco del territorio
