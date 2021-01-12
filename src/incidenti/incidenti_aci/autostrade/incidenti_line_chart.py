
import pandas as pd
import matplotlib.pyplot as plt
import geopandas as gp
import contextily as cx
import sys 
sys.path.append("src")
import aci_utils

ore = ['01','02','03','04','05','06','07','08','09','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24']

data = pd.read_csv('dataset/incidenti/aci/autostrade/ore_2018.csv')
milano = data[data['PROVINCIA'] == 'Milano']

strade = gp.read_file("dataset/autostrade/autostrade_milano_linee.geojson").to_crs(epsg=3857)
strade.index = strade['name']

incidenti = pd.DataFrame()
for field in milano['NOME STRADA'].unique(): 
    incidenti = incidenti.append(
        aci_utils.sum_columns(milano[milano['NOME STRADA'] == field][ore], name=field), 
    )

# Conteggio incidenti per totali, indipendentemente dall'orario
inc = 0
for i in ore:
    inc = incidenti[i] + inc

strade = gp.GeoDataFrame(inc, geometry=strade['geometry'])

ax = strade.plot(figsize=(11,9), column= 0, cmap='hot_r' ,legend=True, linewidth=1.8)
plt.ylim((5.68 * pow(10, 6), 5.72 * pow(10,6)))
plt.xlim((pow(10, 6), 1.04 * pow(10,6)))
plt.axis('off')
cx.add_basemap(ax=ax)
plt.show()

