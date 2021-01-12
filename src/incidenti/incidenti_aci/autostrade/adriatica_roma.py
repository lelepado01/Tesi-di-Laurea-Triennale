
import pandas as pd
import matplotlib.pyplot as plt
import sys 
sys.path.append("src")
import aci_utils

data = pd.read_csv("dataset/incidenti/aci/autostrade/mesi_2018.csv")

mesi = ['Gennaio', 'Febbraio', 'Marzo', 'Aprile', 'Maggio', 'Giugno', 'Luglio', 'Agosto', 'Settembre', 'Ottobre', 'Novembre', 'Dicembre'] 

# Selezione dati per raccordo anulare di Roma
raccordo = data[data['CODICE'] == 'AA09001']
# Selezione dati per SS16 Adriatica
adriatica = data[data['CODICE'] == 'SS01601']

adriatica = aci_utils.sum_columns(adriatica[mesi])
raccordo = aci_utils.sum_columns(raccordo[mesi])

df = pd.DataFrame([adriatica, raccordo], ['Adriatica', 'Raccordo Anulare Roma']).transpose()

df.plot.bar(width=0.9, color=['#a1cc61', '#61a1cc'])
plt.ylabel("Numero di incidenti al mese (2018)")
plt.tight_layout()
plt.show()