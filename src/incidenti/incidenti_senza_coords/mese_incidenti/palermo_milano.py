import pandas as pd
import matplotlib.pyplot as plt

path = "dataset/incidenti/istat/incidenti_2013.txt"
data = pd.read_csv(path, sep="\t")

# Selezione dati per Milano(15) e Palermo (82)
milano_mese = data[data['provincia'] == 15]['mese'].value_counts().sort_index()
palermo_mese = data[data['provincia'] == 82]['mese'].value_counts().sort_index()

index = 0
for giorni_in_mese in [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]:
    milano_mese.iloc[index] /= giorni_in_mese
    palermo_mese.iloc[index] /= giorni_in_mese
    index += 1

milano_media = milano_mese.mean()
palermo_media = palermo_mese.mean()

pd.DataFrame([milano_mese, palermo_mese], ['Milano', 'Palermo']).transpose().plot.bar(
    width = 0.9, 
    color = {'Milano': '#4566c1', 'Palermo': '#66c145'}
)

plt.ylabel("Incidenti al giorno (2013)")
plt.xticks(range(0,12), ["Gennaio","Febbraio","Marzo","Aprile","Maggio","Giugno","Luglio","Agosto","Settembre","Ottobre","Novembre","Dicembre"])
plt.plot([-1, 15], [milano_media, milano_media], color='#f9f03b')
plt.plot([-1, 15], [palermo_media, palermo_media], color='#f9f03b')
plt.text(11.8,milano_media - 0.1,'Media Milano')
plt.text(11.8,palermo_media - 0.1,'Media Palermo')
plt.legend()
plt.tight_layout()
plt.show()