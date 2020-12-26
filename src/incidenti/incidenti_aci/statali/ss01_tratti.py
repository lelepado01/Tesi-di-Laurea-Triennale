
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("dataset/incidenti/aci/autostrade/localizzazione_2018.csv")

ss1 = data[data['CODICE'] == 'SS00101']

def sum_fields(dataset : pd.DataFrame, select_field): 
    df = {}
    for d in dataset[select_field].unique(): 
        df[d] = [
            dataset[dataset[select_field] == d]['INC'].sum(), 
            dataset[dataset[select_field] == d]['FER'].sum(), 
            dataset[dataset[select_field] == d]['MOR'].sum()
            ]

    return pd.DataFrame(df, index=['INC', 'FER', 'MOR'])

ss1 = sum_fields(ss1, 'PROVINCIA').transpose()

ss1.plot.bar(width=0.9, color=['#4ea051', '#514ea0', '#a04e9d'])
plt.ylabel("Province attraversate dalla SS01")
plt.tight_layout()
plt.show()