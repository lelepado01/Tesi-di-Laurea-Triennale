
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
#autostrade_veicoli = data[data['localizzazione_incidente'] == 7]['tipo_veicolo_a']
#autostrade_veicoli = label_utils.join_labels(autostrade_veicoli, "dataset/incidenti/Classificazioni/tipo_veicoli__b_.csv").value_counts(normalize=True).sort_index()

#uniti = pd.DataFrame([
#    tipo_veicoli, autostrade_veicoli
#], index=['tutti', 'autostrade']).transpose()

#autostrade_veicoli.plot.barh()
#plt.show()

#strade_urbane = data[(data['localizzazione_incidente'] == 1) | (data['localizzazione_incidente'] == 2) | (data['localizzazione_incidente'] == 3)]['tipo_veicolo_a']
#strade_urbane = label_utils.join_labels(strade_urbane, "dataset/incidenti/Classificazioni/tipo_veicoli__b_.csv").value_counts(normalize=True).sort_index()

#strade_urbane.plot.barh()
#plt.show()

#strade_extraurbane = data[(data['localizzazione_incidente'] == 4) | (data['localizzazione_incidente'] == 5) | (data['localizzazione_incidente'] == 6)]['tipo_veicolo_a']
#strade_extraurbane = label_utils.join_labels(strade_extraurbane, "dataset/incidenti/Classificazioni/tipo_veicoli__b_.csv").value_counts(normalize=True).sort_index()

#uniti = pd.DataFrame([
#    autostrade_veicoli, strade_urbane, strade_extraurbane
#], index=['Autostrade', 'Strade urbane', 'Strade Extra-Urbane']).transpose()

#uniti[uniti > 0.001].dropna().plot.bar()
#plt.tight_layout()
#plt.show()

# Nelle strade urbane ci sono molti più incidenti con velocipedi e ciclomotori, 
# mentre nelle autostrade con autocarri e automobili


# Il numero di uomini / donne alla guida cambia al cambiare del tipo di strada?

#strade_urbane = data[(data['localizzazione_incidente'] == 1) | (data['localizzazione_incidente'] == 2) | (data['localizzazione_incidente'] == 3)]['veicolo__a___sesso_conducente']
#strade_extraurbane = data[(data['localizzazione_incidente'] == 4) | (data['localizzazione_incidente'] == 5) | (data['localizzazione_incidente'] == 6)]['veicolo__a___sesso_conducente']
#autostrade = data[data['localizzazione_incidente'] == 7]['veicolo__a___sesso_conducente']
#
#strade_urbane = strade_urbane[strade_urbane != ' '].astype(int)
#strade_extraurbane = strade_extraurbane[strade_extraurbane != ' '].astype(int)
#autostrade = autostrade[autostrade != ' '].astype(int)
#
#strade_extraurbane = label_utils.join_labels(strade_extraurbane, "dataset/incidenti/Classificazioni/veicolo__a___sesso_conducente.csv").value_counts(normalize=True).sort_index()
#strade_urbane = label_utils.join_labels(strade_urbane, "dataset/incidenti/Classificazioni/veicolo__a___sesso_conducente.csv").value_counts(normalize=True).sort_index()
#autostrade = label_utils.join_labels(autostrade, "dataset/incidenti/Classificazioni/veicolo__a___sesso_conducente.csv").value_counts(normalize=True).sort_index()
#
#pd.DataFrame(
#    [strade_extraurbane, strade_urbane, autostrade], 
#    index=['Autostrade', 'Strade urbane', 'Strade Extra-Urbane']
#    ).transpose().plot.bar()
#plt.tight_layout()
#plt.show()


