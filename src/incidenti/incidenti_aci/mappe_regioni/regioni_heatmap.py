
import geopandas as gp
import pandas as pd
import matplotlib.pyplot as plt
import sys
sys.path.append('src')
import heatmap as H

def get_sum_of_fields(data : pd.DataFrame, select_field : str, field_to_sum : str) -> pd.Series: 
    res = {}
    index = 0
    for reg in data[select_field].unique():
        res[index] = [reg, 0]
        index += 1

    index = 0
    for reg in data[select_field].unique():
        for row in data[data[select_field] == reg][field_to_sum]:
            res[index] = [res[index][0], res[index][1] + row]
        index += 1

    return pd.DataFrame(res, index=[select_field, field_to_sum]).transpose()


path = "dataset/regioni/regioni.geojson"
regioni = gp.read_file(path)

incidenti_2011 = get_sum_of_fields(pd.read_csv('dataset/incidenti/aci/autostrade/mesi_2011.csv'), 'REGIONE', 'TOTALE').sort_values('REGIONE',inplace=False, ascending=True)
incidenti_2012 = get_sum_of_fields(pd.read_csv('dataset/incidenti/aci/autostrade/mesi_2012.csv'), 'REGIONE', 'TOTALE').sort_values('REGIONE',inplace=False, ascending=True)
incidenti_2013 = get_sum_of_fields(pd.read_csv('dataset/incidenti/aci/autostrade/mesi_2013.csv'), 'REGIONE', 'TOTALE').sort_values('REGIONE',inplace=False, ascending=True)
incidenti_2014 = get_sum_of_fields(pd.read_csv('dataset/incidenti/aci/autostrade/mesi_2014.csv'), 'REGIONE', 'TOTALE').sort_values('REGIONE',inplace=False, ascending=True)
incidenti_2015 = get_sum_of_fields(pd.read_csv('dataset/incidenti/aci/autostrade/mesi_2015.csv'), 'REGIONE', 'TOTALE').sort_values('REGIONE',inplace=False, ascending=True)
incidenti_2016 = get_sum_of_fields(pd.read_csv('dataset/incidenti/aci/autostrade/mesi_2016.csv'), 'REGIONE', 'TOTALE').sort_values('REGIONE',inplace=False, ascending=True)
incidenti_2017 = get_sum_of_fields(pd.read_csv('dataset/incidenti/aci/autostrade/mesi_2017.csv'), 'REGIONE', 'TOTALE').sort_values('REGIONE',inplace=False, ascending=True)
incidenti_2018 = get_sum_of_fields(pd.read_csv('dataset/incidenti/aci/autostrade/mesi_2018.csv'), 'REGIONE', 'TOTALE').sort_values('REGIONE',inplace=False, ascending=True)

incidenti_2011.set_index(incidenti_2011['REGIONE'], inplace=True)
incidenti_2012.set_index(incidenti_2012['REGIONE'], inplace=True)
incidenti_2013.set_index(incidenti_2013['REGIONE'], inplace=True)
incidenti_2014.set_index(incidenti_2014['REGIONE'], inplace=True)
incidenti_2015.set_index(incidenti_2015['REGIONE'], inplace=True)
incidenti_2016.set_index(incidenti_2016['REGIONE'], inplace=True)
incidenti_2017.set_index(incidenti_2017['REGIONE'], inplace=True)
incidenti_2018.set_index(incidenti_2018['REGIONE'], inplace=True)

df = pd.DataFrame([
    incidenti_2011['TOTALE'],
    incidenti_2012['TOTALE'],
    incidenti_2013['TOTALE'],
    incidenti_2014['TOTALE'],
    incidenti_2015['TOTALE'],
    incidenti_2016['TOTALE'],
    incidenti_2017['TOTALE'],
    incidenti_2018['TOTALE']
], [2011,2012,2013, 2014,2015,2016,2017,2018]).transpose()

fig, ax = plt.subplots()
im, cbar = H.heatmap(df, df.index, [2011,2012,2013, 2014,2015,2016,2017,2018], ax=ax, cmap="YlGn", xticks_rotated=True, cbarlabel="Incidenti all'anno per regione")

plt.show()
