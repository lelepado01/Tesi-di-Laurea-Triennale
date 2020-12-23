
import pandas as pd

def variazione_perc(x : float, y : float) -> float: 
    return (y / x) * 100 -100

mese_utilizzato = 7

path = "dataset/incidenti/istat/incidenti_"
for year in range(2010, 2014):
    dati = pd.read_csv(path + str(year) + ".txt", sep='\t')
    rimini_mese = dati[dati['provincia'] == 99]['mese'].value_counts().sort_index()

    index = 0
    for giorni_in_mese in [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]:
        rimini_mese.iloc[index] /= giorni_in_mese
        index += 1

    media = rimini_mese.mean()
    mese_scelto = rimini_mese.iloc[mese_utilizzato]

    print(str(year) + ": " + str(variazione_perc(media, mese_scelto)))


