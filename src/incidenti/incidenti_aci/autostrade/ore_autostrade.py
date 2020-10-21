
import pandas as pd
import matplotlib.pyplot as plt

def sum_columns(data : pd.DataFrame, normalize = False, name=None) -> pd.Series: 
    res = {}
    for col in data.columns: 
        res[col] = sum(data[col])

    if name is None:
        res = pd.Series(res).transpose()
    else: 
        res = pd.Series(res, name=name)

    if normalize: 
        res = res / sum(res)

    return res


data = pd.read_csv('dataset/incidenti/aci/autostrade/ore_2012.csv')
ore = ['01','02','03','04','05','06','07','08','09','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24']
#ore_2012 = data
#print(ore_2012.columns)
#ore = sum_columns(ore_2012[ore])
#ore.plot.bar()
#plt.show()

# Conferma i risultati istat

#print(len(data[data['PROVINCIA'] == 'Milano']['NOME STRADA'].unique()))
milano = data[data['PROVINCIA'] == 'Milano']

incidenti = pd.DataFrame()

for field in milano['NOME STRADA'].unique(): 
    incidenti = incidenti.append(
        sum_columns(milano[milano['NOME STRADA'] == field][ore], name=field), 
    )

#print(incidenti)
#incidenti.transpose().plot()
#plt.legend("")
#plt.show()

import geopandas as gp
import contextily as cx

strade = gp.read_file("dataset/incidenti/aci/autostrade/posizione_autostrade.geojson").to_crs(epsg=3857)
strade.index = strade['name']
#print(len(strade))

strade = gp.GeoDataFrame(incidenti['18'], geometry=strade['geometry'])
#print(strade)

ax = strade.plot(figsize=(11,9), markersize=strade['18'] * 100, alpha=0.5, color='orange')
plt.ylim((5.68 * pow(10, 6), 5.72 * pow(10,6)))
cx.add_basemap(ax=ax)
plt.show()