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
    print("PRINT OHJEISTUS MITEN MATKUSTAA / SIIRTYY / komennot")
    print("PRINT KIRJOITA sana ICAO -> Kirjoita maan -> saat vastauksena sen pääkentän ICAO:n ")

    pelaaja = input("SYÖTÄ PELAAJAN NIMI: ")
    current_location = "EFHK"
    print (f"Olet lentokentälklä: {current_location}")
    matkalaukun_sijainti = random_sijainti() # ARPOO LAUKUN SIJAINNIN
    # MÄÄRITETÄÄN KM LASKURI JA VIHJE LASKURI
    total_kilometrit = 0
    vihje_counter = 0

    while True:
        user_input = input("Syötä seuraavan kentän ICAO tai kirjoita ICAO:").upper()

        if user_input == "ICAO":
            country_name = input("Syötä maan nimi: ")
            icao_lista(country_name)
        else:
            if len(user_input) == 4:
                print(f"Matkustat lentokentälle {user_input}...")
                current_location = user_input
            else:
                print("Virheellinen koodi")

def random_sijainti():
    return "Placeholder" #tähän muuttuja sijaintia laskevan kaavan jälkeen

def icao_lista(country_name):
    sql = (
        "SELECT airport.ident AS icao_code "
        "FROM airport "
        "JOIN country ON airport.iso_country = country.iso_country "
        "WHERE country.name = '" + country_name + "' AND airport.type = 'large_airport';"
    )
    cursor = yhteys.cursor()
    cursor.execute(sql)
    results = cursor.fetchall()

    if results:
        print(f"Suuret lentokentät maassa {country_name}:")
        for result in results:
            print(f"- ICAO-koodi: {result[0]}")
    else:
         print(f"Ei löytynyt suuria lentokenttiä maassa: {country_name}")

aloita_peli()

#OHJELMA:
#STEP 1 = PELINALUSTUS
# - PRINT PELIOHJEET
# - PRINT KÄYTTÄJÄLLE OHJEET & KOMENTOVAIHTOEHDOT
# - MÄÄRITÄ SIJAINTI
# - ARVO MARKALAUKUN SIJAINTI
# - ALOITA VIHJE LASKURI            nämä täytyy alustaa funktion ulkopuolella koska muuttuja sokeus!
# - ALOITA PÄÄSTÖ LASKURI
# - KYSY NIMI
# - KYSY SEURAAVA MATKUSTUSMAA   #Komento()
# - MATKUSTA                   #Matkustus()

# STEP 2
# - ILMOITA SAAPUMISMAAN TIEDOT
# - PÄIVITÄ SIJAINTI MATKALAUKKUUN
# - ILMOITA PELAAJALLE = Kylmempää/lämpimämpää
# - KM LASKURIN PÄIVITTYMINEN
# - VIHJE LASKURIN PÄIVITTYMINEN
# - KYSY PELAAJALTA UUSI MATKUSTUSMAA

# STEP 3
# - Luo kirjasto jossa vain sallitut matkustusmaat (eurooppa)            #Rajataan SQL kyselyn avulla nämä
# - Pelaaja saapuu automaattisesti syöttämänsä maan päälentokentälle #Pelaaja voisi saapua aina lentokentälle mikä tulee 1. maan listalla vaikkapa order by name asc
                                                                    #Tämä koska kaikissa maissa ei ole large_airport

import random

#  PELINALUSTUS
def aloita_peli():
    print("PRINT TAUSTATARINA TJPS")
    print("PRINT TARKOITUS esim. Löydä matkalaukku niin ja näin.")
    print("PRINT OHJEISTUS MITEN MATKUSTAA / SIIRTYY / komennot")
    print("PRINT KIRJOITA sana ICAO -> Kirjoita maan -> saat vastauksena sen pääkentän ICAO:n ")


    pelaaja = input("SYÖTÄ PELAAJAN NIMI: ")
    current_location = "EFHK" #Tämä täytyisi insertata tietokantaan game.location
    print (f"Olet lentokentälklä: {current_location}")
    matkalaukun_sijainti = random_sijainti() # ARPOO LAUKUN SIJAINNIN
    # MÄÄRITETÄÄN KM LASKURI JA VIHJE LASKURI
    #Tähän asti näyttää hyvältä. loput jutut voisi hajauttaa ja tehdä funktiot itsenäisiksi osiksi
    #ehkä jopa omiin .py fileihin ettei tule
    #Liian spagettimainen koodi

    total_kilometrit = 0
    vihje_counter = 0


    #Miks tää on pelinalustus funktion sisällä??
    #Komento funktiosta ois hyvä saada erillinen mikä palauttaa sen käyttäjän inputin sit parametrina siis
    while True:
        user_input = input("Syötä seuraavan kentän ICAO tai kirjoita ICAO:").upper()

        if user_input == "ICAO":
            country_name = input("Syötä maan nimi: ")
            icao_lista(country_name)
        else:
            if len(user_input) == 4:
                print(f"Matkustat lentokentälle {user_input}...")
                current_location = user_input
            else:
                print("Virheellinen koodi")

