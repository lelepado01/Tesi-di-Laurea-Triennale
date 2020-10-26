

import pandas as pd
import matplotlib.pyplot as plt

path = "dataset/incidenti/incidenti_2010.txt"

data = pd.read_csv(path, sep="\t")
data = data[data['ora'] != 25]

ora_punta_weekend = data[data['giorno_settimana'] > 5]['ora'].value_counts().sort_index()
ora_punta_week = data[data['giorno_settimana'] < 6]['ora'].value_counts().sort_index()

ora_punta_week.plot()
ora_punta_weekend.plot()