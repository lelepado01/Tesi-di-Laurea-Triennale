
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("dataset/incidenti/aci/autostrade/comuni_2018.csv")

fields = ['INC', 'FER']

#print(len(data['PROVINCIA'].unique()))

# Il numero di feriti dipende dal numero di incidenti?
# E il numero di morti?

def sum_field_by_column(data, select, field_to_sum1, field_to_sum2): 
    dic = {}
    for f in data[select].unique(): 
        dic[f] = [
            data[data[select] == f][field_to_sum1].sum(), 
            data[data[select] == f][field_to_sum2].sum()
            ]

    return pd.DataFrame(dic)

provincia = sum_field_by_column(data, 'PROVINCIA', fields[0], fields[1]).transpose()
# Calcolo coeff. di correlazione
#print(provincia['FER'].corr(provincia['INC'])) = 0.9826611644228044
# Il coeff. di Pearson è molto vicino a 1, i due campioni sono strettamente correlati
#print(provincia['MOR'].corr(provincia['INC'])) = 0.8204903971483627
#print(provincia['MOR'].corr(provincia['FER'])) = 0.8332572834970239
# Correlazione più debole, ma comunque presente

provincia = provincia.sort_values(by=0).head(20).sort_index()
provincia[0].plot(label='Incidenti')
provincia[1].plot(label='Feriti')
plt.legend()
plt.xticks(range(0,20), provincia.index, rotation=90)
plt.ylabel("Numero di incidenti e feriti (2018)")
plt.tight_layout()
plt.show()

# IMP: Roma e Milano sono outlier

# inc = data['INC']
# fer = data['FER']
# mor = data['MOR']

# print(inc.corr(fer))
# print(inc.corr(mor))
# print(fer.corr(mor))