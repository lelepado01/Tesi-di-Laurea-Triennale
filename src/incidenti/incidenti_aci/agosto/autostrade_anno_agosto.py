
import pandas as pd
import matplotlib.pyplot as plt
import sys
sys.path.append('src')
import aci_utils

path = "dataset/incidenti/aci/autostrade/mesi_"

# Per ogni annata sono calcolate le strade con più incidenti
agosto = pd.DataFrame()
for year in range(2011, 2019):
    print("Processing: " + str(year))
    data = pd.read_csv(path + str(year) + ".csv")
    data['Anno'] = [year] * len(data)
    agosto_temp = pd.DataFrame()
    agosto_temp = agosto_temp.append(data[['NOME STRADA', 'Anno', 'Agosto']])

    agosto_temp = aci_utils.sum_field_by_two_columns(agosto_temp, 'NOME STRADA', 'Anno', 'Agosto')
    agosto_temp = agosto_temp[aci_utils.filter_by_value(agosto_temp['NOME STRADA_Anno'], str(year))]
    agosto_temp = agosto_temp.sort_values(by='Value', ascending=False)

    agosto = agosto.append(agosto_temp)

# Le strade sono ordinate in ordine ascendente e sono prese le ultime 15 (con più incidenti)
agosto = agosto.sort_values(by='Value', ascending=True).tail(15)

# Colorazione del grafo 'a mano'
color_ls = ['#79ceb6'] * 15
color_ls[11] = '#7991ce'
color_ls[7] = '#7991ce'
color_ls[4] = '#7991ce'
color_ls[3] = '#7991ce'
color_ls[2] = '#7991ce'
color_ls[8] = '#ce7991'
color_ls[1] = '#ceb679'


plt.barh(agosto['NOME STRADA_Anno'].astype(str), agosto['Value'], color=color_ls)
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()