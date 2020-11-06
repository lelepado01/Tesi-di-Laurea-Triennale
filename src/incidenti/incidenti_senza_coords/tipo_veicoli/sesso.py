

import pandas as pd
import matplotlib.pyplot as plt
import sys
sys.path.append("src/")
import label_utils

path = "dataset/incidenti/incidenti_2012.txt"

data = pd.read_csv(path, sep="\t", encoding='latin1')

strade_urbane = data[(data['localizzazione_incidente'] == 1) | (data['localizzazione_incidente'] == 2) | (data['localizzazione_incidente'] == 3)]['veicolo__a___sesso_conducente']
strade_extraurbane = data[(data['localizzazione_incidente'] == 4) | (data['localizzazione_incidente'] == 5) | (data['localizzazione_incidente'] == 6)]['veicolo__a___sesso_conducente']
autostrade = data[data['localizzazione_incidente'] == 7]['veicolo__a___sesso_conducente']

strade_urbane = strade_urbane[strade_urbane != ' '].astype(int).value_counts(normalize=True)
strade_extraurbane = strade_extraurbane[strade_extraurbane != ' '].astype(int).value_counts(normalize=True)
autostrade = autostrade[autostrade != ' '].astype(int).value_counts(normalize=True)

df = pd.DataFrame(
    [strade_extraurbane, strade_urbane, autostrade], 
    index=['Autostrade', 'Strade urbane', 'Strade Extra-Urbane']
).transpose()
print(df)
# print(pd.crosstab(df, columns=[1,2]))