
import pandas as pd
import matplotlib.pyplot as plt

# path = "dataset/incidenti/incidenti_2013.txt"
# data = pd.read_csv(path, sep="\t")

# milano_mese = data[data['provincia'] == 15]['mese'].value_counts().sort_index()
# rimini_mese = data[data['provincia'] == 99]['mese'].value_counts().sort_index()

# index = 0
# for giorni_in_mese in [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]:
#     rimini_mese.iloc[index] /= giorni_in_mese
#     milano_mese.iloc[index] /= giorni_in_mese
#     index += 1

# milano_media = milano_mese.mean()
# rimini_media = rimini_mese.mean()

# pd.DataFrame([milano_mese, rimini_mese], ['Milano', 'Rimini']).transpose().plot.bar(
#     width=0.9,
#     color={
#         'Milano': '#5747d1',
#         'Rimini': '#d15747'
#     }
# )
# plt.xlabel("")
# plt.ylabel("Incidenti al giorno (2013)")
# plt.xticks(range(0,12), ["Gennaio","Febbraio","Marzo","Aprile","Maggio","Giugno","Luglio","Agosto","Settembre","Ottobre","Novembre","Dicembre"])
# plt.plot([-1, 15], [milano_media, milano_media], color='#c0d147')
# plt.plot([-1, 15], [rimini_media, rimini_media], color='#c0d147')
# plt.text(11.8,milano_media - 0.1,'Media Milano')
# plt.text(11.8,rimini_media - 0.1,'Media Rimini')
# # milano_mese.plot.bar(width=0.8, color='#5747d1')
# # rimini_mese.plot.bar(width=0.8, color='#d15747')
# plt.legend(bbox_to_anchor=(1,1), loc="upper left")
# plt.tight_layout()
# plt.show()

# Calcolo perc di incremento

def variazione_perc(x : float, y : float) -> float: 
    return (y / x) * 100 -100

path = "dataset/incidenti/incidenti_"
for year in range(2010, 2014):
    dati = pd.read_csv(path + str(year) + ".txt", sep='\t')
    rimini_mese = dati[dati['provincia'] == 99]['mese'].value_counts().sort_index()

    index = 0
    for giorni_in_mese in [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]:
        rimini_mese.iloc[index] /= giorni_in_mese
        index += 1

    media = rimini_mese.mean()
    agosto = rimini_mese.iloc[7]

    print(str(year) + ": " + str(variazione_perc(media, agosto)))

# Incremento rispetto alla media
# 2010: 63.75
# 2011: 60.49
# 2012: 45.93
# 2013: 51.82
# 
# Invece per Luglio?
# 2010: 101.72
# 2011: 54.6  
# 2012: 75.97 
# 2013: 116.37



