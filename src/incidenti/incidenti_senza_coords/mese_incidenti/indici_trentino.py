
import pandas as pd
import matplotlib.pyplot as plt

def variazione_perc(x : float, y : float) -> float: 
    return (y / x) * 100 -100

anno_utilizzato = 2013
provincia_utilizzata = 22

path = "dataset/incidenti/istat/incidenti_"

dati = pd.read_csv(path + str(anno_utilizzato) + ".txt", sep='\t')
rimini_mese = dati[dati['provincia'] == provincia_utilizzata]['mese'].value_counts().sort_index()

index = 0
for giorni_in_mese in [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]:
    rimini_mese.iloc[index] /= giorni_in_mese
    index += 1

media = rimini_mese.mean()

rimini_mese.plot.bar()
plt.show()

# mese_scelto = rimini_mese.iloc[mese_utilizzato]
# print(str(year) + ": " + str(variazione_perc(media, mese_scelto)))


