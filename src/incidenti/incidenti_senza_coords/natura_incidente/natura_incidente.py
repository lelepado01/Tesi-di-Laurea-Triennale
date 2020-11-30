
import pandas as pd
import matplotlib.pyplot as plt
import sys
sys.path.append('src')
import aci_utils

data = pd.read_csv("dataset/incidenti/incidenti_2010.txt", sep='\t')

tipo_incidenti = data[['natura_incidente', 'feriti']]

tamponamento = tipo_incidenti[tipo_incidenti['natura_incidente'] == 4]['feriti']
frontale = tipo_incidenti[tipo_incidenti['natura_incidente'] == 1]['feriti']
ostacolo = tipo_incidenti[tipo_incidenti['natura_incidente'] == 8]['feriti']
sbandamento = tipo_incidenti[tipo_incidenti['natura_incidente'] == 10]['feriti']

tamponamento = tamponamento.value_counts()
frontale = frontale.value_counts()
ostacolo = ostacolo.value_counts()
sbandamento = sbandamento.value_counts()

df = pd.DataFrame(
    [tamponamento, frontale, ostacolo, sbandamento], 
    ['tamponamento', 'frontale', 'ostacolo', 'sbandamento']
)#.transpose()
df = df[[1,2,3,4]].transpose()

color_ls = ['#60c1c1', '#6060c1', '#c16060', '#c1c160']

df.plot.bar(width=0.9, color=color_ls)
plt.xticks(rotation=0)
plt.xlabel("Numero di feriti")
plt.ylabel("Incidenti con specifico numero di feriti")
plt.show()

