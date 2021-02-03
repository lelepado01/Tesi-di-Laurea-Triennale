# Tirocinio Interno

## Studio sull'incidentalità stradale tramite dataset aperti

### Utilizzo del codice: 

Tutti gli script utilizzati per questo lavoro sono reperibili a questa pagina 
[github](https://github.com/lelepado01/Tesi-di-Laurea-Triennale). 

Il repository è diviso in tre cartelle principali, *dataset*, *src* 
e *tesi*. La prima contiene tutti i file di dati utilizzati, divisi per 
argomento, e alcuni documenti di testo riguardanti le stime realizzate, come la percentuale di 
conducenti maschio e femmina. 

La cartella *tesi* contiene la maggior parte delle immagini presenti 
nella relazione (Ci si riferisce alle figure ottenute tramite screenshot 
da Google Maps e altri siti, non ai grafi). 
e il codice sorgente Latex usato per produrre la tesi.

Infine, nella directory *src* è contenuto il codice sorgente utilizzato 
per realizzare i grafi, le mappe e le stime, diviso per argomento. 
Ogni grafico è associato a uno script python che ne permette la creazione, registrato con 
lo stesso nome, e estensione *.py*. 

Quindi se in una cartella fosse presente l'immagine *esempio.png*, lo script con 
cui questa è stata creata avrà nome *esempio.py*. 

Invece, se si volessero trovare le informazioni sul grafico raffigurante 
l'incremento di incidenti dal 2010 al 2018, i dataset utilizzati si troverebbero 
nella directory:

dataset/incidenti/incidenti_istat

Mentre il codice sorgente e le immagini sarebbero situati al percorso:

src/incidenti/incidenti_senza_coords/anno

Alcune figure, in particolare quelle con grafici posizionati in coppia 
orizzontalmente (I grafici singoli sono tutti nella directory *src*, 
le figure doppie, unite tramite programmi esterni, in più, sono raccolte separatamente 
in *tesi/img_unite*), 
sono raccolte nella cartella *tesi/img_unite*, 
mentre la directory *tesi/img* contiene gli screenshot 
che non hanno bisogno di codice sorgente. 

Infine, in modo da fornire un collegamento tra i dataset nella specifica cartella e i siti 
di open data in cui sono stati trovati, nella tabella sottostante sono associati i percorsi di 
ogni file e l'url del portale di origine. 

### Provenienza dei Dati:

- Incidenti

    [Dati su Incidenti ISTAT](https://www.istat.it/it/archivio/87539)

    [Dati su Incidenti GEO (The Submarine)](https://www.google.com/maps/d/u/0/viewer?mid=1mXi6rbgjNHopZg7ZtpC-uZHY2f9wZ-58&ll=45.46373804532758%2C9.174953786724828&z=13)

    [Articolo The Submarine](https://thesubmarine.it/2018/06/20/mappa-incidenti-stradali-milano/)

    [Dati su Incidenti con Strada Provinciale (ACI)](http://www.aci.it/fileadmin/documenti/ACI/Trasparenza/Open_Data/Old_A_LOCALIZZAZIONE_INCIDENTI_STRADALI_STRADE_PROVINCIA.pdf) (2013 non disponibile)

    [Dati su Incidenti con Autostrada (ACI)](http://www.aci.it/fileadmin/documenti/ACI/Trasparenza/Open_Data/Catalogo_localizzazione_in_formato_Open_2019.pdf) 

    [ACI](http://www.aci.it/laci/studi-e-ricerche/dati-e-statistiche/open-data.html)

- Autovelox

    [Posizione in Italia](https://www.google.com/maps/d/viewer?mid=1CBgMTvIDnbGo22-Y1f3rVcbeX4C0v_w1&ll=45.365557951599605%2C10.03650113755961&z=8) 
    (Non ufficiale)

    [Posizione a Milano](https://overpass-turbo.eu/) 
    (Tramite openstreetmaps e Overpass API)

    [Autovelox installati nel 2014](https://www.ztlmilano.it/Autovelox-Milano)

- Meteo

    [Sensori](https://www.dati.lombardia.it/Ambiente/Stazioni-Meteorologiche/nf78-nj6b)

    [Dati sensore per 2020](https://www.dati.lombardia.it/Ambiente/Dati-sensori-meteo/647i-nhxk)

    [Dati sensore per tutti anni passati](https://www.arpalombardia.it/Pages/Meteorologia/Richiesta-dati-misurati.aspx)

    [Dati presi da ilmeteo](https://www.ilmeteo.it/portale/archivio-meteo/Milano/2010/)

    [Dati Milano Generali](https://zenodo.org/record/3992354)

- Linee Autobus (ATM)

    [Linee di superficie](https://dati.comune.milano.it/dataset/ds532-atm-composizione-percorsi-linee-di-superficie-urbane)

    [Percorsi linee di superficie](https://dati.comune.milano.it/dataset/ds538_atm-percorsi-linee-di-superficie-urbane)

- Linee Autobus (turistici)

    [Aree di sosta bus turistici](https://dati.comune.milano.it/dataset/ds740_sosta_bus_gt_turistici)

- Presenza di Pavé

    [Mappa con vie in pavé](https://blog.urbanfile.org/2018/05/02/milano-arredo-urbano-il-pave-risorsa-da-preservare-o-problema-da-eliminare/)

- Autostrade

    [Mappa con Autostrade](http://dati.mit.gov.it/catalog/dataset/grafo-stradale-anas)

- Patenti

    [Infografica](https://www.mit.gov.it/sites/default/files/media/notizia/2017-07/INFOGRAFICA%20Dati%20sintesi%20patenti%20Italia.pdf)

- Traffico per ora

    [Scrape di google maps ogni tot](https://www.google.com/maps/@45.4696946,9.1595385,13.09z/data=!5m1!1e1)
    : Servirebbe un modo per salvare tutti i dati per ogni ora

    [Maps](https://developers.google.com/maps/documentation/javascript/trafficlayer#maps_layer_traffic-javascript)
    : Sembra che maps non fornisca i dati sul traffico tipico, ma solo quello in tempo reale

    [Azure o Here](https://stackoverflow.com/questions/50987451/get-traffic-data)

    [Azure](https://stackoverflow.com/questions/58661346/how-to-get-raw-traffic-flow-data)

- Turismo

    [Istat](https://www.istat.it/it/archivio/16777)

- Informazioni provenienti dal dataset Istat/ACI sugli incidenti: 
    - Stagione
    - Traffico
    - Vento
    - Weekend
    - Tipo di Strada (autostrada, strada urbana...)
    - Segnaletica (rotonda...)
    - Sesso Conducente
