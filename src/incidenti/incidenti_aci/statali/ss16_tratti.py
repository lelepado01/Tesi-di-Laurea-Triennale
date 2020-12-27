
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("dataset/incidenti/aci/autostrade/localizzazione_2018.csv")
ss16 = data[data['CODICE'] == 'SS01601']

def sum_fields(dataset : pd.DataFrame, select_field): 
    df = {}
    for d in dataset[select_field].unique(): 
        df[d] = [
            dataset[dataset[select_field] == d]['INC'].sum(), 
            dataset[dataset[select_field] == d]['FER'].sum()
            ]

    return pd.DataFrame(df, index=['Incidenti', 'Feriti'])

ss16 = sum_fields(ss16, 'PROVINCIA').transpose()

ss16.plot.bar(width=0.9, color=['#4ea051', '#514ea0'])
plt.ylabel("Province attraversate dalla SS16")
plt.tight_layout()
plt.show()