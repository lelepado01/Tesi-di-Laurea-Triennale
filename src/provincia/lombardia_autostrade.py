
import geopandas as gp
import pandas as pd
import matplotlib.pyplot as plt
import sys
sys.path.append("src")
import aci_utils

# Selezione regione lombardia (codice 3)
data = gp.read_file("dataset/regioni/provincia.geojson").to_crs(epsg=3857)
lombardia = data[data['reg_istat_code_num'] == 3]

incidenti = pd.read_csv("dataset/incidenti/aci/autostrade/comuni_2018.csv")
incidenti_lombardia = incidenti[incidenti['REGIONE'] == 'Lombardia']

incidenti_lombardia = gp.GeoDataFrame(aci_utils.get_sum_of_fields(incidenti_lombardia, 'PROVINCIA', 'INC'))

incidenti_lombardia = lombardia.merge(incidenti_lombardia, left_on='prov_name', right_on='PROVINCIA')

from matplotlib.lines import Line2D

incidenti_lombardia.plot(column='INC', cmap='OrRd')
plt.legend([
    Line2D([],[],color='#84190f',linewidth=5), 
    Line2D([],[],color='#ef5547',linewidth=5), 
    Line2D([],[],color='#efd4ae',linewidth=5)
], [max(incidenti_lombardia['INC']), int(incidenti_lombardia['INC'].mean()), min(incidenti_lombardia['INC'])])
plt.axis('off')
plt.show()