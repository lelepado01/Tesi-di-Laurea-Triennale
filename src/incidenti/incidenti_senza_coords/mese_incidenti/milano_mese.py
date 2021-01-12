
import pandas as pd
import matplotlib.pyplot as plt

path = "dataset/incidenti/istat/incidenti_2013.txt"
data = pd.read_csv(path, sep="\t")
milano_mese = data[data['provincia'] == 15]['mese'].value_counts().sort_index()

index = 0
for giorni_in_mese in [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]:
    milano_mese.iloc[index] /= giorni_in_mese
    index += 1

media = milano_mese.mean()

# Colore del grafo per evidenziare una colonna
color_ls = ['#928ace']*12
color_ls[7] = '#5747d1'

plt.xlabel("Mese")
plt.ylabel("Incidenti al giorno (2013)")
plt.plot([-1, 100], [media, media], color='#c0d147', label='Media')
plt.text(11.7,media - 0.1,'Media')
milano_mese.plot.bar(width=0.8, color=color_ls)
plt.show()
