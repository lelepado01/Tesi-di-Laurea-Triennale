
import pandas as pd
import matplotlib.pyplot as plt

mesi = ["Gennaio","Febbraio","Marzo","Aprile","Maggio","Giugno","Luglio","Agosto","Settembre","Ottobre","Novembre","Dicembre"]

path = "dataset/area_c/orari_2012.csv"
data = pd.read_csv(path, sep=';')

ingressi_area_c = pd.Series()
for f in data['month'].unique():
    ingressi_area_c = ingressi_area_c.append(
        pd.Series(data[data['month'] == f]['totale'].sum()), 
        ignore_index=True)


incidenti = pd.read_csv("dataset/incidenti/istat/incidenti_2012.txt", sep='\t')
mesi_incidenti = incidenti['mese'].value_counts().sort_index()

# Normalizzazione di accessi a area c per orario tra 0 e 1
ingressi_area_c.index = range(1,13)
perc_traffico = ingressi_area_c / ingressi_area_c.sum()

# Calcolo rapporto tra incidenti e traffico
rapp = mesi_incidenti / ingressi_area_c

# Colorazione del grafico per avere colonne più accentuate
color_ls = ['#dbad85']*12
color_ls[5:7] = ['#dd8d46']*3

plt.subplot(1,2,1)
plt.bar(perc_traffico.index, perc_traffico, color=color_ls, width=0.9)
plt.ylabel("Percentuale di traffico in Area C")
plt.xticks(range(1,13), mesi, rotation=90)
plt.tight_layout()

plt.subplot(1,2,2)
plt.fill_between(rapp.index, rapp, color='#9f66ad')
plt.xticks(range(1, 13), mesi, rotation=90)
plt.ylabel("Rapporto tra incidenti e traffico")
plt.tight_layout()
plt.show()
