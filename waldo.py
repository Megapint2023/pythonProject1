#OHJELMA:
#STEP 1 = PELINALUSTUS
# - PRINT PELIOHJEET
# - PRINT KÄYTTÄJÄLLE OHJEET & KOMENTOVAIHTOEHDOT
# - MÄÄRITÄ SIJAINTI
# - ARVO MARKALAUKUN SIJAINTI
# - ALOITA VIHJE LASKURI
# - ALOITA PÄÄSTÖ LASKURI
# - KYSY NIMI
# - KYSY SEURAAVA MATKUSTUSMAA
# - MATKUSTA

# STEP 2
# - ILMOITA SAAPUMISMAAN TIEDOT
# - PÄIVITÄ SIJAINTI MATKALAUKKUUN
# - ILMOITA PELAAJALLE = Kylmempää/lämpimämpää
# - KM LASKURIN PÄIVITTYMINEN
# - VIHJE LASKURIN PÄIVITTYMINEN
# - KYSY PELAAJALTA UUSI MATKUSTUSMAA

# STEP 3
# - Luo kirjasto jossa vain sallitut matkustusmaat (eurooppa)
# - Pelaaja saapuu automaattisesti syöttämänsä maan päälentokentälle

import mysql.connector
from geopy.distance import geodesic
import random

yhteys = mysql.connector.connect(
         host='127.0.0.1',
         port= 3306,
         database='flight_game',
         user='megapint',
         password='wine',
         autocommit=True
         )

#  PELINALUSTUS
def aloita_peli():
    print("PRINT TAUSTATARINA TJPS")
    print("PRINT TARKOITUS esim. Löydä matkalaukku niin ja näin.")
    print("PRINT OHJEISTUS MITEN MATKUSTAA / SIIRTYY")
    pelaaja = input("SYÖTÄ PELAAJAN NIMI: ")
    current_location = "EFHK"
    print (f"Olet lentokentälklä: + {current_location}")
    matkalaukun_sijainti = random_sijainti()
    # MÄÄRITETÄÄN KM LASKURI
    total_kilometrit = 0
    # MÄÄRITETÄÄN VIHJE LASKURI
    vihje_counter = 0

def rendom_sijainti():
    pass


aloita_peli()




