
import pandas as pd
import matplotlib.pyplot as plt
import sys
sys.path.append('src')
import aci_utils

data = pd.read_csv("dataset/incidenti/incidenti_2010.txt", sep='\t')

# Ci sono tipi di incidenti che favoriscono feriti/morti?

tipo_incidenti = data[['natura_incidente', 'feriti']]
#print(tipo_incidenti['feriti'].unique())

#print(tipo_incidenti['natura_incidente'].corr(tipo_incidenti['feriti'])) = -0.1378

# Davvero? non c'è correlazione?

#numero_incidenti_per_tipo = tipo_incidenti['natura_incidente'].value_counts()
#tipo_incidenti = aci_utils.sum_field_by_column(tipo_incidenti, 'natura_incidente', 'feriti')

#print(tipo_incidenti)
#print(numero_incidenti_per_tipo)

#print(numero_incidenti_per_tipo.corr(tipo_incidenti['val']))
#
#pd.DataFrame(
#    [numero_incidenti_per_tipo, tipo_incidenti['val']], 
#    ['incidenti', 'feriti']
#    ).transpose().plot()
#plt.show()


