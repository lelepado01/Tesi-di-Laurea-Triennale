
import pandas as pd
import matplotlib.pyplot as plt
import sys
sys.path.append('src')
import aci_utils

path = "dataset/incidenti/aci/autostrade/mesi_"

agosto = pd.DataFrame()

for year in range(2011, 2012):
    data = pd.read_csv(path + str(year) + ".csv")
    data['Anno'] = [year] * len(data)
    agosto = agosto.append(data[['NOME STRADA', 'Anno', 'Agosto']])


#print(aci_utils.two_cols_unique(data[['NOME STRADA', 'Anno']]))

    #agosto = aci_utils.sum_field_by_two_columns(agosto, 'NOME STRADA', 'Anno', 'Agosto')
    #agosto = agosto[aci_utils.filter_by_value(agosto['NOME STRADA_Anno'], str(year))]
    #agosto = agosto.sort_values(by='Value', ascending=False).head(5)
#
    #plt.barh(agosto['Nome e Anno'].astype(str), agosto['Inc'])
    #plt.xticks(rotation=90)
    #plt.tight_layout()
    #plt.show()

s = 0
index = 1
for year in range(2011, 2019): 
    agosto_2018 = pd.read_csv(path + str(year)+".csv")
    agosto_2018 = agosto_2018[['NOME STRADA', 'Agosto']]
    agosto_2018 = aci_utils.sum_field_by_column(agosto_2018, 'NOME STRADA', 'Agosto')
    agosto_2018 = agosto_2018.sort_values(by='val', ascending=False).head(1)
    #print(agosto_2018)
    s += agosto_2018['val'].iloc[0]
    #plt.subplot(8,1,index)
    ##plt.title(str(year))
    #index += 1
    #plt.barh(agosto_2018.index, agosto_2018['val'])
    ##plt.tight_layout()
    #plt.legend("")
    

print(s / 8)
#plt.show()

