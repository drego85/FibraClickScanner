# FibraClick Scanner


Questo software nasce con l'idea di ricevere in maniera totalmente automatica una notifica Push sul proprio Smartphone non appena il cabinet della Fibra (VDSL) TIM viene attivato.

Una seconda revisione dello scanner integra invece la notifica di una qualsiasi varazione dello statto del cabinet o del comune indicato.

Vengono analizzati i dati forniti dal portale [FibraClick](https://fibra.click/) e qualora risultasse una variazione (Attivato, Cambio Pianificazione, Saturo, ecc) rispetto alla precedente analisi viene inviata una notifica Push allo Smartphone o Tablet attraverso i servizi offerti da [PushOver](https://pushover.net/).


#### Utilizzo

Lo scanner permette di monitorare l'attivazione generica di un comune o più specificatamente l'attivazione del proprio ONU (Armadio).

Nel primo caso si riceverà una notifica quall'ora il comune venga pianificato per l'attivazione della Fibra TIM e gli eventuali aggiornamenti di pianificazione.
Nel secondo caso si riceverà una notifica quando lo stato del proprio ONU cambia (pianificato, attivo, saturo, ecc)

Se il proprio comune non è attualmente pianificato potete valorizzare esclusivamente la variabile "comune" nel file di configurazione, nel momento in cui il comune verrà pianificato per l'attivazione della Fibra riceverete una notifica.

Se il tuo comune è invece già pianificato o attivo recati sul sito [FibraClick](https://fibra.click/) e prelevare il nome della propria Centrale (CLLI) e il numero del proprio ONU (attenzione omettere eventuale testo/cifre prima del trattino basso "_" e indicare se previsto lo zero prima del numero della centrale) o la lista dei numeri onu da monitorare.

Esempio: Per il comune di Roma, Centrale Aurelia, Cabinet 001 i dati di nostro interesse sono:
 * ROMAITEH
 * 001

Configurare pertanto il file config.txt come indicato di seguito ed eseguire in maniera automatica lo script (su Linux è possibile usare crontab).
 
#### File configurazione

Il file config.sample.txt una volta editato con i corretti valori va rinominato in config.txt

Sfruttando i dati prelevati in precedenza il file config.txt dovrà essere così valorizzato:

[pushover]

api_token = Visitare [PushOver](https://pushover.net/) per ottenere la chiave della propria Applicazione

user_key = Visitare [PushOver](https://pushover.net/) per ottenere la chiave del proprio Dispositivo

[fibraclick]

comune = 

sede_clli = ROMAITEH

onu_ids = 001,002,003


#### Librerie Python 

Per una corretta esecuzione del codice è necessario installare le seguenti librerie (tra parentesi il comando da eseguire per l'installazione):

* python-pushover (pip install python-pushover --upgrade)
* configparser (pip install configparser --upgrade)

#### Screenshot Notifica

![Screenshot Notifica Notifica](https://www.andreadraghetti.it/wp-content/uploads/2017/01/IMG_1407-640x430.png)

#### License

Copyright (c) 2017 Andrea Draghetti | [Twitter](https://twitter.com/andreaghetti) | [Blog](https://www.andreadraghetti.it)  
Released under the GPL 3 license.
