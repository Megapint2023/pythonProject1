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

def aloita_peli():
    print("PRINT TAUSTATARINA TJPS")
    print("PRINT TARKOITUS esim. Löydä matkalaukku niin ja näin.")
    print("PRINT OHJEISTUS MITEN MATKUSTAA / SIIRTYY")
    pelaaja = input("SYÖTÄ PELAAJAN NIMI: ")
    location = "EFHK"
    print (f"Olet lentokentälklä: + {location}")
    matkalaukku = arvo_laukku_sijainti()

    total_kilometrit = 0
    vihje_counter = 0

    while True:


def calculate_distance(info1, info2):
    sql = f"SELECT info FROM table WHERE data IN jotain ('{info1}', '{info2}')"
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()

    if len(tulos) != mitä ei pitäisi olla:
        print("VIRHEILMOITUS")
        return

    etaisyys = distance(tulos[0], tulos[1]).kilometers

    print(f"Etäisyys {icao1} ja {icao2} välillä on {etaisyys:.2f} kilometriä.")




aloita_peli()

