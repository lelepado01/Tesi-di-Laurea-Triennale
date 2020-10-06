
import pandas as pd
import matplotlib.pyplot as plt

meteo = pd.read_csv("dataset/meteo/meteo_milano_generale_2008_2019.csv", sep=",")

meteo_2010 = meteo[meteo['Date_Time'].map(lambda x : x.split(' ')[0].split('/')[2] == "2010")]
meteo_2011 = meteo[meteo['Date_Time'].map(lambda x : x.split(' ')[0].split('/')[2] == "2011")]
meteo_2012 = meteo[meteo['Date_Time'].map(lambda x : x.split(' ')[0].split('/')[2] == "2012")]
meteo_2013 = meteo[meteo['Date_Time'].map(lambda x : x.split(' ')[0].split('/')[2] == "2013")]
meteo_2014 = meteo[meteo['Date_Time'].map(lambda x : x.split(' ')[0].split('/')[2] == "2014")]
meteo_2015 = meteo[meteo['Date_Time'].map(lambda x : x.split(' ')[0].split('/')[2] == "2015")]
meteo_2016 = meteo[meteo['Date_Time'].map(lambda x : x.split(' ')[0].split('/')[2] == "2016")]
meteo_2017 = meteo[meteo['Date_Time'].map(lambda x : x.split(' ')[0].split('/')[2] == "2017")]
meteo_2018 = meteo[meteo['Date_Time'].map(lambda x : x.split(' ')[0].split('/')[2] == "2018")]

#meteo_2010['Temperature'].value_counts().sort_index().plot()
#plt.show()
#meteo_2011['Temperature'].value_counts().sort_index().plot()
#plt.show()
#meteo_2012['Temperature'].value_counts().sort_index().plot()
#plt.show()
#meteo_2013['Temperature'].value_counts().sort_index().plot()
#plt.show()
#meteo_2014['Temperature'].value_counts().sort_index().plot()
#plt.show()
#meteo_2015['Temperature'].value_counts().sort_index().plot()
#plt.show()
#meteo_2016['Temperature'].value_counts().sort_index().plot()
#plt.show()
#meteo_2017['Temperature'].value_counts().sort_index().plot()
#plt.show()
#meteo_2018['Temperature'].value_counts().sort_index().plot()
#plt.show()

wind = meteo_2010['Wind_Speed'].value_counts().sort_index()
print(meteo_2010['Wind_Speed'].var())
#wind.plot()
#plt.show()

# TODO: questo può essere utile con i dataset degli incidenti