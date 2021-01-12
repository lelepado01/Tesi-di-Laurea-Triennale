
import pandas as pd

data = pd.read_csv("dataset/incidenti/aci/autostrade/comuni_2018.csv")
fields = ['INC', 'FER', 'MOR']

def sum_field_by_column(data, select, field_to_sum1, field_to_sum2, field_to_sum3): 
    dic = {}
    for f in data[select].unique(): 
        dic[f] = [
            data[data[select] == f][field_to_sum1].sum(), 
            data[data[select] == f][field_to_sum2].sum(),
            data[data[select] == f][field_to_sum3].sum()
            ]

    return pd.DataFrame(dic, index=fields)

provincia = sum_field_by_column(data, 'PROVINCIA', fields[0], fields[1], fields[2]).transpose()
print("INC e FER tra province: ", end="")
print(provincia['FER'].corr(provincia['INC']))# = 0.9964
print("INC e MOR tra province: ", end="")
print(provincia['MOR'].corr(provincia['INC']))# = 0.7941
print("MOR e FER tra province: ", end="")
print(provincia['MOR'].corr(provincia['FER']))# = 0.8058

inc = data['INC']
fer = data['FER']
mor = data['MOR']

print("INC e FER: ", end="")
print(inc.corr(fer))# = 0.9836
print("INC e MOR: ", end="")
print(inc.corr(mor))# = 0.3385
print("MOR e FER: ", end="")
print(fer.corr(mor))# = 0.3355