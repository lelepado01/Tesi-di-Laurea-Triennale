
import pandas as pd
import matplotlib.pyplot as plt

path = "dataset/incidenti/incidenti_2010.txt"

data = pd.read_csv(path, sep="\t")
#print(data['ora'].unique())

ora = data[data['ora'] < 25]['ora'].value_counts().sort_index()

# GRAFO 1
#ora.plot.bar()
#plt.show()

# Ho iniziato guardando il campo 'ora', tramite GRAFO 1, si nota che 
# il picco di incidenti durante l'anno si hanno tra le 17-19.
# Probabilmente perchè la gente inizia a uscire da lavoro, è possibile tentare 
# una verifica, guardando se il trend cambia in Agosto, quando la maggior 
# parte delle persone sono in vacanza

ora_in_agosto = data[(data['mese'] == 8) & (data['ora'] < 25)]['ora'].value_counts().sort_index()

# GRAFO 2
#ora_in_agosto.plot.bar()
#plt.show()

# Non sembra essere il caso, un altro modo per controllare è guardare solo 
# per sabato e domenica

ora_sabato_domenica = data[(data['giorno_settimana'] > 5) & (data['ora'] < 25)]['ora'].value_counts().sort_index()

# GRAFO 3
#ora_sabato_domenica.plot.bar()
#plt.show()

ora_domenica = data[(data['giorno_settimana'] == 7) & (data['ora'] < 25)]['ora'].value_counts().sort_index()

# GRAFO 4
#ora_domenica.plot.bar()
#plt.show()

# Provo a confrontare le ore 18 (di uscita) rispetto a tutti i giorni della settimana

ora_18 = data[data['ora'] == 18]['giorno_settimana'].value_counts().sort_index()

# GRAFO 5
#ora_18.plot.bar()
#plt.show()

# qui si nota i minori incidenti nel weekend, 
# ma questa discesa vale per tutte le fasce orarie?

ora_8 = data[data['ora'] == 8]['giorno_settimana'].value_counts().sort_index()
ora_11 = data[data['ora'] == 11]['giorno_settimana'].value_counts().sort_index()
ora_22 = data[data['ora'] == 22]['giorno_settimana'].value_counts().sort_index()

# GRAFO 6
#fasce_unite = pd.DataFrame([ora_8, ora_11, ora_18, ora_22], index=['8', '11', '18', '22']).transpose()
#fasce_unite.plot.bar()
#plt.show()

# Alle 8 ho una discesa simile, probabilmente per il traffico nella direzione opposta
# Alle 11 ho minore discesa, solo di Domenica
# Alle 22 non ho discesa di incidenti nei weekend (probabilmente per il traffico serale)

# Un'altra cosa che posso controllare è quanto influisce il numero di 
# incidenti dovuti alle escite del sabato sera

ore_notte = data[((data['ora'] > 21) & (data['ora'] != 25)) | (data['ora'] < 4)][['giorno_settimana', 'ora']]
sabato = ore_notte[ore_notte['giorno_settimana'] == 6]['ora'].value_counts().sort_index()

# Scelgo mercoledi per fare il confronto con sabato, 
# volendo potrei utilizzare tutti i giorni settimanali e fare normalize = True: 

#settimana = ore_notte[ore_notte['giorno_settimana'] < 6]['ora'].value_counts(normalize=True).sort_index()
mercoledi = ore_notte[ore_notte['giorno_settimana'] == 3]['ora'].value_counts().sort_index()

# GRAFO 7
#settimana_e_sabato = pd.DataFrame([settimana, sabato], index=['settimana', 'sabato']).transpose()
mercoledi_e_sabato = pd.DataFrame([mercoledi, sabato], index=['mercoledi', 'sabato']).transpose()
mercoledi_e_sabato.plot.bar()
plt.show()

# Dal grafo si nota che sabato si hanno molti più incidenti nella fascia dell'[1, 2, 3], 
# mentre di mercoledi nella fascia delle 22

