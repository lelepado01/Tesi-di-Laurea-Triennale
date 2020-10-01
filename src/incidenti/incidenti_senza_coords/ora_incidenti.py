
import pandas as pd
import matplotlib.pyplot as plt

path = "dataset/incidenti/incidenti_2010.txt"

data = pd.read_csv(path, sep="\t")
#print(data['ora'].unique())

ora = data[data['ora'] < 25]['ora'].value_counts().sort_index()

# MAPPA 1
#ora.plot.bar()
#plt.show()

# Ho iniziato guardando il campo 'ora', tramite MAPPA 1, si nota che 
# il picco di incidenti durante l'anno si hanno tra le 17-19.
# Probabilmente perchè la gente inizia a uscire da lavoro, è possibile tentare 
# una verifica, guardando se il trend cambia in Agosto, quando la maggior 
# parte delle persone sono in vacanza

ora_in_agosto = data[(data['mese'] == 8) & (data['ora'] < 25)]['ora'].value_counts().sort_index()

# MAPPA 2
#ora_in_agosto.plot.bar()
#plt.show()

# Non sembra essere il caso, un altro modo per controllare è guardare solo 
# per sabato e domenica

ora_sabato_domenica = data[(data['giorno_settimana'] == 6) | (data['giorno_settimana'] == 7)]['ora'].value_counts().sort_index()

# MAPPA 3
#ora_sabato_domenica.plot.bar()
#plt.show()

ora_domenica = data[data['giorno_settimana'] == 7]['ora'].value_counts().sort_index()

# MAPPA 4
#ora_domenica.plot.bar()
#plt.show()

# Provo a confrontare le ore 18 (di uscita) rispetto a tutti i giorni della settimana

ora_18 = data[data['ora'] == 18]['giorno_settimana'].value_counts().sort_index()

# MAPPA 5
#ora_18.plot.bar()
#plt.show()

# qui si nota i minori incidenti nel weekend, 
# ma questa discesa vale per tutte le fasce orarie?

ora_8 = data[data['ora'] == 8]['giorno_settimana'].value_counts().sort_index()
ora_11 = data[data['ora'] == 11]['giorno_settimana'].value_counts().sort_index()
ora_22 = data[data['ora'] == 22]['giorno_settimana'].value_counts().sort_index()

#ora_8.plot.bar() # ancora più accentuato
#plt.show()

#ora_11.plot.bar() # sabato uguale ai giorni restanti della settimana
#plt.show()

#ora_22.plot.bar() # tutti i giorni uguali
#plt.show()