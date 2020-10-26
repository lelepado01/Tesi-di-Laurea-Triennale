
import pandas as pd
import matplotlib.pyplot as plt

path = "dataset/incidenti/incidenti_2010.txt"
data = pd.read_csv(path, sep="\t")

milano_mese = data[data['provincia'] == 15]['mese'].value_counts().sort_index()

index = 0
for giorni_in_mese in [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]:
    milano_mese.iloc[index] /= giorni_in_mese
    index += 1

media = milano_mese.mean()

plt.xlabel("Mese")
plt.ylabel("Incidenti al mese (2010)")

plt.plot([-1, 100], [media, media], color='#e85929', label='Media')
plt.text(11.7,media - 0.1,'Media')

milano_mese.plot.bar(width=0.8, color='#e8b829')
plt.show()