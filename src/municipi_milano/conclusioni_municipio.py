import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("dataset/milano_municipi/conclusioni_municipio.csv", sep=';')

incremento_percentuale_totale = 0
for km, zona in zip(data['Incidenti per chilometro'], data['Incidenti per zona']): 
    incremento_percentuale = (km - zona) * 100 / zona
    incremento_percentuale_totale += incremento_percentuale

data[['Incidenti per chilometro', 'Incidenti per zona']].plot.barh(color=['#dd994f', '#4f94dd'], width=0.9 )
plt.yticks(range(0, len(data)), data['nome'])
plt.legend(bbox_to_anchor=(1,1), loc="upper left")
plt.tight_layout()
plt.show()