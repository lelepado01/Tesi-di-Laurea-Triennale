
import pandas as pd
import matplotlib.pyplot as plt

import sys
sys.path.append('src')

import label_utils

data = pd.read_csv("dataset/incidenti/incidenti_2012.txt", sep="\t")
agosto = data[data['mese'] == 8]['provincia']
agosto_label = label_utils.join_labels(agosto, 'dataset/incidenti/Classificazioni/provincia.csv').value_counts().head(10)
#agosto_label = agosto_label / agosto_label.sum()

# print(agosto_label)
mesi = label_utils.join_labels(data['provincia'], 'dataset/incidenti/Classificazioni/provincia.csv').value_counts().head(10)
#mesi = mesi / mesi.sum()
# print(mesi.head(10))

agosto_ls = ['#8bc1c4']*12
agosto_ls[:4] = ['#5bc1c6']*4

mesi_ls = ['#8fc1ab']*12
mesi_ls[:2] = ['#5bc696']*2
mesi_ls[7] = '#5bc696'
mesi_ls[9] = '#5bc696'

plt.subplot(2,1,1)
agosto_label.plot.bar(width=0.9, color=agosto_ls)
plt.ylabel("Incidenti in Agosto (2011)")
plt.tight_layout()
plt.subplot(2,1,2)
mesi.plot.bar(width=0.9, color=mesi_ls)
plt.ylabel("Incidenti all'anno (2011)")
plt.tight_layout()
plt.show()