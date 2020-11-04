
import geopandas as gp
import pandas as pd
import matplotlib.pyplot as plt

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

field_incidenti = 'Agosto'
path = "dataset/regioni/regioni.geojson"
regioni = gp.read_file(path)

data = pd.read_csv('dataset/incidenti/aci/autostrade/mesi_2012.csv')
data = data[data['TOTALE'] != '0,0'].astype({'TOTALE': int})

incidenti = get_sum_of_fields(data, 'REGIONE', field_incidenti)

incidenti.index = incidenti['REGIONE']
regioni.index = regioni['reg_name']
print(incidenti)
# print(regioni)

regioni = gp.GeoDataFrame(incidenti[field_incidenti], geometry=regioni['geometry'].transpose())

from matplotlib.lines import Line2D

regioni.plot(column=field_incidenti, cmap='OrRd', legend=True)
# plt.title("Incidenti per regione nel 2014")
plt.axis('off')
plt.legend([
    Line2D([],[],color='#a52317',linewidth=5), 
    Line2D([],[],color='#d6584d',linewidth=5), 
    Line2D([],[],color='#f7aca5',linewidth=5)
], [max(regioni[field_incidenti]), '1000', min(regioni[field_incidenti])])
plt.show()

# agosto = get_sum_of_fields(data, 'REGIONE', 'Agosto')
# gennaio = get_sum_of_fields(data, 'REGIONE', 'Gennaio')

# agosto.index = agosto['REGIONE']
# gennaio.index = gennaio['REGIONE']
# agosto = agosto['Agosto']
# gennaio = gennaio['Gennaio']

# red_ls = ['#d693a3']*20
# red_ls[3:8] = ['#f65578']*6
# red_ls[5] = '#d693a3'
# red_ls[10] = '#f65578'
# red_ls[14] = '#f65578'

# blue_ls = ['#95c6d8']*20
# blue_ls[3:8] = ['#70b8ff']*6
# blue_ls[5] = '#95c6d8'
# blue_ls[10] = '#70b8ff'
# blue_ls[14] = '#70b8ff'

# plt.bar(agosto.index, agosto, label='Agosto',  color=red_ls)
# plt.bar(gennaio.index, gennaio, label='Gennaio', alpha=0.9, color=blue_ls)
# plt.xticks(rotation=90)
# plt.ylabel("Incidenti al mese (2014)")
# plt.legend()
# plt.tight_layout()
# plt.show()