import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("dataset/autovelox/conclusioni_autovelox.csv", sep=';')

incremento_percentuale_totale = 0
for km, zona in zip(data['Incidenti per chilometro'], data['Incidenti per zona']): 
    incremento_percentuale = (km - zona) * 100 / zona
    incremento_percentuale_totale += incremento_percentuale

colonne = ['Incidenti per chilometro', 'Incidenti per zona']

data.sort_values(by='Incidenti per chilometro', inplace=True, ascending=False)

data[colonne].plot.barh(color=['#a4ce88', '#88a4ce'], width=0.9)
plt.yticks(range(0, len(data)), data['nome'])
plt.legend(bbox_to_anchor=(1,1), loc="upper left")
plt.tight_layout()
plt.show()