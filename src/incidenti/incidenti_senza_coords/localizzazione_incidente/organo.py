
import pandas as pd
import matplotlib.pyplot as plt

path = "dataset/incidenti/incidenti_2011.txt"

data = pd.read_csv(path, sep="\t")
print((data['organo_di_rilevazione'] == data['organo_coordinatore']).unique())

# Non sembrano dati molto interessanti...