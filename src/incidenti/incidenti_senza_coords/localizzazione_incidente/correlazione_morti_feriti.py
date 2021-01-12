
import pandas as pd

data = pd.read_csv("dataset/incidenti/istat/incidenti_2018.txt", sep="\t", encoding='latin1')

incroci = 'intersezione_o_non_interse3'
morti = ['morti_entro_24_ore', 'morti_entro_30_giorni']

data['morti'] = data[morti[0]] + data[morti[1]]

print("Corr. tra morti e feriti", data['feriti'].corr(data['morti']))
# Le altre due combinazioni non possono essere calcolate per la forma del  dataset, a 
# ogni riga corrisponde un incidente 
# Se calcolata così si ha correlazione molto bassa

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

# Calcolo della correlazione in base al tipo di intersezione
print("Corr. tra morti e feriti", indici['feriti'].corr(indici['morti']))
# = 0.9590
print("Corr. tra incidenti e feriti", indici['incidenti'].corr(indici['feriti']))
# = 0.9998
print("Corr. tra incidenti e morti", indici['incidenti'].corr(indici['morti']))
# = 0.9603