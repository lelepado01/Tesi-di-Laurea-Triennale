
import pandas as pd
import matplotlib.pyplot as plt

# I dati sulle strade provinciali sono meno...

data = pd.read_csv("dataset/incidenti/aci/strade_provinciali/aci_2018.csv")
#print(data.columns)

print(data[data['provincia'] == 'Milano']['nome strada'].value_counts())

# I dati sulle autostrade hanno anche mese, ora e giorno della settimana, 
# con la posizione in quale autostrada

data_autostrade = pd.read_csv("dataset/incidenti/aci/autostrade/localizzazione_2018.csv")

print(data_autostrade['NOME STRADA'].value_counts())

# PROBLEMA: i dati sono già elaborati

