import pandas as pd
import matplotlib.pyplot as plt

path = "dataset/incidenti/incidenti_2011.txt"
data = pd.read_csv(path, sep="\t")

milano_mese = data[data['provincia'] == 15]['mese'].value_counts().sort_index()
rimini_mese = data[data['provincia'] == 99]['mese'].value_counts().sort_index()
palermo_mese = data[data['provincia'] == 82]['mese'].value_counts().sort_index()

index = 0
for giorni_in_mese in [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]:
    rimini_mese.iloc[index] /= giorni_in_mese
    milano_mese.iloc[index] /= giorni_in_mese
    palermo_mese.iloc[index] /= giorni_in_mese
    index += 1

milano_media = milano_mese.mean()
rimini_media = rimini_mese.mean()
palermo_media = palermo_mese.mean()

plt.xlabel("Mese")
plt.ylabel("Incidenti al giorno (2011)")
plt.plot([-1, 15], [milano_media, milano_media], color='#f9f03b')
plt.plot([-1, 15], [rimini_media, rimini_media], color='#f9f03b')
plt.plot([-1, 15], [palermo_media, palermo_media], color='#f9f03b')
plt.text(11.8,milano_media - 0.1,'Media Milano')
plt.text(11.8,rimini_media - 0.1,'Media Rimini')
plt.text(11.8,palermo_media - 0.1,'Media Palermo')
milano_mese.plot.bar(width=0.9, color='#4566c1', alpha=1.0, label='Milano')
rimini_mese.plot.bar(width=0.9, color='#c14566', alpha=1.0, label='Rimini')
palermo_mese.plot.bar(width=0.9, color='#66c145', alpha=0.5, label='Palermo')
plt.legend()
plt.tight_layout()
plt.show()