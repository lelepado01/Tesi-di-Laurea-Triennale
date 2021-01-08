
import pandas as pd
import matplotlib.pyplot as plt

path = "dataset/incidenti/istat/incidenti_2013.txt"
data = pd.read_csv(path, sep="\t", encoding='latin1')

aosta_mese = data[data['provincia'] == 7]['mese'].value_counts().sort_index()

index = 0
for giorni_in_mese in [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]:
    aosta_mese.iloc[index] /= giorni_in_mese
    index += 1

media = aosta_mese.mean()

color_ls = ['#5747d1']*12

plt.xlabel("Mese")
plt.ylabel("Incidenti al giorno (2013)")
plt.plot([-1, 12], [media, media], color='#c0d147', label='Media')
plt.text(11.7,media-0.01,'Media')
aosta_mese.plot.bar(width=0.8, color=color_ls)
plt.show()

