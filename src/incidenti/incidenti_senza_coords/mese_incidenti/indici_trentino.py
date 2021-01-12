
import pandas as pd

def variazione_perc(x : float, y : float) -> float: 
    return (y / x) * 100 -100

anno_utilizzato = 2013
provincia_utilizzata = 22
mese_utilizzato = 2

path = "dataset/incidenti/istat/incidenti_"

dati = pd.read_csv(path + str(anno_utilizzato) + ".txt", sep='\t')
rimini_mese = dati[dati['provincia'] == provincia_utilizzata]['mese'].value_counts().sort_index()

index = 0
for giorni_in_mese in [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]:
    rimini_mese.iloc[index] /= giorni_in_mese
    index += 1

media = rimini_mese.mean()

mese_scelto = rimini_mese.iloc[mese_utilizzato]
print(str(anno_utilizzato) + "/" + str(mese_utilizzato) + ": " + str(variazione_perc(media, mese_scelto)))


