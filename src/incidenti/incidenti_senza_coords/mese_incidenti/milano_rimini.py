
import pandas as pd
import matplotlib.pyplot as plt

mesi = ["Gennaio","Febbraio","Marzo","Aprile","Maggio","Giugno","Luglio","Agosto","Settembre","Ottobre","Novembre","Dicembre"]
path = "dataset/incidenti/istat/incidenti_2013.txt"
data = pd.read_csv(path, sep="\t")

# Selezione dati per Milano (15) e Rimini (99)
milano_mese = data[data['provincia'] == 15]['mese'].value_counts().sort_index()
rimini_mese = data[data['provincia'] == 99]['mese'].value_counts().sort_index()

index = 0
for giorni_in_mese in [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]:
    rimini_mese.iloc[index] /= giorni_in_mese
    milano_mese.iloc[index] /= giorni_in_mese
    index += 1

milano_media = milano_mese.mean()
rimini_media = rimini_mese.mean()

pd.DataFrame([milano_mese, rimini_mese], ['Milano', 'Rimini']).transpose().plot.bar(
    width = 0.9,
    color = {'Milano': '#4566c1', 'Rimini': '#d15747'}
)

plt.xlabel("")
plt.ylabel("Incidenti al giorno (2013)")
plt.xticks(range(0,12), mesi)
plt.plot([-1, 15], [milano_media, milano_media], color='#c0d147')
plt.plot([-1, 15], [rimini_media, rimini_media], color='#c0d147')
plt.text(11.8,milano_media - 0.1,'Media Milano')
plt.text(11.8,rimini_media - 0.1,'Media Rimini')
plt.legend(bbox_to_anchor=(1,1), loc="upper left")
plt.tight_layout()
plt.show()

