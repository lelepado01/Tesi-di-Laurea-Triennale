
import pandas as pd
import matplotlib.pyplot as plt
import sys
sys.path.append("src/")
import label_utils

path = "dataset/incidenti/incidenti_2010.txt"

data = pd.read_csv(path, sep="\t")

tipo_veicoli = data['tipo_veicolo_a']
tipo_veicoli = label_utils.join_labels(tipo_veicoli, "dataset/incidenti/Classificazioni/tipo_veicoli__b_.csv").value_counts().sort_index()
#print(tipo_veicoli)

#tipo_veicoli.plot.barh()
#plt.show()

# I principali veicoli coinvolti sono: 
#   - auto private
#   - moto private
#   - autocarri

# Cambia se seleziono strade differenti?
autostrade_veicoli = data[data['localizzazione_incidente'] == 7]['tipo_veicolo_a']
autostrade_veicoli = label_utils.join_labels(autostrade_veicoli, "dataset/incidenti/Classificazioni/tipo_veicoli__b_.csv").value_counts(normalize=True).sort_index()

#uniti = pd.DataFrame([
#    tipo_veicoli, autostrade_veicoli
#], index=['tutti', 'autostrade']).transpose()

#autostrade_veicoli.plot.barh()
#plt.show()

strade_urbane = data[(data['localizzazione_incidente'] == 1) | (data['localizzazione_incidente'] == 2) | (data['localizzazione_incidente'] == 3)]['tipo_veicolo_a']
strade_urbane = label_utils.join_labels(strade_urbane, "dataset/incidenti/Classificazioni/tipo_veicoli__b_.csv").value_counts(normalize=True).sort_index()

#strade_urbane.plot.barh()
#plt.show()

strade_extraurbane = data[(data['localizzazione_incidente'] == 4) | (data['localizzazione_incidente'] == 5) | (data['localizzazione_incidente'] == 6)]['tipo_veicolo_a']
strade_extraurbane = label_utils.join_labels(strade_extraurbane, "dataset/incidenti/Classificazioni/tipo_veicoli__b_.csv").value_counts(normalize=True).sort_index()

uniti = pd.DataFrame([
    autostrade_veicoli, strade_urbane, strade_extraurbane
], index=['Autostrade', 'Strade urbane', 'Strade Extra-Urbane']).transpose()

uniti.dropna().plot.bar()
plt.tight_layout()
plt.show()

# Nelle strade urbane ci sono molti più incidenti con velocipedi e ciclomotori, 
# mentre nelle autostrade con autocarri e automobili
