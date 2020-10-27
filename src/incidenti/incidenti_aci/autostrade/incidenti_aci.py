
import pandas as pd
import matplotlib.pyplot as plt

# I dati sulle autostrade hanno anche mese, ora e giorno della settimana, 
# con la posizione in quale autostrada

data_autostrade = pd.read_csv("dataset/incidenti/aci/autostrade/localizzazione_2018.csv")

aut = data_autostrade['NOME STRADA'].value_counts().sort_values(ascending=False).head(20)
#print(data_autostrade['NOME STRADA'].value_counts().sort_values(ascending=False).head(20))

import geopandas as gp
import contextily as cx

autostrade = gp.read_file("dataset/autostrade/autostrade.geojson").to_crs(epsg=3857)
#print(aut)

df = pd.merge(autostrade, aut, left_on='name', right_on=aut.index)
#print(df[['name', 'geometry']])

ax = df.plot(figsize=(11,9), column='NOME STRADA')
plt.ylim((4.5 * pow(10, 6), 6.1 * pow(10, 6)))
plt.xlim(left=0.55 * pow(10,6))
cx.add_basemap(ax=ax, source=cx.providers.CartoDB.Voyager)
plt.show()