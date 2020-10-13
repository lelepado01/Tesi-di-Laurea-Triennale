
# TODO: questo può essere utile con i dataset degli incidenti

import pandas as pd
import matplotlib.pyplot as plt
import sys

sys.path.append("src/meteo/")

import meteo_generale_utils as mgu

meteo = pd.read_csv("dataset/meteo/meteo_milano_generale_2008_2019.csv", sep=",")

meteo_2010 = mgu.get_weather_by_year(meteo, 2010)
print(meteo_2010.columns)

#meteo_2010['Temperature'].value_counts().sort_index().plot()
#plt.show()

#ora_temp = mgu.get_weather_by_year(meteo_2010, 2010)
#ora_temp = mgu.get_weather_by_month(ora_temp, 8)
#ora_temp = mgu.get_weather_by_day(ora_temp, 1)[['Date_Time', 'Temperature']]

#labels = ora_temp['Date_Time'].values
#keep = range(0, len(labels), 4)
#labels = [ora_temp['Date_Time'].values[y] for y in keep]
#print(labels)

#plt.plot(ora_temp['Temperature'])
#plt.show()

#for year in range(2008, 2018): 
#    ora_temp = mgu.get_weather_by_year(meteo, year)
#    ora_temp = mgu.get_weather_by_month(ora_temp, 8)
#    ora_temp = mgu.get_weather_by_day(ora_temp, 1)[['Date_Time', 'Temperature']]
#    plt.plot(mgu.get_hour(ora_temp), ora_temp['Temperature'])
#
#plt.show()

# Temperatura media in italia?
media = pd.Series()
for year in range(2008, 2019): 
    meteo_anno = mgu.get_weather_by_year(meteo, year)
    media_temp = meteo_anno['Humidity'].mean()
    media = media.append(pd.Series(media_temp, index=[year]))

#print(media)

media.plot.bar()
plt.show()

# La temperatura sembra rimanere stabile, anche se 2016, 2017, 2018 sono in crescita
# Anche la varianza della temperatura non sembra cambiare
# La velocità del vento media aumenta (?) è un errore?
# La varianza rimane costante