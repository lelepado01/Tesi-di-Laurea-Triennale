
import geopandas as gp
import pandas as pd
import matplotlib.pyplot as plt
import sys
sys.path.append('src')
import heatmap as H
import aci_utils

path = "dataset/regioni/regioni.geojson"
regioni = gp.read_file(path)

incidenti_2011 = aci_utils.get_sum_of_fields(pd.read_csv('dataset/incidenti/aci/autostrade/mesi_2011.csv'), 'REGIONE', 'TOTALE').sort_values('REGIONE',inplace=False, ascending=True)
incidenti_2012 = aci_utils.get_sum_of_fields(pd.read_csv('dataset/incidenti/aci/autostrade/mesi_2012.csv'), 'REGIONE', 'TOTALE').sort_values('REGIONE',inplace=False, ascending=True)
incidenti_2013 = aci_utils.get_sum_of_fields(pd.read_csv('dataset/incidenti/aci/autostrade/mesi_2013.csv'), 'REGIONE', 'TOTALE').sort_values('REGIONE',inplace=False, ascending=True)
incidenti_2014 = aci_utils.get_sum_of_fields(pd.read_csv('dataset/incidenti/aci/autostrade/mesi_2014.csv'), 'REGIONE', 'TOTALE').sort_values('REGIONE',inplace=False, ascending=True)
incidenti_2015 = aci_utils.get_sum_of_fields(pd.read_csv('dataset/incidenti/aci/autostrade/mesi_2015.csv'), 'REGIONE', 'TOTALE').sort_values('REGIONE',inplace=False, ascending=True)
incidenti_2016 = aci_utils.get_sum_of_fields(pd.read_csv('dataset/incidenti/aci/autostrade/mesi_2016.csv'), 'REGIONE', 'TOTALE').sort_values('REGIONE',inplace=False, ascending=True)
incidenti_2017 = aci_utils.get_sum_of_fields(pd.read_csv('dataset/incidenti/aci/autostrade/mesi_2017.csv'), 'REGIONE', 'TOTALE').sort_values('REGIONE',inplace=False, ascending=True)
incidenti_2018 = aci_utils.get_sum_of_fields(pd.read_csv('dataset/incidenti/aci/autostrade/mesi_2018.csv'), 'REGIONE', 'TOTALE').sort_values('REGIONE',inplace=False, ascending=True)

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
