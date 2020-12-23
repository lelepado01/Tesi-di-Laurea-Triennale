
import pandas as pd
import matplotlib.pyplot as plt

campi = ['veicolo__a___sesso_conducente', 'veicolo__a___et__passegger12']
campi_2 = ['veicolo__a___sesso_conducente', 'veicolo__a___sesso_passegg37']

df = pd.DataFrame()
for year in range(2010, 2019):
    l = 0
    if year < 2014:
        data = pd.read_csv("dataset/incidenti/istat/incidenti_" + str(year) +".txt", sep='\t')
        l = len(data)
        data = data[(data[campi[0]] != '  ') & (data[campi[0]] != ' ')]
        data = data[(data[campi[1]] == '  ') | (data[campi[1]] == ' ')]
    elif year != 2017: 
        data = pd.read_csv("dataset/incidenti/istat/incidenti_" + str(year) +".txt", sep='\t', encoding='latin1')[campi_2]
        l = len(data)
        data = data[data[campi_2[0]] != " "]
        data = data[data[campi_2[1]] == " "]
    else: 
        continue

    df = df.append(pd.DataFrame([year, len(data), l], index=['anno', 'numero', 'sample_size']).transpose(), ignore_index=True)

i = [*range(2010, 2019)]
i.remove(2017)
df.index = i

df['numero'].plot(label='Incidenti con solo conducente', color='#4bccc9')
df['sample_size'].plot(label='Incidenti totali', color='#4b8dcc')
plt.fill_between(df['sample_size'].index, df['sample_size'], color='#4b8dcc')
plt.fill_between(df['numero'].index, df['numero'], color='#4bccc9')
plt.xlabel("Anno")
plt.ylabel("Numero di Incidenti")
plt.legend(loc='lower right')
plt.tight_layout()
plt.show()