
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

# Prendo una lista di tutti i file nella cartella
dir_path = 'dataset/incidenti/Classificazioni/'
res = os.listdir(dir_path)

# Elimino i file nella lista che non voglio convertire (quelli che non in formato html)
for f in res: 
    if not (os.path.isfile(dir_path + str(f)) and str(f).endswith(".html")): 
        res.remove(f)

def parse_html_file(path : str): 
    file = open(dir_path + file_path).read()
    parser = MyHTMLParser(dir_path)
    parser.feed(file)
    parser.file.close()

# Per ogni file parso i dati e li metto in un nuovo file csv
for file_path in res: 
    parse_html_file(file_path)