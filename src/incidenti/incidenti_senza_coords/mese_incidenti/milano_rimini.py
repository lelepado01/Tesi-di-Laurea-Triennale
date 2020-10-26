
import pandas as pd
import matplotlib.pyplot as plt

path = "dataset/incidenti/incidenti_2010.txt"
data = pd.read_csv(path, sep="\t")

milano_mese = data[data['provincia'] == 15]['mese'].value_counts().sort_index()
rimini_mese = data[data['provincia'] == 99]['mese'].value_counts().sort_index()

index = 0
for giorni_in_mese in [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]:
    rimini_mese.iloc[index] /= giorni_in_mese
    milano_mese.iloc[index] /= giorni_in_mese
    index += 1

milano_media = milano_mese.mean()
rimini_media = rimini_mese.mean()

plt.xlabel("Mese")
plt.ylabel("Incidenti al mese (2010)")
plt.plot([-1, 15], [milano_media, milano_media], color='#c0d147', label='Media Milano')
plt.plot([-1, 15], [rimini_media, rimini_media], color='#c0d147', label='Media Rimini')
plt.text(11.7,milano_media - 0.1,'Milano Media')
plt.text(11.7,rimini_media - 0.1,'Rimini Media')
milano_mese.plot.bar(width=0.8, color='#5747d1')
rimini_mese.plot.bar(width=0.8, color='#d15747')
plt.tight_layout()
plt.show()