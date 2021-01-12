
import pandas as pd

def variazione_perc(x : float, y : float) -> float: 
    return (y / x) * 100 -100

mese_utilizzato = 7
path = "dataset/incidenti/istat/incidenti_"

# Per ogni anno, somma per mese, degli incidenti ad Aosta (cod. 7)
years = []
for year in range(2010, 2014):
    dati = pd.read_csv(path + str(year) + ".txt", sep='\t')
    aosta_mese = dati[dati['provincia'] == 7]['mese'].value_counts().sort_index()

    # Nel 2010 non ci sono stati incidenti in febbraio
    ls = []
    if year == 2010: 
        ls = [31, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    else: 
        ls = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
    index = 0
    for giorni_in_mese in ls:
        aosta_mese.iloc[index] /= giorni_in_mese
        index += 1

    media = aosta_mese.mean()
    mese_scelto = aosta_mese.iloc[mese_utilizzato]

    years.append(str(year) + ": " + str(variazione_perc(media, mese_scelto)))

for year in years: 
    print(year)