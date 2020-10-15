
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

def get_sum_fields(data : pd.DataFrame, select_field : str, field_to_sum : str) -> pd.Series: 
    res = {}
    for field in data[select_field].unique(): 
        res[field] = sum(data[data[select_field] == field][field_to_sum])

    return pd.Series(res)

def sum_columns(data : pd.DataFrame, normalize = False) -> pd.Series: 
    res = {}
    for col in data.columns: 
        res[col] = sum(data[col])

    res = pd.Series(res).transpose()

    if normalize: 
        res = res / sum(res)

    return res

#res = {}
#for prov in lombardia['PROVINCIA'].unique(): 
#    res[prov] = sum(lombardia[lombardia['PROVINCIA'] == prov]['TOTALE'])

#lombardia = get_sum_fields(data, 'REGIONE', 'TOTALE')
#lombardia.plot.bar()
#plt.tight_layout()
#plt.show()

# Per come sono organizzati, i dati sono un po' scomodi

# Voglio vedere la differenza per mese tra due autostrade diverse

mesi = ['Gennaio', 'Febbraio', 'Marzo', 'Aprile', 'Maggio', 'Giugno', 'Luglio', 'Agosto', 'Settembre', 'Ottobre', 'Novembre', 'Dicembre'] 

rimini = data[data['PROVINCIA'] == 'Rimini'][mesi]
milano = data[data['PROVINCIA'] == 'Milano'][mesi]
aosta = data[data['PROVINCIA'] == 'Aosta'][mesi]
roma = data[data['PROVINCIA'] == 'Roma'][mesi]

rimini = sum_columns(rimini)
milano = sum_columns(milano)
aosta = sum_columns(aosta)
roma = sum_columns(roma)

# Normalizzo
#rimini = rimini / sum(rimini)
#milano = milano / sum(milano)
#aosta = aosta / sum(aosta)
#roma =  roma / sum(roma)

#pd.DataFrame([milano, aosta], index=['Milano', 'Aosta']).transpose().plot.bar()
#pd.DataFrame([milano, roma], index=['Milano', 'Roma']).transpose().plot.bar()
#plt.show()

#print(sum_columns(rimini))

# Quali sono le autostrade con più incidenti?

#autostrade = get_sum_fields(data, 'NOME STRADA', 'TOTALE').sort_values(ascending=True)
#autostrade[autostrade > 400].plot.barh()
#plt.tight_layout()
#plt.xlabel("Autostrade con più incidenti totali")
#plt.show()

#print(autostrade)

# E in quali mesi avvengono questi incidenti?

adriatica = data[data['CODICE'] == 'SS01601'][mesi]
a1 = data[data['CODICE'] == 'AA00101'][mesi]
aurelia = data[data['CODICE'] == 'SS00101'][mesi]

adriatica = sum_columns(adriatica, normalize=True)
a1 = sum_columns(a1, normalize=True)
aurelia =  sum_columns(aurelia, normalize=True)

#pd.DataFrame([a1, adriatica, aurelia], ['A1', 'Adriatica', 'Aurelia']).transpose().plot()
#plt.xlabel("Differenza tra incidenti mensili")
#plt.show()

# Intorno a milano Avvengono più incidenti se inverno?