
import pandas as pd

tasso_turismo = pd.read_csv("dataset/turismo/tasso_turismo.csv", sep=';')
tasso_turismo.index = tasso_turismo['regione']
tasso_turismo.pop('regione')
mesi_non_estivi = tasso_turismo.transpose()

mesi_non_estivi = pd.read_csv("dataset/turismo/mesi_non_estivi.csv", sep=';')
mesi_non_estivi.index = mesi_non_estivi['regione']
mesi_non_estivi.pop('regione')
mesi_non_estivi = mesi_non_estivi.transpose()

montagna = ['Trentino', 'Valle d\'Aosta']
trent = tasso_turismo[tasso_turismo.index == montagna[0]]
aosta = tasso_turismo[tasso_turismo.index == montagna[1]]

mt = trent.transpose().mean()
ma = aosta.transpose().mean()

print((trent['2018'] - trent['2015']) / trent['2015'])
print((trent['2018'] - mt) / mt)

print((aosta['2018'] - aosta['2015']) / aosta['2015'])
print((aosta['2018'] - ma) / ma)