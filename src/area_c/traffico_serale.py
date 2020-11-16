
import pandas as pd
import matplotlib.pyplot as plt
import datetime

data = pd.read_csv("dataset/area_c/orari_2016.csv", sep=';').dropna()

orari_serali = data[(data['hour'] == 23) | (data['hour'] == 24) |(data['hour'] == 0) | (data['hour'] == 1) | (data['hour'] == 2) | (data['hour'] == 3) | (data['hour'] == 4) | (data['hour'] == 5) | (data['hour'] == 6)]

def is_weekend(year, month, day) -> pd.Series: 
    s = pd.Series()

    for y, m, d in zip(year, month, day): 
        s = s.append(pd.Series(datetime.datetime(y, m, d).weekday() > 4), ignore_index=True)

    return s

# print(len(orari_serali))

weekend_days = orari_serali

weekend_days = orari_serali[is_weekend(orari_serali['year'], orari_serali['month'], orari_serali['day'])]

# print(weekend_days)

traffico = {}
for f in orari_serali['hour'].unique():
    traffico[f] = orari_serali[orari_serali['hour'] == f]['totale'].sum()

traffico = pd.DataFrame(traffico, index=['incidenti']).transpose()

traffico.plot.bar()
plt.show()