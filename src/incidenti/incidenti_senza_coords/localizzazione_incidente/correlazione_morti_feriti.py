import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("dataset/incidenti/incidenti_2018.txt", sep="\t", encoding='latin1')

incroci = 'intersezione_o_non_interse3'
morti = ['morti_entro_24_ore', 'morti_entro_30_giorni']

data['morti'] = data[morti[0]] + data[morti[1]]

morti = {}
feriti = {}
for inc in data[incroci].unique(): 
    morti[inc] = 0
    feriti[inc] = 0

for inc, mor in zip(data[incroci], data['morti']): 
    morti[inc] += mor

for inc, fer in zip(data[incroci], data['feriti']):
    feriti[inc] += fer

inc = data[incroci].value_counts()

indici = pd.DataFrame(morti, index=['morti']).transpose()
indici['feriti'] = feriti.values()
indici['incidenti'] = inc

print(indici)

print("Corr. tra morti e feriti", indici['feriti'].corr(indici['morti']))
print("Corr. tra incidenti e feriti", indici['incidenti'].corr(indici['feriti']))
print("Corr. tra incidenti e morti", indici['incidenti'].corr(indici['morti']))