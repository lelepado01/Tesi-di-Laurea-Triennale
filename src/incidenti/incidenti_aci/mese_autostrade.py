
import pandas as pd
import matplotlib.pyplot as plt

# Come cambiano gli incidenti in base la mese sulle autostrade?

data = pd.read_csv("dataset/incidenti/aci/autostrade/mesi_2018.csv")

#print(data.columns)
#print(data[data['NOME STRADA']== 'A 01 -  Milano-Roma-Napoli (Autostrada del Sole)'])

# Ci sono più colonne per Provincia, strada ecc...
# I dati vanno comunque modificati

lombardia = data[data['REGIONE'] == 'Lombardia'][['PROVINCIA', 'TOTALE']]
#print(lombardia)

res = {}
for prov in lombardia['PROVINCIA'].unique(): 
    res[prov] = sum(lombardia[lombardia['PROVINCIA'] == prov]['TOTALE'])

lombardia = pd.Series(res)
lombardia.plot.bar()
plt.tight_layout()
plt.show()


