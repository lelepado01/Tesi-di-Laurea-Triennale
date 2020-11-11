
from matplotlib import markers
from matplotlib.pyplot import legend
import pandas as pd
import matplotlib.pyplot as plt
import sys
sys.path.append('src')
import aci_utils

data = pd.read_csv("dataset/incidenti/incidenti_2010.txt", sep='\t')

# Ci sono tipi di incidenti che favoriscono feriti/morti?

tipo_incidenti = data[['natura_incidente', 'feriti']]

tamponamento = tipo_incidenti[tipo_incidenti['natura_incidente'] == 4]['feriti'].value_counts(normalize=True)
frontale = tipo_incidenti[tipo_incidenti['natura_incidente'] == 1]['feriti'].value_counts(normalize=True)
pedoni = tipo_incidenti[tipo_incidenti['natura_incidente'] == 5]['feriti'].value_counts(normalize=True)
sbandamento = tipo_incidenti[tipo_incidenti['natura_incidente'] == 10]['feriti'].value_counts(normalize=True)

# tamponamento = tamponamento[tamponamento > 0.01]
# frontale = frontale[frontale > 0.01]
# pedoni = pedoni[pedoni > 0.01]
# sbandamento = sbandamento[sbandamento > 0.01]

df = pd.DataFrame(
    [tamponamento, frontale, pedoni, sbandamento], 
    ['tamponamento', 'frontale', 'pedoni', 'sbandamento']
)#.transpose()
df = df[[1,2,3,4]].transpose()

# df.plot.bar(width=0.8)
# plt.xticks(rotation=0)
# plt.xlabel("Numero di feriti")
# plt.ylabel("Percentuale di feriti rispetto al totale del tipo di incidente")
# plt.show()

tamponamento = pd.Series(
    [tamponamento[1], tamponamento[2], tamponamento[3], tamponamento[4], 1-tamponamento[[1,2,3,4]].sum()], 
    index=["1","2","3","4","altro"]
    )

frontale = pd.Series(
    [frontale[1], frontale[2], frontale[3], frontale[4], 1-frontale[[1,2,3,4]].sum()], 
    index=["1","2","3","4","altro"]
    )

pedoni = pd.Series(
    [pedoni[1], pedoni[2], pedoni[3], pedoni[4], 1-pedoni[[1,2,3,4]].sum()], 
    index=["1","2","3","4","altro"]
    )

sbandamento = pd.Series(
    [sbandamento[1], sbandamento[2], sbandamento[3], sbandamento[4], 1-sbandamento[[1,2,3,4]].sum()], 
    index=["1","2","3","4","altro"]
    )

# print(tamponamento)
# print(frontale)
# print(pedoni)
# print(sbandamento)

# plt.subplot(2,2,1)
# plt.pie(tamponamento)
# plt.plot(pd.Series([0]), marker='o', markersize=80, color='white')

# plt.subplot(2,2,2)
# plt.pie(frontale)
# plt.plot(pd.Series([0]), marker='o', markersize=80, color='white')

# plt.subplot(2,2,3)
# plt.pie(pedoni)
# plt.plot(pd.Series([0]), marker='o', markersize=80, color='white')

# plt.subplot(2,2,4)
# plt.pie(sbandamento)
sbandamento.plot.pie(legend=True, radius=0.2)
plt.legend(bbox_to_anchor=(1,1), loc="upper left")
plt.plot(pd.Series([0]), marker='o', markersize=80, color='white')
plt.legend()
plt.show()