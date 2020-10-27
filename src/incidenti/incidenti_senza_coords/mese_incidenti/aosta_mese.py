
import pandas as pd
import matplotlib.pyplot as plt

path = "dataset/incidenti/incidenti_2010.txt"
data = pd.read_csv(path, sep="\t")

aosta_mese = data[data['provincia'] == 7]['mese'].value_counts().sort_index()

index = 0
for giorni_in_mese in [31, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]:
    aosta_mese.iloc[index] /= giorni_in_mese
    index += 1

media = aosta_mese.mean()

plt.xlabel("Mese")
plt.ylabel("Incidenti al giorno (2010)")
plt.plot([-1, 100], [media, media], color='#c0d147', label='Media')
plt.text(10.7,media-0.01,'Media')
aosta_mese.plot.bar(width=0.8, color='#5747d1')
plt.show()