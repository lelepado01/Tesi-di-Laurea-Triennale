
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

weekend_days = orari_serali
week_days = orari_serali
days = is_weekend(orari_serali['year'], orari_serali['month'], orari_serali['day'])

weekend_days.index = range(0, len(weekend_days))
week_days.index = range(0, len(week_days))
i = 0
for d in days: 
    if not d: 
        weekend_days = weekend_days.drop(index=i)
    else: 
        week_days = week_days.drop(index=i)
    i+= 1

traffico = {}
for f in weekend_days['hour'].unique():
    traffico[f] = weekend_days[weekend_days['hour'] == f]['totale'].sum()

traffico_weekend = pd.DataFrame(traffico, index=['Traffico in weekend']).transpose()

traffico = {}
for f in weekend_days['hour'].unique():
    traffico[f] = week_days[week_days['hour'] == f]['totale'].sum()

traffico_week = pd.DataFrame(traffico, index=['Traffico in settimana']).transpose()


traffico_weekend /= 2 * 52
traffico_week /= 5 * 52

traffico_weekend = traffico_weekend.reindex([23,0,1,2,3,4,5,6])
traffico_week = traffico_week.reindex([23,0,1,2,3,4,5,6])


data = pd.read_csv("dataset/incidenti/istat/incidenti_2016.txt", sep="\t", encoding='latin1')
data = data[data['Ora'] != 25]

notte = data[(data['Ora'] < 7) | (data['Ora'] > 22)]
ora_notte_week = notte[notte['giorno'] < 6]['Ora'].value_counts().sort_index()
ora_notte_weekend = notte[notte['giorno'] > 5]['Ora'].value_counts().sort_index()

ora_notte_week = ora_notte_week.reindex([23,24,1,2,3,4,5,6])
ora_notte_weekend = ora_notte_weekend.reindex([23,24,1,2,3,4,5,6])

ora_notte_week /= 5 * 52 
ora_notte_weekend /= 2 * 52

ora_notte_week = ora_notte_week.rename(index={24:0})
ora_notte_weekend = ora_notte_weekend.rename(index={24:0})

traffico_week = pd.Series(traffico_week['Traffico in settimana'], index=traffico_week.index)
traffico_weekend = pd.Series(traffico_weekend['Traffico in weekend'], index=traffico_weekend.index)

ora_notte_week /= traffico_week
ora_notte_weekend /= traffico_weekend

pd.DataFrame(
    [ora_notte_week, ora_notte_weekend], 
    ['Week', 'Weekend']
).transpose().plot.bar(color=['#d1d162', '#6262d1'], width=0.9)

plt.xlabel("Principali ore della notte")
plt.ylabel("Rapporto tra incidenti e traffico")
plt.legend(['week', 'weekend'])
plt.xticks(rotation=0)

plt.show()