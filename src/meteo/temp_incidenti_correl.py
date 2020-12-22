
import pandas as pd
import sys
sys.path.append("src")
import meteo.meteo_generale_utils as mgu

meteo = pd.read_csv("dataset/meteo/meteo_milano_generale_2008_2019.csv")

for year in [2010, 2011, 2012, 2013]: 
    meteo_2010 = mgu.get_weather_by_year(meteo, 2013)

    meteo_per_mese = pd.Series() 
    for month in range(1,13): 
        media = mgu.get_weather_by_month(meteo_2010, month)['Humidity'].mean()
        meteo_per_mese = meteo_per_mese.append(pd.Series(media, index=[month]))

    incidenti = pd.read_csv("dataset/incidenti/istat/incidenti_" + str(year) +".txt", sep="\t")

    inc = pd.Series()
    for m in incidenti['mese'].unique(): 
        inc = inc.append(pd.Series(len(incidenti[incidenti['mese'] == m]), index=[m]))

    print(str(year) + ": " + str(meteo_per_mese.corr(inc)))


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