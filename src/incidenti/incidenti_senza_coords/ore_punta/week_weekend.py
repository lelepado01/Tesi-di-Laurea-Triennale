
import pandas as pd
import matplotlib.pyplot as plt

path = "dataset/incidenti/incidenti_2018.txt"

data = pd.read_csv(path, sep="\t")
data = data[data['Ora'] != 25]

ora_weekend = data[data['giorno'] > 5]['Ora'].value_counts().sort_index()
ora_week = data[data['giorno'] < 6]['Ora'].value_counts().sort_index()

ora_week /= 5 * 52
ora_weekend /= 2 * 52

ora_week.plot(color='#d5ef5f', alpha=0.5, label="Week")
ora_weekend.plot(color='#7057e0', alpha=0.5, label="Weekend")
plt.xlabel("Orario")
plt.ylabel("Numero di incidenti per giorno (2018)")
plt.legend()
plt.fill_between(ora_week.index, ora_week, color='#d5ef5f', alpha=0.5)
plt.fill_between(ora_weekend.index, ora_weekend, color='#7057e0', alpha=0.5)
plt.show()

# print((ora_week[9] / ora_week.mean()) * 100 -100)
# print((ora_weekend[9] / ora_weekend.mean()) * 100 -100)

# domenica = data[data['giorno_settimana'] == 6]['ora'].value_counts().sort_index()

# print((domenica[18] / domenica.mean()) * 100 -100)