def random_sijainti():
    return "Placeholder"

def icao_lista(country_name):
    sql = (
        "SELECT airport.ident AS icao_code "
        "FROM airport "
        "JOIN country ON airport.iso_country = country.iso_country "
        "WHERE country.name = '" + country_name + "' AND airport.type = 'large_airport';"
    )
    cursor = yhteys.cursor()
    cursor.execute(sql)
    results = cursor.fetchall()

    if results:
        print(f"Suuret lentokentät maassa {country_name}:")
        for result in results:
            print(f"- ICAO-koodi: {result[0]}")
    else:
         print(f"Ei löytynyt suuria lentokenttiä maassa: {country_name}")

aloita_peli()


#        # VIRHEILMOITUKSET MYÖHEMMIN
#        new_icao = seuraava_lento_kentta(new_country)
#        totaldistance = calculate_distance(current_location, new_icao)
#        total_kilometrit += totaldistance
#        vihje_counter += 1
#        # VIRHEILMOITUKSET MYÖHEMMIN
#        print(f"Saavut {new_country}-maahan. Etäisyys edellisestä sijainnista: {totaldistance:.2f} km.")
#
#        suitcase_distance = calculate_distance(new_icao, current_location)
#        previous_suitcase_distance = calculate_distance(current_location, current_location)
#
#        if suitcase_distance < previous_suitcase_distance:
#            print("Olet nyt lähempänä matkalaukkua!")
#        else:
#            print("Olet nyt kauempana matkalaukusta.")
#
#        current_location = new_icao
#
#        if suitcase_distance == location:
#            print("Onneksi olkoon! Löysit oikean maan!")
#            break



## ETISYYDEN LASKEMISEN FUNKTIO
#def calculate_distance(icao1, icao2):
#    try:
#        sql = f"SELECT latitude_deg, longitude_deg FROM airport WHERE ident IN ('{icao1}', '{icao2}')"
#        cursor = yhteys.cursor()
#        cursor.execute(sql)
#        tulos = cursor.fetchall()
#
#        if len(tulos) != 2:
#            print("Virhe haettaessa lentokenttien tietoja.")
#            return None
#
#        coords1 = (tulos[0][0], tulos[0][1])
#        coords2 = (tulos[1][0], tulos[1][1])
#
#        # Use geodesic distance from geopy
#        return geodesic(coords1, coords2).kilometers
#    except Exception as e:
#        print(f"Virhe: {e}")
#        return None
#
## LAUKUN SATUNNAINEN ARVONTA
#def random_current_location():
#    sql = "SELECT ident FROM airport WHERE iso_country IN (SELECT code FROM country WHERE continent = 'EU')"
#    cursor = yhteys.cursor()
#    cursor.execute(sql)
#    tulos = cursor.fetchall()
#
#    return random.choice(tulos)[0]
#
## LAUKUN SATUNNAINEN LENTOKENTÄN ARVONTAAN
#def get_random_airport_in_country(country_code):
#    sql = f"SELECT ident FROM airport WHERE iso_country = '{country_code}'"
#    cursor = yhteys.cursor()
#    cursor.execute(sql)
#    tulos = cursor.fetchall()
#
#    if tulos:
#        return random.choice(tulos)[0]
#    return None
#


# TODO LIST:
# MATKUSTAMINEN (Heini)
# -> Kysy minne käyttäjä haluaa matkustaa
# -> Tee db query, joka tarkistaa, että syötetty maa on EU:ssa
# -> EI / KYLLÄ (iffi)
# Päivitä pelaajan location
# palauta paluu arvona mihin maahan matkustit



def travel_to_next(next_destination):
    query = "SELECT name FROM country WHERE name = %s AND continent = 'EU'"

    kursori = yhteys.cursor()
    kursori.execute(query, (next_destination,))
    tulos = kursori.fetchone()

    if tulos:
        print(f"Matkustat maahan: {next_destination}")
    else:
        print(f"Maata {next_destination} ei löytynyt Euroopasta.")

    return next_destination


next_destination = input("Seuraava matkustuskohde?: ")
travel_to_next(next_destination)