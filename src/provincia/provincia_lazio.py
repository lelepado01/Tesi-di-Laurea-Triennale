
import geopandas as gp
import pandas as pd
import matplotlib.pyplot as plt

data = gp.read_file("dataset/regioni/provincia.geojson").to_crs(epsg=3857)

lombardia = data[data['reg_istat_code_num'] == 12]
# lombardia.plot()
# plt.show()

#incidenti = pd.read_csv("dataset/incidenti/aci/autostrade/comuni_2018.csv")
incidenti = pd.read_csv("dataset/incidenti/aci/strade_provinciali/aci_2018.csv")
incidenti_lombardia = incidenti[incidenti['REGIONE'] == 'Lazio']

def get_sum_of_fields(data : pd.DataFrame, select_field : str, field_to_sum : str) -> pd.Series: 
    res = {}
    index = 0
    for reg in data[select_field].unique():
        res[index] = [reg, 0]
        index += 1

    index = 0
    for reg in data[select_field].unique():
        for row in data[data[select_field] == reg][field_to_sum]:
            res[index] = [res[index][0], res[index][1] + row]
        index += 1

    return pd.DataFrame(res, index=[select_field, field_to_sum]).transpose()


incidenti_lombardia = gp.GeoDataFrame(get_sum_of_fields(incidenti_lombardia, 'provincia', 'Inc'))
# incidenti_lombardia = gp.GeoDataFrame(get_sum_of_fields(incidenti_lombardia, 'PROVINCIA', 'INC'))

incidenti_lombardia = lombardia.merge(incidenti_lombardia, left_on='prov_name', right_on='provincia') 
# incidenti_lombardia = lombardia.merge(incidenti_lombardia, left_on='prov_name', right_on='PROVINCIA')

from matplotlib.lines import Line2D

# inc = 'INC'
inc = 'Inc'

incidenti_lombardia.plot(column=inc, cmap='OrRd')
plt.legend([
    Line2D([],[],color='#84190f',linewidth=5), 
    Line2D([],[],color='#ef5547',linewidth=5), 
    Line2D([],[],color='#efd4ae',linewidth=5)
], [max(incidenti_lombardia[inc]), int(incidenti_lombardia[inc].mean()), min(incidenti_lombardia[inc])])
plt.axis('off')
plt.show()