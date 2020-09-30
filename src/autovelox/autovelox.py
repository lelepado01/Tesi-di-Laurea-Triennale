
import geopandas as gp
import matplotlib.pyplot as plt

path = "tesi/Tesi/dataset/autovelox/autovelox_milano.geojson"

autovelox = gp.read_file(path)
#print(autovelox)
#print(len(autovelox))

# Il dataset contiene alcuni campi superflui
#   id e @id

# print(autovelox[autovelox['id'] != autovelox['@id']])
#   restituisce un dataframe vuoto (sono due colonne uguali)

# controllo se ci sono altri campi tutti uguali: 
for index in autovelox.columns: 
    print(str(index) + ":  " + str(len(autovelox[index].unique())))

# questi campi hanno tutti un solo valore != None

#print(autovelox['addr:housenumber'].unique())
#print(autovelox['addr:city'].unique())
#print(autovelox['addr:postcode'].unique())
#print(autovelox['addr:street'].unique())
#print(autovelox['description'].unique())
#print(autovelox['type'].unique())

# I due fix dicono che uno non ha posizione precisa, e l'altro misura solo gli accessi

#print(autovelox['fixme'].unique())
#print(autovelox['fixme:2'].unique())

# questi campi sono removibili

#print(autovelox['surface'].unique())
#print(autovelox['layer'].unique())
#print(autovelox['highway'].unique()) # -> SOLO speed_camera
#print(autovelox['old_name'].unique())
#print(autovelox['alt_name'].unique())
#print(autovelox['direction'].unique())

