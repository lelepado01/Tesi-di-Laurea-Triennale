
import pandas as pd
import matplotlib.pyplot as plt

path = "dataset/incidenti/incidenti_2010.txt"

data = pd.read_csv(path, sep="\t")

tipo_veicoli = data['tipo_veicolo_a'].value_counts().sort_index()
#print(tipo_veicoli)

tipo_veicoli[tipo_veicoli > 100].plot.bar()
plt.show()

# I principali veicoli coinvolti sono: 
#   - auto private
#   - moto private
#   - autocarri
 
# TODO: altri dati disponibili