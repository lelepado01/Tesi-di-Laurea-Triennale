
import pandas as pd
import matplotlib.pyplot as plt

giorni_al_mese = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
giorni_al_trimestre = [31 +28+ 31, 30+ 31+30, 31+ 31+ 30, 31+ 30+ 31]

incidenti_2010 = pd.read_csv("dataset/incidenti/istat/incidenti_2010.txt", sep="\t")
incidenti_2011 = pd.read_csv("dataset/incidenti/istat/incidenti_2011.txt", sep="\t")
incidenti_2012 = pd.read_csv("dataset/incidenti/istat/incidenti_2012.txt", sep="\t")
incidenti_2013 = pd.read_csv("dataset/incidenti/istat/incidenti_2013.txt", sep="\t")
incidenti_2014 = pd.read_csv("dataset/incidenti/istat/incidenti_2014.txt", sep="\t")
incidenti_2015 = pd.read_csv("dataset/incidenti/istat/incidenti_2015.txt", sep="\t", encoding='latin1')
incidenti_2016 = pd.read_csv("dataset/incidenti/istat/incidenti_2016.txt", sep="\t", encoding='latin1')
incidenti_2017 = pd.read_csv("dataset/incidenti/istat/incidenti_2017.txt", sep="\t", error_bad_lines=False, engine="python")
incidenti_2018 = pd.read_csv("dataset/incidenti/istat/incidenti_2018.txt", sep="\t", encoding='latin1')

def get_trimestre(data : pd.Series) -> pd.Series: 
    res = {
        1 : data.transpose()[0:3].sum(), 
        2 : data.transpose()[3:6].sum(), 
        3 : data.transpose()[6:9].sum(), 
        4 : data.transpose()[9:13].sum()
        }

    return pd.Series(res.values(), res.keys())

def get_provincia(prov : int) -> pd.DataFrame: 
    aosta_2010 = get_trimestre(incidenti_2010[incidenti_2010['provincia'] == prov]['mese'].value_counts().sort_index())
    aosta_2011 = get_trimestre(incidenti_2011[incidenti_2011['provincia'] == prov]['mese'].value_counts().sort_index())
    aosta_2012 = get_trimestre(incidenti_2012[incidenti_2012['provincia'] == prov]['mese'].value_counts().sort_index())
    aosta_2013 = get_trimestre(incidenti_2013[incidenti_2013['provincia'] == prov]['mese'].value_counts().sort_index())
    aosta_2014 = incidenti_2014[incidenti_2014['provincia'] == prov]['trimestre'].value_counts().sort_index()
    aosta_2015 = incidenti_2015[incidenti_2015['provincia'] == prov]['trimestre'].value_counts().sort_index()
    aosta_2016 = incidenti_2016[incidenti_2016['provincia'] == prov]['trimestre'].value_counts().sort_index()
    aosta_2017 = incidenti_2017[incidenti_2017['provincia'] == prov]['trimestre'].value_counts().sort_index()
    aosta_2018 = incidenti_2018[incidenti_2018['provincia'] == prov]['trimestre'].value_counts().sort_index()

    return pd.DataFrame(
        [aosta_2010, aosta_2011, aosta_2012, aosta_2013, aosta_2014, aosta_2015, aosta_2016, aosta_2017, aosta_2018], 
        ['2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018']
        ).transpose()

# Milano
provs = get_provincia(15)

import sys
sys.path.append('src')
import heatmap as H

fig, ax = plt.subplots()

im, cbar = H.heatmap(provs, provs.index, range(2010, 2019), ax=ax, cmap="YlGn", cbarlabel="")

fig.tight_layout()
plt.ylabel("Trimestre", fontdict={'fontsize': 10})
plt.show()
