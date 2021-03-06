
import pandas as pd

def variazione_perc(x : float, y : float) -> float: 
    return (y / x) * 100 -100

mese_scelto = 7
path = "dataset/incidenti/istat/incidenti_"
# Per ogni anno, somma per mese, degli incidenti a Milano (cod. 15)
for year in range(2011, 2014):
    dati = pd.read_csv(path + str(year) + ".txt", sep='\t', encoding='latin1')
    milano_mese = dati[dati['provincia'] == 15]['mese'].value_counts().sort_index()

    index = 0
    for giorni_in_mese in [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]:
        milano_mese.iloc[index] /= giorni_in_mese
        index += 1

    media = milano_mese.mean()
    mese_utilizzato = milano_mese.iloc[mese_scelto]

    print(str(year) + ": " + str(variazione_perc(media, mese_utilizzato)))

