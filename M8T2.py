# Kirjoita ohjelma, joka kysyy käyttäjältä maakoodin (esimerkiksi FI) ja tulostaa kyseisessä maassa
# olevien lentokenttien lukumäärät tyypeittäin.
# Esimerkiksi Suomen osalta tuloksena on saatava tieto siitä,
# että pieniä lentokenttiä on 65 kappaletta, helikopterikenttiä on 15 kappaletta jne.


import mysql.connector
yhteys = mysql.connector.connect(
         host='127.0.0.1',
         port= 3306,
         database='flight_game',
         user='megapint',
         password='wine',
         autocommit=True
         )

def hae_tiedot(icao):
    sql = f"SELECT name, municipality FROM airport WHERE ident = '{icao}'"
    print(sql)
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()
    if kursori.rowcount >0 :
        for rivi in tulos:
            print(f"KAUPUNKI: {rivi[0]}, KUNTA: {rivi[1]}")
    else:
        print("Kyseisellä ICAO-koodilla ei löytynyt tietoja.")
    kursori.close()

print ("Ohjelma hakee ICAO-koodilla lentokentän tiedot.")
icao = input(str("ICAO koodi:"))
hae_tiedot(icao)