
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("dataset/incidenti/aci/autostrade/localizzazione_2018.csv")
data = data[data['CODICE'] == 'SS01601']

# Conteggio incidenti e feriti per provincia su SS16
df = {}
for d in data['PROVINCIA'].unique(): 
    df[d] = [
        data[data['PROVINCIA'] == d]['INC'].sum(), 
        data[data['PROVINCIA'] == d]['FER'].sum()
        ]

ss16 = pd.DataFrame(df, index=['Incidenti', 'Feriti']).transpose()

ss16.plot.bar(width=0.9, color=['#4ea051', '#514ea0'])
plt.ylabel("Province attraversate dalla SS16")
plt.tight_layout()
plt.show()