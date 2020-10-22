
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


tamponamento = tipo_incidenti[tipo_incidenti['natura_incidente'] == 4]['feriti'].value_counts(normalize=True)
frontale = tipo_incidenti[tipo_incidenti['natura_incidente'] == 1]['feriti'].value_counts(normalize=True)
pedoni = tipo_incidenti[tipo_incidenti['natura_incidente'] == 5]['feriti'].value_counts(normalize=True)
sbandamento = tipo_incidenti[tipo_incidenti['natura_incidente'] == 10]['feriti'].value_counts(normalize=True)
tamponamento = tamponamento[tamponamento > 0.01]
frontale = frontale[frontale > 0.01]
pedoni = pedoni[pedoni > 0.01]
sbandamento = sbandamento[sbandamento > 0.01]
#print(tamponamento.value_counts())
#print(frontale.value_counts())

pd.DataFrame(
    [tamponamento, frontale, pedoni, sbandamento], 
    ['tamponamento', 'frontale', 'pedoni', 'sbandamento']
).transpose().plot.bar()
plt.show()