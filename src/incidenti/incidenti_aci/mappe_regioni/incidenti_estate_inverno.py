
import pandas as pd
import matplotlib.pyplot as plt

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

agosto = get_sum_of_fields(data, 'REGIONE', 'Agosto')
gennaio = get_sum_of_fields(data, 'REGIONE', 'Gennaio')

agosto.index = agosto['REGIONE']
gennaio.index = gennaio['REGIONE']
agosto = agosto['Agosto']
gennaio = gennaio['Gennaio']

red_ls = ['#ce7182']*20
blue_ls = ['#cebd71']*20

order = [
    'Piemonte', 'Valle d\'Aosta', 'Liguria', 'Lombardia', 
    'Trentino-Alto Adige', 'Veneto', 'Friuli-Venezia Giulia', 'Emilia Romagna', 
    'Toscana', 'Umbria', 'Marche', 'Lazio', 
    'Abruzzo', 'Molise', 'Campania', 'Puglia', 'Basilicata', 'Calabria', 
    'Sicilia', 'Sardegna'
]

agosto = agosto.reindex(order)
gennaio = gennaio.reindex(order)

pd.DataFrame(
    [agosto, gennaio], 
    ['Agosto', 'Gennaio']
).transpose().plot.bar(width=0.9, color=[red_ls, blue_ls])

plt.text(2, 490, "Nord Italia")
plt.text(8, 320, "Centro Italia")
plt.text(15, 230, "Sud Italia")

plt.xticks(rotation=90)
plt.ylabel("Incidenti al mese (2018)")
plt.xlabel("")
plt.legend()
plt.tight_layout()
plt.show()