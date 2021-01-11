
import geopandas as gp
import pandas as pd
import matplotlib.pyplot as plt
import sys
sys.path.append("src")
import aci_utils

field_incidenti = 'TOTALE'

path = "dataset/regioni/regioni.geojson"
regioni = gp.read_file(path)

data = pd.read_csv('dataset/incidenti/aci/autostrade/mesi_2018.csv') 
data = data[data['TOTALE'] != '0,0'].astype({'TOTALE': int})

incidenti = aci_utils.get_sum_of_fields(data, 'REGIONE', field_incidenti)

incidenti.index = incidenti['REGIONE']
regioni.index = regioni['reg_name']

regioni = gp.GeoDataFrame(incidenti[field_incidenti], geometry=regioni['geometry'].transpose())

from matplotlib.lines import Line2D

regioni.plot(column=field_incidenti, cmap='OrRd', legend=True)
plt.axis('off')
plt.legend([
    Line2D([],[],color='#a52317',linewidth=5), 
    Line2D([],[],color='#d6584d',linewidth=5), 
    Line2D([],[],color='#f7aca5',linewidth=5)
], [max(regioni[field_incidenti]), int(regioni[field_incidenti].mean()), min(regioni[field_incidenti])])
plt.show()