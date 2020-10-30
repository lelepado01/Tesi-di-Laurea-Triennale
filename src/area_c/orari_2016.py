
import pandas as pd
import matplotlib.pyplot as plt

path = "dataset/area_c/giorno_2015.csv"

data = pd.read_csv(path, sep=';')

# print(data['totale'].mean())

# Ho modificato il dataset per mostrare y;m;d separati
# Manca Novembre

# Agosto e DIcembre sono bassi, mancano dati?

print("Giorni in Agosto: " + str(len(data[data['month'] == 8])))
print("Giorni in Dicembre: " + str(len(data[data['month'] == 12])))

# print(data['month'].unique())
df = pd.Series()
for f in data['month'].unique():
    df = df.append(
        pd.Series(data[data['month'] == f]['totale'].sum()), 
        ignore_index=True
        )

print(df)

mesi = [
    'Gennaio',
    'Febbraio',
    'Marzo',
    'Aprile',
    'Maggio',
    'Giugno',
    'Luglio',
    'Agosto',
    'Settembre',
    'Ottobre',  # non c'è novembre
    'Dicembre'
]

df.plot.bar()
plt.xticks(range(0, 11), mesi)
plt.show()

# Ho metà dei giorni a dicembre, potrei raddoppiarli...
# Non ho dati a novembre, potrei stimare una media...

# TODO: usare