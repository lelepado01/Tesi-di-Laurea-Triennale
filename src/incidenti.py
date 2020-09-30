
import pandas as pd
import matplotlib.pyplot as plt

file_path = "dataset/incidenti/incidenti_2010.txt"
data = pd.read_csv(file_path, sep='\t', decimal='.')

incidenti_per_mese = data['mese'].value_counts()

#plt.plot(incidenti_per_mese.sort_index())
#plt.show()
loc = data['denominazione_della_strada'].value_counts()
loc = loc[loc < 400][loc > 20]
print(loc)

loc.plot.bar()
plt.show()