#strade_urbane = data[(data['localizzazione_incidente'] == 1) | (data['localizzazione_incidente'] == 2) | (data['localizzazione_incidente'] == 3)]['veicolo__a___et__conducente']
#strade_extraurbane = data[(data['localizzazione_incidente'] == 4) | (data['localizzazione_incidente'] == 5) | (data['localizzazione_incidente'] == 6)]['veicolo__a___et__conducente']
#autostrade = data[data['localizzazione_incidente'] == 7]['veicolo__a___et__conducente']
#
#strade_urbane = strade_urbane[strade_urbane != '  '].astype(int)
#strade_extraurbane = strade_extraurbane[strade_extraurbane != '  '].astype(int)
#autostrade = autostrade[autostrade != '  '].astype(int)
#
#strade_extraurbane = label_utils.join_labels(strade_extraurbane, "dataset/incidenti/Classificazioni/veicolo__a___et__conducente.csv").value_counts(normalize=True).sort_index()
#strade_urbane = label_utils.join_labels(strade_urbane, "dataset/incidenti/Classificazioni/veicolo__a___et__conducente.csv").value_counts(normalize=True).sort_index()
#autostrade = label_utils.join_labels(autostrade, "dataset/incidenti/Classificazioni/veicolo__a___et__conducente.csv").value_counts(normalize=True).sort_index()
#
#pd.DataFrame(
#    [strade_extraurbane, strade_urbane, autostrade], 
#    index=['Autostrade', 'Strade urbane', 'Strade Extra-Urbane']
#    ).transpose().plot()
#plt.tight_layout()
#plt.show()

# TODO: i maggiori incidenti da donne in strade urbane vale per ogni anno?

def get_gender_ratio(data) -> pd.DataFrame: 
    strade_urbane = data[(data['localizzazione_incidente'] == 1) | (data['localizzazione_incidente'] == 2) | (data['localizzazione_incidente'] == 3)]['veicolo__a___sesso_conducente']
    strade_extraurbane = data[(data['localizzazione_incidente'] == 4) | (data['localizzazione_incidente'] == 5) | (data['localizzazione_incidente'] == 6)]['veicolo__a___sesso_conducente']
    autostrade = data[data['localizzazione_incidente'] == 7]['veicolo__a___sesso_conducente']

    strade_urbane = strade_urbane[strade_urbane != ' '].astype(int)
    strade_extraurbane = strade_extraurbane[strade_extraurbane != ' '].astype(int)
    autostrade = autostrade[autostrade != ' '].astype(int)

    strade_extraurbane = label_utils.join_labels(strade_extraurbane, "dataset/incidenti/Classificazioni/veicolo__a___sesso_conducente.csv").value_counts(normalize=True).sort_index()
    strade_urbane = label_utils.join_labels(strade_urbane, "dataset/incidenti/Classificazioni/veicolo__a___sesso_conducente.csv").value_counts(normalize=True).sort_index()
    autostrade = label_utils.join_labels(autostrade, "dataset/incidenti/Classificazioni/veicolo__a___sesso_conducente.csv").value_counts(normalize=True).sort_index()

    return pd.DataFrame(
        [strade_extraurbane, strade_urbane, autostrade], 
        index=['Autostrade', 'Strade urbane', 'Strade Extra-Urbane']
        ).transpose()

plt.subplot(211)
gen_2011 = get_gender_ratio(pd.read_csv("dataset/incidenti/incidenti_2011.txt", sep='\t'))

plt.bar(gen_2011.transpose().index, gen_2011.transpose(), alpha=0.3)
plt.tight_layout()
#gen_2012 = get_gender_ratio(pd.read_csv("dataset/incidenti/incidenti_2012.txt", sep='\t'))
#plt.subplot(212)
#for field in gen_2012.columns: 
#    plt.bar(field, gen_2012[field])
#plt.bar(gen_2011.index, gen_2011['Autostrade'])
#plt.bar(gen_2011.index, gen_2012['Autostrade'])
#plt.figure(3)
#plt.subplot(213)
#gen_2013 = get_gender_ratio(pd.read_csv("dataset/incidenti/incidenti_2013.txt", sep='\t')).plot.bar()
#plt.figure(4)
#plt.subplot(214)
#gen_2015 = get_gender_ratio(pd.read_csv("dataset/incidenti/incidenti_2015.txt", sep='\t', encoding='latin1')).plot.bar()

plt.show()

# sembra che la tendenza rimanga negli anni

# Realizzare grafo per visualizzare