
from html.parser import HTMLParser
import os

class MyHTMLParser(HTMLParser):
    def __init__(self, path): 
        self.start_line = ""
        self.file = None
        self.path : str = path
        HTMLParser.__init__(self)

    def handle_endtag(self, tag):
        if tag == "td": 
            self.file.write(",")

    def handle_data(self, data):
        if self.start_line == "": 
            #print(data)
            self.start_line = str(data) 
            filename = self.start_line.split(" ")[4]
            #print(self.path + filename)
            self.file = open(self.path + filename + ".csv", "w")
        else: 
            self.file.write(data)

dir_path = 'dataset/incidenti/Classificazioni/'

res = os.listdir(dir_path)
#print(res)
for f in res: 
    if not (os.path.isfile(dir_path + str(f)) and str(f).endswith(".html")): 
        res.remove(f)

#print(res)

for file_path in res: 
    file = open(dir_path + file_path).read()
    parser = MyHTMLParser(dir_path)
    parser.feed(file)
    parser.file.close()