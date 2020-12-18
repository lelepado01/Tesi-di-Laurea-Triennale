
import pandas as pd
import matplotlib.pyplot as plt

import sys
sys.path.append('src')

import label_utils

data = pd.read_csv("dataset/incidenti/incidenti_2011.txt", sep="\t")
agosto = data[data['mese'] == 8]['provincia']
agosto_label = label_utils.join_labels(agosto, 'dataset/incidenti/Classificazioni/provincia.csv').value_counts().head(10)
#agosto_label = agosto_label / agosto_label.sum()

mesi = label_utils.join_labels(data['provincia'], 'dataset/incidenti/Classificazioni/provincia.csv').value_counts().head(10)
#mesi = mesi / mesi.sum()

agosto_ls = ['#6ac48f']*12
agosto_ls[:4] = ['#1dad59']*4

mesi_ls = ['#6a9ec4']*12
mesi_ls[:2] = ['#1d71ad']*2
mesi_ls[7] = '#1d71ad'
mesi_ls[9] = '#1d71ad'

plt.subplot(2,1,1)
agosto_label.plot.bar(width=0.9, color=agosto_ls)
plt.ylabel("Incidenti in Agosto (2011)")
plt.tight_layout()
plt.subplot(2,1,2)
mesi.plot.bar(width=0.9, color=mesi_ls)
plt.ylabel("Incidenti all'anno (2011)")
plt.tight_layout()
plt.show()