
import geopandas as gp
import pandas as pd
import matplotlib.pyplot as plt
import sys
sys.path.append("src")
import aci_utils

# Selezione degli incidenti in regione lazio (codice 12)
data = gp.read_file("dataset/regioni/provincia.geojson").to_crs(epsg=3857)
lombardia = data[data['reg_istat_code_num'] == 12]

incidenti = pd.read_csv("dataset/incidenti/aci/strade_provinciali/aci_2018.csv")
incidenti_lombardia = incidenti[incidenti['REGIONE'] == 'Lazio']
incidenti_lombardia = gp.GeoDataFrame(aci_utils.get_sum_of_fields(incidenti_lombardia, 'provincia', 'Inc'))
incidenti_lombardia = lombardia.merge(incidenti_lombardia, left_on='prov_name', right_on='provincia') 

from matplotlib.lines import Line2D

inc = 'Inc'

incidenti_lombardia.plot(column=inc, cmap='OrRd')
plt.legend([
    Line2D([],[],color='#84190f',linewidth=5), 
    Line2D([],[],color='#ef5547',linewidth=5), 
    Line2D([],[],color='#efd4ae',linewidth=5)
], [max(incidenti_lombardia[inc]), int(incidenti_lombardia[inc].mean()), min(incidenti_lombardia[inc])])
plt.axis('off')
plt.show()