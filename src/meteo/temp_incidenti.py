
import pandas as pd
import matplotlib.pyplot as plt
import sys
sys.path.append("src")

import meteo.meteo_generale_utils as mgu

incidenti = pd.read_csv("dataset/incidenti/incidenti_2013.txt", sep="\t")

inc = pd.Series()
for m in incidenti['mese'].unique(): 
    inc = inc.append(pd.Series(len(incidenti[incidenti['mese'] == m]), index=[m]))

meteo = pd.read_csv("dataset/meteo/meteo_milano_generale_2008_2019.csv")
meteo_2010 = mgu.get_weather_by_year(meteo, 2011)

meteo_per_mese = pd.Series() 
for month in range(1,13): 
    media = mgu.get_weather_by_month(meteo_2010, month)['Temperature'].mean()
    meteo_per_mese = meteo_per_mese.append(pd.Series(media, index=[month]))

umid = pd.Series() 
for month in range(1,13): 
    media = mgu.get_weather_by_month(meteo_2010, month)['Humidity'].mean()
    umid = umid.append(pd.Series(media, index=[month]))



# inc = inc / inc.sum()
# meteo_per_mese = meteo_per_mese / meteo_per_mese.sum()

inc = inc.sort_index()
meteo_per_mese = meteo_per_mese.sort_index()

ax = plt.subplot(311)
ax.bar(inc.index, inc, color='#86ba5d', width=0.9)
plt.ylabel("Incidenti per mese (2011)")
plt.xticks(range(1,13))

plt.subplot(312)
plt.ylabel("Temperatura media (°C)")
plt.bar(meteo_per_mese.index, meteo_per_mese, color='#5d86ba', width=0.9)
plt.xticks(range(1,13))

plt.subplot(313)
plt.ylabel("Umidità media")
plt.bar(umid.index, umid, color='#ba5d86', width=0.9)
plt.xticks(range(1,13))
plt.show()

# for year in [2010, 2011, 2012, 2013]: 
#     meteo_2010 = mgu.get_weather_by_year(meteo, 2013)

#     meteo_per_mese = pd.Series() 
#     for month in range(1,13): 
#         media = mgu.get_weather_by_month(meteo_2010, month)['Humidity'].mean()
#         meteo_per_mese = meteo_per_mese.append(pd.Series(media, index=[month]))

#     incidenti = pd.read_csv("dataset/incidenti/incidenti_" + str(year) +".txt", sep="\t")

#     inc = pd.Series()
#     for m in incidenti['mese'].unique(): 
#         inc = inc.append(pd.Series(len(incidenti[incidenti['mese'] == m]), index=[m]))


#     # print(meteo_per_mese)
#     # print(inc)

#     print(str(year) + ": " + str(meteo_per_mese.corr(inc)))


# TEMP
# 2010: 0.768
# 2011: 0.900
# 2012: 0.732
# 2013: 0.658

# Wind Speed
# 2010: 0.585
# 2011: 0.626
# 2012: 0.501
# 2013: 0.465

# Humidity
# 2010: -0.626
# 2011: -0.730
# 2012: -0.609
# 2013: -0.516