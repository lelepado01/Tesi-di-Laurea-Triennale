
import pandas as pd
import matplotlib.pyplot as plt
import sys
sys.path.append("src")
import label_utils

path = "dataset/incidenti/incidenti_"

for year in range(2010, 2019): 
    if year == 2017: 
        data = pd.read_csv(path + str(year) + ".txt", sep="\t",  error_bad_lines=False, engine='python')
    else: 
        data = pd.read_csv(path + str(year) + ".txt", sep="\t",  encoding="latin1")

    natura_incidente = data['natura_incidente']

    natura_incidente_labels = label_utils.join_labels(
        natura_incidente, 
        "dataset/incidenti/Classificazioni/natura_incidente.csv"
    ).value_counts(normalize=True).sort_values().tail(3)

    print(str(year) + "------------------------")
    print(natura_incidente_labels)


