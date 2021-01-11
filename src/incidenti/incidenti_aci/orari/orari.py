
import matplotlib.pyplot as plt
import pandas as pd
import sys
sys.path.append("src")
import aci_utils

data = pd.read_csv('dataset/incidenti/aci/autostrade/ore_2018.csv')
ore = ['01','02','03','04','05','06','07','08','09','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24']

raccordo = data[data['CODICE'] == 'AA09001']
ss16 = data[data['CODICE'] == 'SS01601']
ss16 = ss16[ss16['PROVINCIA'] == 'Bari']

ss1 = data[data['CODICE'] == 'SS00101']
ss1 = ss1[ss1['PROVINCIA'] == 'Genova']

raccordo = aci_utils.sum_columns(raccordo[ore])
ss16 = aci_utils.sum_columns(ss16[ore])
ss1 = aci_utils.sum_columns(ss1[ore])

plt.subplot(3,1,1)
raccordo.plot.bar(color='#d888b3', width=0.9)
plt.ylabel("Raccordo Anulare\nRoma")
plt.xticks(range(0,25,2), rotation=0)
plt.tight_layout()

plt.subplot(3,1,2)
ss16.plot.bar(color='#88b3d8', width=0.9)
plt.ylabel("SS16\nprovincia di Bari")
plt.xticks(range(0,25,2),rotation=0)
plt.tight_layout()

plt.subplot(3,1,3)
ss1.plot.bar(color='#b3d888', width=0.9)
plt.ylabel("SS1\nprovincia di Genova")
plt.xticks(range(0,25,2),rotation=0)
plt.tight_layout()
plt.show()