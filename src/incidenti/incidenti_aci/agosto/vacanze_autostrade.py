
import pandas as pd
import matplotlib.pyplot as plt
import sys
sys.path.append('src')
import aci_utils
import heatmap as H

path = "dataset/incidenti/aci/autostrade/mesi_"

# Per ogni anno sono prese le cinque strade con più incidenti
incidenti_per_strada = pd.DataFrame()
for year in range(2011, 2019): 
    print("Processing: " + str(year))
    agosto_2018 = pd.read_csv(path + str(year)+".csv")
    agosto_2018 = agosto_2018[['NOME STRADA', 'Agosto']]
    agosto_2018 = aci_utils.sum_field_by_column(agosto_2018, 'NOME STRADA', 'Agosto')
    # Sono prese le cinque strade con maggior numero di incidenti 
    agosto_2018 = agosto_2018.sort_values(by='val', ascending=False).head(5)

    if year == 2011: 
        incidenti_per_strada = pd.DataFrame(agosto_2018.values, index=agosto_2018.index, columns=[str(year)])
    else: 
        incidenti_per_strada[str(year)] = agosto_2018
    
incidenti_per_strada = incidenti_per_strada.astype(int)

fig, ax = plt.subplots()
im, cbar = H.heatmap(incidenti_per_strada, incidenti_per_strada.index, incidenti_per_strada.columns, ax=ax, cmap="YlGn", cbarlabel="Incidenti all'anno")
texts = H.annotate_heatmap(im, valfmt="{x}")
fig.tight_layout()
plt.show()