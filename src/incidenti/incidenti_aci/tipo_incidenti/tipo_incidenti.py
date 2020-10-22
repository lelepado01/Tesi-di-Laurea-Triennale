
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("dataset/incidenti/aci/autostrade/localizzazione_2012.csv")

#print(data.columns)

# IMP: questo dataset ha dei campi senza nome e di cui non mi fiderei

tipo = data[['ScFRONTALE', 'ScFRONTLAT-ScLAT', 'TAMPONAMENTO','InvPEDONI', 'FUORIUSCITA']]

print(tipo)

