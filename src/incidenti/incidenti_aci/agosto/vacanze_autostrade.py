
import pandas as pd
import matplotlib.pyplot as plt
import sys
sys.path.append('src')
import aci_utils

path = "dataset/incidenti/aci/autostrade/mesi_"

s = 0
index = 1
for year in range(2011, 2019): 
    agosto_2018 = pd.read_csv(path + str(year)+".csv")
    agosto_2018 = agosto_2018[['NOME STRADA', 'Agosto']]
    agosto_2018 = aci_utils.sum_field_by_column(agosto_2018, 'NOME STRADA', 'Agosto')
    agosto_2018 = agosto_2018.sort_values(by='val', ascending=False).head(5)
    #print(agosto_2018)
    s += agosto_2018['val'].iloc[0]
    plt.subplot(8,1,index)
    plt.title(str(year), loc='right', y=0.5)
    index += 1
    plt.barh(agosto_2018.index, agosto_2018['val'])
    #plt.tight_layout()
    

#print(s / 8)
plt.show()

