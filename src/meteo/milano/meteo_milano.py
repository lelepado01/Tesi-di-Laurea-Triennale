
import pandas as pd
import matplotlib.pyplot as plt
import sys
sys.path.append("src")

import meteo.meteo_generale_utils as mgu

incidenti = pd.read_csv("dataset/incidenti/incidenti_2010.txt", sep="\t")

inc = pd.Series()
for m in incidenti['mese'].unique(): 
    inc = inc.append(pd.Series(len(incidenti[incidenti['mese'] == m]), index=[m]))

meteo = pd.read_csv("dataset/meteo/meteo_milano_generale_2008_2019.csv")
meteo_2010 = mgu.get_weather_by_year(meteo, 2010)

meteo_per_mese = pd.Series() 
for month in range(1,13): 
    media = mgu.get_weather_by_month(meteo_2010, month)['Dew_Point'].mean()
    meteo_per_mese = meteo_per_mese.append(pd.Series(media, index=[month]))


# inc = inc / inc.sum()
# meteo_per_mese = meteo_per_mese / meteo_per_mese.sum()
print(inc.corr(meteo_per_mese))
# Temp - Inc = 0.76
# WindSpeed - Inc = 0.64
# Humidity - Inc = -0.60
# Temp - Inc = 0.76

inc = inc.sort_index()
meteo_per_mese = meteo_per_mese.sort_index()

ax = plt.subplot(121)
ax.bar(inc.index, inc, color='#8f6ab5')
plt.ylabel("Incidenti per mese (2010)")
plt.xticks(range(1,13))
# ax.spines['right'].set_visible(False)
# ax.spines['top'].set_visible(False)

plt.subplot(122)
plt.ylabel("Temperatura media per mese (°C)")
plt.bar(meteo_per_mese.index, meteo_per_mese, color='#6ab58f')
plt.xticks(range(1,13))
plt.show()