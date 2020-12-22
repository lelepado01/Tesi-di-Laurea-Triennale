
import pandas as pd
import matplotlib.pyplot as plt

# path = "dataset/incidenti/istat/incidenti_2013.txt"
# data = pd.read_csv(path, sep="\t", encoding='latin1')

# aosta_mese = data[data['provincia'] == 7]['mese'].value_counts().sort_index()

# index = 0
# for giorni_in_mese in [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]:
#     aosta_mese.iloc[index] /= giorni_in_mese
#     index += 1

# # print(aosta_mese)

# media = aosta_mese.mean()

# color_ls = ['#5747d1']*12
# # color_ls[0] = '#5747d1'7670a9
# # print(color_ls)

# plt.xlabel("Mese")
# plt.ylabel("Incidenti al giorno (2013)")
# plt.plot([-1, 12], [media, media], color='#c0d147', label='Media')
# plt.text(11.7,media-0.01,'Media')
# aosta_mese.plot.bar(width=0.8, color=color_ls)
# plt.show()


# Calcolo perc di incremento

def variazione_perc(x : float, y : float) -> float: 
    return (y / x) * 100 -100

path = "dataset/incidenti/istat/incidenti_"
years = []
for year in range(2010, 2014):
    dati = pd.read_csv(path + str(year) + ".txt", sep='\t')
    aosta_mese = dati[dati['provincia'] == 7]['mese'].value_counts().sort_index()

    ls = []
    if year == 2010: 
        ls = [31, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    else: 
        ls = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
    index = 0
    for giorni_in_mese in ls:
        aosta_mese.iloc[index] /= giorni_in_mese
        index += 1

    media = aosta_mese.mean()
    agosto = aosta_mese.iloc[7]

    years.append(str(year) + ": " + str(variazione_perc(media, agosto)))

print(years)

# Per aosta sembra che il campione di incidenti non sia abbastanza grande 
# (Agosto)
# 2010: -2.93 
# 2011: 124.0 
# 2012: 52.25 
# 2013: -15.21

# Per Gennaio?
# 2010: 78.48 
# 2011: -32.12
# 2012: -41.44
# 2013: -24.63

# Direi che il comportamento non  è consistente 
# (anche se a gennaio scende sempre, 2010 è outlier)