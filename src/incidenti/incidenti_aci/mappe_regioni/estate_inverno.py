
import pandas as pd
import matplotlib.pyplot as plt

order = [
    'Piemonte', 'Valle d\'Aosta', 'Liguria', 'Lombardia', 
    'Trentino-Alto Adige', 'Veneto', 'Friuli-Venezia Giulia', 'Emilia Romagna', 
    'Toscana', 'Umbria', 'Marche', 'Lazio', 
    'Abruzzo', 'Molise', 'Campania', 'Puglia', 'Basilicata', 'Calabria', 
    'Sicilia', 'Sardegna'
]

def get_sum_of_fields(data : pd.DataFrame, select_field : str, field_to_sum : str) -> pd.Series: 
    res = {}
    index = 0
    for reg in data[select_field].unique():
        res[index] = [reg, 0]
        index += 1

    index = 0
    for reg in data[select_field].unique():
        for row in data[data[select_field] == reg][field_to_sum]:
            res[index] = [res[index][0], res[index][1] + row]
        index += 1

    return pd.DataFrame(res, index=[select_field, field_to_sum]).transpose()


data = pd.read_csv('dataset/incidenti/aci/autostrade/mesi_2018.csv') 
data = data[data['TOTALE'] != '0,0'].astype({'TOTALE': int})

estate = pd.Series() 
for mese in ['Giugno', 'Luglio', 'Agosto']: 
    e = get_sum_of_fields(data, 'REGIONE', mese)
    e.index = e['REGIONE']
    e.reindex(order)
    e = e[mese]
    if mese == 'Giugno': 
        estate = e
    else: 
        estate += e


inverno = pd.Series()
for mese in ['Dicembre', 'Gennaio', 'Febbraio']: 
    e = get_sum_of_fields(data, 'REGIONE', mese)
    e.index = e['REGIONE']
    e.reindex(order)
    e = e[mese]
    if mese == 'Dicembre': 
        inverno = e
    else: 
        inverno += e

red_ls = ['#ce7182']*20
blue_ls = ['#cebd71']*20

df = pd.DataFrame([inverno, estate], ['Inverno', 'Estate']).transpose()
df.plot.bar(width=0.9, color=[red_ls, blue_ls])

plt.text(2, 1800, "Nord Italia")
plt.text(8, 1100, "Centro Italia")
plt.text(15, 700, "Sud Italia")

plt.xlabel("")
plt.ylabel("Numero incidenti per mesi invernali e estivi")
plt.tight_layout()
plt.show()
