# Kirjoita ohjelma, joka kysyy käyttäjältä maakoodin (esimerkiksi FI) ja tulostaa kyseisessä maassa
# olevien lentokenttien lukumäärät tyypeittäin.
# Esimerkiksi Suomen osalta tuloksena on saatava tieto siitä,
# että pieniä lentokenttiä on 65 kappaletta, helikopterikenttiä on 15 kappaletta jne.


import mysql.connector
from collections import Counter # LISÄTTY. Python moduuli joka tehty erinäisen datan laskemiseen.

yhteys = mysql.connector.connect(
         host='127.0.0.1',
         port= 3306,
         database='flight_game',
         user='megapint',
         password='wine',
         autocommit=True
         )

def hae_tiedot(iso_country):
    sql = f"SELECT name, type FROM airport WHERE iso_country = '{iso_country}'" # TOIMII
    print(sql)
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()
    # if kursori.rowcount >0 :  -> else: lopussa ajaa samaa kuin tämä rivi
    if tulos:
        tyypit = Counter() # LISÄTTY -> tavallinen functio laskisi vaan yhteen kaikki tyypit. Counter taas on sisäänrakennettu functio, joka osaa myös erottamaa eri tyyppien tosistaan ja laskee ne erikseen
        for rivi in tulos: #looppi printtaa kaikki kentät. Samalla rivillä tiedot: nimi + tyyppi
            print(f"LENTOKENTTÄ: {rivi[0]}, TYYPPI: {rivi[1]}")
            tyypit[rivi[1]] += 1 # laskuri -> kpl määrät
        print("===============================================================") # printtauksessa erottelee tiedon
        for airport_type, count in tyypit.items():
            print(f"{count} {airport_type}(s)")
    else:
        print("Kyseisellä maakoodilla ei löytynyt tietoja.")

    kursori.close()

print ("Ohjelma etsii maakoodilla kaikki sen lentokentät (esim. FI).")
iso_country = input("Syötä maakooodi: ").upper() # LISÄTTY .upper() -> muuttaa kirjaimet isoksi "toimintavarmempi"
hae_tiedot(iso_country)