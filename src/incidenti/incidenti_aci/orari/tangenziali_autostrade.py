
import matplotlib.pyplot as plt
import pandas as pd
import sys
sys.path.append("src")
import heatmap as H

def sum_columns(data : pd.DataFrame, normalize = False, name=None) -> pd.Series: 
    res = {}
    for col in data.columns: 
        res[col] = sum(data[col])

    if name is None:
        res = pd.Series(res).transpose()
    else: 
        res = pd.Series(res, name=name)

    if normalize: 
        res = res / sum(res)

    return res


data = pd.read_csv('dataset/incidenti/aci/autostrade/ore_2018.csv')
ore = ['01','02','03','04','05','06','07','08','09','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24']

milano = data[data['PROVINCIA'] == 'Milano']

incidenti = pd.DataFrame()
for field in milano['NOME STRADA'].unique(): 
    incidenti = incidenti.append(
        sum_columns(milano[milano['NOME STRADA'] == field][ore], name=field), 
    )


fields = [
    'A 01 -  Milano-Roma-Napoli (Autostrada del Sole)', 
    'A 04 -  Torino-Trieste',     
    'A 07 -  Milano-Genova',     
    'A 08 -  Milano-Varese (Autostrada dei Laghi)',
    'A 50 -  Tangenziale Ovest Milano',    
    'A 51 -  Tangenziale Est Milano',    
    'A 52 -  Tangenziale Nord Milano'
    ]  

incidenti = incidenti.drop(index='0')

incidenti_1 = pd.DataFrame()
for i in [0, 2,3, 5,9,10,11]:
    incidenti_1 = incidenti_1.append(incidenti.iloc[i])

fig, ax = plt.subplots()

im, cbar = H.heatmap(
    incidenti_1, 
    incidenti_1.index, 
    range(0,24), 
    ax=ax, 
    cmap="YlGn", 
    cbarlabel="Incidenti per autostrada (2018)")

plt.show()