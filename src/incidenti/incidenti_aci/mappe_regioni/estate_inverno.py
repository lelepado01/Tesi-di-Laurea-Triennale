
import pandas as pd
import matplotlib.pyplot as plt
import sys
sys.path.append("src")
import aci_utils

# L'ordine utilizzato raggruppa le regioni del nord, centro e sud
order = [
    'Piemonte', 'Valle d\'Aosta', 'Liguria', 'Lombardia', 
    'Trentino-Alto Adige', 'Veneto', 'Friuli-Venezia Giulia', 'Emilia Romagna', 
    'Toscana', 'Umbria', 'Marche', 'Lazio', 
    'Abruzzo', 'Molise', 'Campania', 'Puglia', 'Basilicata', 'Calabria', 
    'Sicilia', 'Sardegna'
]

data = pd.read_csv('dataset/incidenti/aci/autostrade/mesi_2018.csv') 
data = data[data['TOTALE'] != '0,0'].astype({'TOTALE': int})

# Conteggio incidenti in mesi estivi
estate = pd.Series() 
for mese in ['Giugno', 'Luglio', 'Agosto']: 
    e = aci_utils.get_sum_of_fields(data, 'REGIONE', mese)
    e.index = e['REGIONE']
    e.reindex(order)
    e = e[mese]
    if mese == 'Giugno': 
        estate = e
    else: 
        estate += e

# Conteggio incidenti in mesi invernali
inverno = pd.Series()
for mese in ['Dicembre', 'Gennaio', 'Febbraio']: 
    e = aci_utils.get_sum_of_fields(data, 'REGIONE', mese)
    e.index = e['REGIONE']
    e.reindex(order)
    e = e[mese]
    if mese == 'Dicembre': 
        inverno = e
    else: 
        inverno += e

# Colorazione per grafico
red_ls = ['#7cd6aa']*20
blue_ls = ['#7ca7d6']*20

df = pd.DataFrame([inverno, estate], ['Inverno', 'Estate']).transpose()
df.plot.bar(width=0.9, color=[blue_ls, red_ls])
# Aggiunta di testi per indicare le regioni di nord, centro e sud
plt.text(2, 1800, "Nord Italia")
plt.text(8, 1100, "Centro Italia")
plt.text(15, 700, "Sud Italia")
# Eliminazione x label, che altrimenti mostrerebbe 'REGIONE'
plt.xlabel("")
plt.ylabel("Incidenti in mesi invernali e estivi")
plt.tight_layout()
plt.show()
