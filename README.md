# Tirocinio

## Studio sull'incidentalità stradale tramite dataset aperti

### Incidenti

[Dati su Incidenti ISTAT](https://www.istat.it/it/archivio/87539)

[Dati su Incidenti GEO (The Submarine)](https://www.google.com/maps/d/u/0/viewer?mid=1mXi6rbgjNHopZg7ZtpC-uZHY2f9wZ-58&ll=45.46373804532758%2C9.174953786724828&z=13)

[Dati su Incidenti con Strada Provinciale (ACI)](http://www.aci.it/fileadmin/documenti/ACI/Trasparenza/Open_Data/Old_A_LOCALIZZAZIONE_INCIDENTI_STRADALI_STRADE_PROVINCIA.pdf) (2013 non disponibile)

[Dati su Incidenti con Autostrada (ACI)](http://www.aci.it/fileadmin/documenti/ACI/Trasparenza/Open_Data/Catalogo_localizzazione_in_formato_Open_2019.pdf) 

[ACI](http://www.aci.it/laci/studi-e-ricerche/dati-e-statistiche/open-data.html)

### Dati:

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

- Linee Autobus (ATM)

    [Linee di superficie](https://dati.comune.milano.it/dataset/ds532-atm-composizione-percorsi-linee-di-superficie-urbane)

    [Percorsi linee di superficie](https://dati.comune.milano.it/dataset/ds538_atm-percorsi-linee-di-superficie-urbane)

- Linee Autobus (turistici)

    [Aree di sosta bus turistici](https://dati.comune.milano.it/dataset/ds740_sosta_bus_gt_turistici)

- Presenza di Piste Ciclabili

    [Percorsi piste ciclabili](https://geoportale.comune.milano.it/sit/cerca-nel-catalogo/)

- Presenza di Pavé

    [Mappa con vie in pavé](https://blog.urbanfile.org/2018/05/02/milano-arredo-urbano-il-pave-risorsa-da-preservare-o-problema-da-eliminare/)

- Autostrade

    [Mappa con Autostrade](http://dati.mit.gov.it/catalog/dataset/grafo-stradale-anas)

- Presenza di trasporto merci

- Posso usare direttamente il dataset sugli incidenti per: 
    - Stagione
    - Traffico
    - Vento
    - Weekend
    - Tipo di Strada (autostrada, strada urbana...)
    - Segnaletica (rotonda...)
    - Sesso Conducente

### Todo

- Devo tradurre i commenti / i nomi delle variabili in inglese?
- Trascrivere commenti importanti da file a latex, che ordine devo tenere per i capitoli? 
- Trovare mappa con Pavè a milano
- Campione conducenti veicoli
- Dataset con autostrade è troppo grande, non posso caricarlo su git, e richiede tanta pulizia

### Risultati da Trascrivere in Tesi: 

- [x] Atm + Incidenti
- [ ] Autovelox + Incidenti
- [ ] Ciclabili + Incidenti
- [ ] Meteo
- [x] Incidenti ACI (i dati che ho trovato sulle autostrade sono confermati dai dati istat)
- [x] Mese Incidenti
- [x] Ora Incidenti
- [x] Strada Incidenti
- [x] Tipo Veicoli
- [x] Conducente Veicolo
- [x] Pedoni
- [x] Incidenti per Trimestre