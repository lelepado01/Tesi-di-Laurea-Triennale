
import pandas as pd
import matplotlib.pyplot as plt

# I dati sulle autostrade hanno anche mese, ora e giorno della settimana, 
# con la posizione in quale autostrada

data_autostrade = pd.read_csv("dataset/incidenti/aci/autostrade/localizzazione_2018.csv")

print(data_autostrade['NOME STRADA'].value_counts().sort_values(ascending=False).head(20))
