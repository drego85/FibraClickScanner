#!/usr/python
# This file is part of FibraClick Scanner.
#
# Copyright(c) 2017 Andrea Draghetti
# https://www.andreadraghetti.it
#
# This file may be licensed under the terms of of the
# GNU General Public License Version 3 (the ``GPL'').
#
# Software distributed under the License is distributed
# on an ``AS IS'' basis, WITHOUT WARRANTY OF ANY KIND, either
# express or implied. See the GPL for the specific language
# governing rights and limitations.
#
# You should have received a copy of the GPL along with this
# program. If not, go to http://www.gnu.org/licenses/gpl.html
# or write to the Free Software Foundation, Inc.,
# 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.
import os
import json
import requests
from pushover import init, Client

try:
    from configparser import ConfigParser
except ImportError:
    from ConfigParser import ConfigParser  # ver. < 3.0

header = {"User-Agent": "Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; WOW64; Trident/6.0)",
          "Accept-Language": "it"}
timeoutconnection = 60
notfound = True

# Leggo i parametri di configurazione
if os.path.exists("config.txt") is True:
    config = ConfigParser()
    config.read("config.txt")
    sede_clli = config.get("fibraclick", "sede_clli")
    onu_id = config.get("fibraclick", "onu_id")
    status = config.get("fibraclick", "status")
    api_token = config.get("pushover", "api_token")
    user_key = config.get("pushover", "user_key")
else:
    print "Impossibile leggere il file di configurazione."
    print "Editare i parametri del file config.sample.txt e rinominarlo in config.txt!"
    exit()

# Inizializzo PushOver
if api_token:
    init(api_token)
else:
    print "Parametri Pushover assenti, impossibile inviare eventuale notifica push."

url = "https://fibra.click/api/data/copertura/armadi/?sede=%s" % sede_clli

page = requests.get(url, headers=header, timeout=timeoutconnection)
data = json.loads(page.text)

if sede_clli and onu_id:
    for each in data["data"]:
        if each["onu_id"] == onu_id:

            currentstatus = str(each["attivazione"])

            if currentstatus != status:

                print "Variato lo stato dell'ONU: " + onu_id + " in: " + currentstatus

                # Invio la notifica Push
                if api_token:
                    Client(user_key).send_message(
                        "Variato lo stato dell'ONU: " + onu_id + " in: " + currentstatus,
                        title="FibraClick Scanner", url="https://fibra.click",
                        url_title="Tutti i dettagli su FibraClick")

                # Aggiorno il file di configurazione con il nuovo valore ottenuto
                cfgfile = open("config.txt", "w")
                config.set("fibraclick", "status", currentstatus)
                config.write(cfgfile)
                cfgfile.close()

            else:
                print "Nessuna variazione dell'ONU: " + onu_id + ", " + currentstatus

            notfound = False
            break

    if notfound:
        print "ONU: " + onu_id + " e Sede Clli: " + sede_clli + " non attualmente pianificati o errore nell'inserimento dei dati."

else:
    print "ONU e Sede Clli non specificati, editare i parametri del file config.sample.txt e rinominarlo in config.txt!"
