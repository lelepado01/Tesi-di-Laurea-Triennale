
import pandas as pd
import matplotlib.pyplot as plt

def sum_columns(data : pd.DataFrame, normalize = False) -> pd.Series: 
    res = {}
    for col in data.columns: 
        res[col] = sum(data[col])

    res = pd.Series(res).transpose()

    if normalize: 
        res = res / sum(res)

    return res


ore_2012 = pd.read_csv('/Users/gabrielepadovani/Desktop/Università/Tesi/dataset/incidenti/aci/autostrade/ore_2012.csv')
print(ore_2012.columns)
ore = sum_columns(ore_2012[['01','02','03','04','05','06','07','08','09','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24']])
ore.plot.bar()
plt.show()