
import pandas as pd
import matplotlib.pyplot as plt
import sys
sys.path.append("src")
import aci_utils

data = pd.read_csv("dataset/incidenti/aci/autostrade/comuni_2016.csv")

fields = ['INC','FER']

#print(len(data['PROVINCIA'].unique()))

# Il numero di feriti dipende dal numero di incidenti?
# E il numero di morti?

#provincia = aci_utils.sum_field_by_column(data, 'PROVINCIA', fields).transpose()
# Calcolo coeff. di correlazione
#print(provincia['FER'].corr(provincia['INC'])) = 0.9826611644228044
# Il coeff. di Pearson è molto vicino a 1, i due campioni sono strettamente correlati
#print(provincia['MOR'].corr(provincia['INC'])) = 0.8204903971483627
#print(provincia['MOR'].corr(provincia['FER'])) = 0.8332572834970239
# Correlazione più debole, ma comunque presente

# provincia = provincia.sort_values(by='Inc', ascending=False).head(10)
# provincia.plot()
# plt.show()

# IMP: Roma e Milano sono outlier