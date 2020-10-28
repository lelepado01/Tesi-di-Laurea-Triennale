
import pandas as pd
import matplotlib.pyplot as plt
import sys 
sys.path.append("src/")

import label_utils

path = "dataset/incidenti/incidenti_2011.txt"
data : pd.DataFrame = pd.read_csv(path, sep="\t")

def count_people(row, campi) -> int: 
    count = 0
    if row[campi[0]] != '  ' and row[campi[0]] != ' ':  
        if row[campi[1]] == '  ' or row[campi[1]] == ' ':
            count += 1

    return count

def get_people_in_vehicles(dataset : pd.DataFrame, fields): 
    res = {}
    for index in range(0, len(dataset)): 
        res[index] = 0

    for index, row in dataset.iterrows(): 
        res[index] = count_people(row, fields)

    return pd.Series(res)

campi = ['veicolo__a___sesso_conducente', 'veicolo__a___et__passegger12']
campi_2 = ['veicolo__a___sesso_conducente', 'veicolo__a___sesso_passegg37']

#passeggeri_2010 = get_people_in_vehicles(pd.read_csv("dataset/incidenti/incidenti_2010.txt", sep="\t"), campi).value_counts()
#print("Caricato 2010")
#passeggeri_2011 = get_people_in_vehicles(pd.read_csv("dataset/incidenti/incidenti_2011.txt", sep="\t"), campi).value_counts()
#print("Caricato 2011")
#passeggeri_2012 = get_people_in_vehicles(pd.read_csv("dataset/incidenti/incidenti_2012.txt", sep="\t"), campi).value_counts()
#print("Caricato 2012")
#passeggeri_2013 = get_people_in_vehicles(pd.read_csv("dataset/incidenti/incidenti_2013.txt", sep="\t"), campi).value_counts()
#print("Caricato 2013")
#passeggeri_2014 = get_people_in_vehicles(pd.read_csv("dataset/incidenti/incidenti_2014.txt", sep="\t"), campi_2).value_counts()
#print("Caricato 2014")
#passeggeri_2015 = get_people_in_vehicles(pd.read_csv("dataset/incidenti/incidenti_2015.txt", sep="\t", encoding='latin1'), campi_2).value_counts()
#print("Caricato 2015")
#passeggeri_2016 = get_people_in_vehicles(pd.read_csv("dataset/incidenti/incidenti_2016.txt", sep="\t", encoding='latin1'), campi_2).value_counts()
#print("Caricato 2016")

#df = pd.DataFrame([
#    #passeggeri_2010.iloc[0],
#    #passeggeri_2011.iloc[0],
#    #passeggeri_2012.iloc[0],
#    #passeggeri_2013.iloc[0],
#    passeggeri_2014.iloc[0],
#    passeggeri_2015.iloc[0],
#    passeggeri_2016.iloc[0]
#], index=[
#    #"passeggeri_2010",
#    #"passeggeri_2011",
#    #"passeggeri_2012",
#    #"passeggeri_2013",
#    "passeggeri_2014",
#    "passeggeri_2015",
#    "passeggeri_2016"
#])
#
#print(df)
#
#df.plot()
#plt.show()


df = pd.DataFrame()

for year in range(2010, 2019):
    l = 0
    if year < 2014:
        data = pd.read_csv("dataset/incidenti/incidenti_" + str(year) +".txt", sep='\t')
        l = len(data)
        data = data[(data[campi[0]] != '  ') & (data[campi[0]] != ' ')]
        data = data[(data[campi[1]] == '  ') | (data[campi[1]] == ' ')]
    elif year != 2017: 
        data = pd.read_csv("dataset/incidenti/incidenti_" + str(year) +".txt", sep='\t', encoding='latin1')[campi_2]
        l = len(data)
        data = data[data[campi_2[0]] != " "]
        data = data[data[campi_2[1]] == " "]
    else: 
        continue

    df = df.append(pd.DataFrame([year, len(data), l], index=['anno', 'numero', 'sample_size']).transpose(), ignore_index=True)

print(df)

df['numero'].plot()
df['sample_size'].plot()
plt.show()