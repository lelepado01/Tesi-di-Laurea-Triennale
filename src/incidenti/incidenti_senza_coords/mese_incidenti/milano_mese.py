
import pandas as pd
import matplotlib.pyplot as plt

path = "dataset/incidenti/incidenti_2013.txt"
data = pd.read_csv(path, sep="\t")

milano_mese = data[data['provincia'] == 15]['mese'].value_counts().sort_index()

index = 0
for giorni_in_mese in [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]:
    milano_mese.iloc[index] /= giorni_in_mese
    index += 1

media = milano_mese.mean()

color_ls = ['#928ace']*12
color_ls[7] = '#5747d1'

plt.xlabel("Mese")
plt.ylabel("Incidenti al giorno (2013)")
plt.plot([-1, 100], [media, media], color='#c0d147', label='Media')
plt.text(11.7,media - 0.1,'Media')
milano_mese.plot.bar(width=0.8, color=color_ls)
plt.show()

# Quanto scendono gli incidenti in Agosto (Numericamente) 
# Lo faccio per ogni anno

agosto = milano_mese.iloc[7]

def variazione_perc(x : float, y : float) -> float: 
    return (y / x) * 100 -100

var_2010 = variazione_perc(media, agosto)
#print(var_2010) = 47.4%

# Sono incidenti al giorno, se guardo incidenti al mese?
#print(variazione_perc(media, agosto)) = -1.56

# Invece rispetto a luglio e settembre?

#print(variazione_perc(milano_mese.iloc[6], agosto)) = -50.4%
#print(variazione_perc(agosto, milano_mese.iloc[8])) = 95.7%

# Vale per tutti gli anni?

# path = "dataset/incidenti/incidenti_"
# for year in range(2011, 2014):
#     dati = pd.read_csv(path + str(year) + ".txt", sep='\t', encoding='latin1')
#     milano_mese = dati[dati['provincia'] == 15]['mese'].value_counts().sort_index()

#     index = 0
#     for giorni_in_mese in [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]:
#         milano_mese.iloc[index] /= giorni_in_mese
#         index += 1

#     media = milano_mese.mean()
#     agosto = milano_mese.iloc[7]

#     print(str(year) + ": " + str(variazione_perc(media, agosto)))

# 2011: -35.14
# 2012: -45.46
# 2013: -41.37

# Gli altri anni non hanno più il mese dell'incidente, solo il trimestre

