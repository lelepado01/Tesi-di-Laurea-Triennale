import pandas as pd
import sys
sys.path.append("src")
import aci_utils

data = pd.read_csv("dataset/incidenti/aci/autostrade/mesi_2018.csv")

mesi = ['Gennaio', 'Febbraio', 'Marzo', 'Aprile', 'Maggio', 'Giugno', 'Luglio', 'Agosto', 'Settembre', 'Ottobre', 'Novembre', 'Dicembre'] 

raccordo = data[data['CODICE'] == 'AA09001']
raccordo = aci_utils.sum_columns(raccordo[mesi])
racc_mean = raccordo.mean()
print((raccordo['Agosto'] - racc_mean) / racc_mean) # -0.46