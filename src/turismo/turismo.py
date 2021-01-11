
import pandas as pd
import matplotlib.pyplot as plt

tasso_turismo = pd.read_csv("dataset/turismo/tasso_turismo.csv", sep=';')
tasso_turismo.index = tasso_turismo['regione']
tasso_turismo.pop('regione')
tasso_turismo = tasso_turismo.transpose()

mesi_non_estivi = pd.read_csv("dataset/turismo/mesi_non_estivi.csv", sep=';')
mesi_non_estivi.index = mesi_non_estivi['regione']
mesi_non_estivi.pop('regione')
mesi_non_estivi = mesi_non_estivi.transpose()

regioni = ['Sicilia', 'Toscana', 'Trentino', 'Sardegna', 'Liguria', 'Valle d\'Aosta', 'Lombardia']

plt.subplot(1,2,1)
index_1 = mesi_non_estivi[regioni]
plt.plot(index_1)
plt.ylabel("Turismo in mesi non estivi")
plt.xticks(range(0,21,2), rotation = 90)

plt.subplot(1,2,2)
index_2 = tasso_turismo[regioni]
plt.plot(index_2)
plt.ylabel("Tasso Turisticità")
plt.legend(regioni, bbox_to_anchor=(1,1), loc="upper left")
plt.xticks(range(0,23,2), rotation = 90)
plt.show()

