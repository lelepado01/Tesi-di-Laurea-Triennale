
# Il dataset istat con dati di incidenti aveva metadati in file HTML
# Ho convertito tutti i file in csv in modo da poterli importare con pandas 

from html.parser import HTMLParser
import os

class MyHTMLParser(HTMLParser):
    def __init__(self, path): 
        # Distinguo la prima linea perchè contiene il nome del file csv 
        # (cioè il nome del campo) 
        self.start_line = ""
        self.file = None
        self.path : str = path
        HTMLParser.__init__(self)

    def handle_endtag(self, tag):
        # Se trovo un tag di chiusura </td>,  metto una virgola per separare il campo
        if tag == "td": 
            self.file.write(",")

    def handle_data(self, data):
        # Se sto parsando la prima linea, estraggo il nome del campo
        if self.start_line == "": 
            self.start_line = str(data)
            filename = self.start_line.split(" ")[4] # è sempre in quarta posizione
            self.file = open(self.path + filename + ".csv", "w")
        else: 
            # Se trovo qualunque dato, lo scrivo nel nuovo file
            self.file.write(data)

# Dir_path è il path relativo alla directory
# filename è il nome del file
# La funzione crea un nuovo file con nome = al campo che sta parsando
def parse_html_file(dir_path : str, file_name : str): 
    file = open(dir_path + file_name).read()
    parser = MyHTMLParser(dir_path)
    parser.feed(file)
    parser.file.close()

# Realizza un parse di file html in file csv a partire dalla directory di riferimento
def parse_files_in_dir(dir_path : str): 
    # Prendo una lista di tutti i file nella cartella
    res = os.listdir(path)

    # Elimino i file nella lista che non voglio convertire (quelli che non in formato html)
    for f in res: 
        if not (os.path.isfile(dir_path + str(f)) and str(f).endswith(".html")): 
            res.remove(f)

    # Per ogni file parso i dati e li metto in un nuovo file csv
    for file_path in res: 
        parse_html_file(dir_path, file_path)

# Posso fare parse di più file alla volta
#dir_path = 'dataset/incidenti/Classificazioni/'
#parse_files_in_dir(dir_path)

# O di un solo file
#parse_html_file("dataset/incidenti/Classificazioni/", "INCSTRAD_Classificazione_Anno 2011_var36.html")