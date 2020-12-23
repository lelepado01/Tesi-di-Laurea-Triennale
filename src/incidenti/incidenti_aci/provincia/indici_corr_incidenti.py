
import pandas as pd

data = pd.read_csv("dataset/incidenti/aci/autostrade/comuni_2018.csv")

fields = ['INC', 'FER']

def sum_field_by_column(data, select, field_to_sum1, field_to_sum2): 
    dic = {}
    for f in data[select].unique(): 
        dic[f] = [
            data[data[select] == f][field_to_sum1].sum(), 
            data[data[select] == f][field_to_sum2].sum()
            ]

    return pd.DataFrame(dic)

provincia = sum_field_by_column(data, 'PROVINCIA', fields[0], fields[1]).transpose()
print(provincia['MOR'].corr(provincia['INC']))# = 0.8204903971483627
print(provincia['FER'].corr(provincia['INC']))# = 0.9826611644228044
print(provincia['MOR'].corr(provincia['FER']))# = 0.8332572834970239

inc = data['INC']
fer = data['FER']
mor = data['MOR']

print(inc.corr(fer))
print(inc.corr(mor))
print(fer.corr(mor))