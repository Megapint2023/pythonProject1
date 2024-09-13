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

def hae_tiedot(iso_country):
    sql = f"SELECT name, type FROM airport WHERE iso_country = '{iso_country}'" # viilaa
    print(sql)
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()
    if kursori.rowcount >0 :
        for rivi in tulos:
            print(f"LENTOKENTTÄ: {rivi[0]}, TYYPPI: {rivi[1]}") # selvitä miten saa kaikki tuloksen rivit sekä miten "laskutoimitus"
    else:
        print("Kyseisellä maakoodilla ei löytynyt tietoja.")
    kursori.close()

print ("Ohjelma etsii maakoodilla kaikki sen lentokentät (esim. FI).")
iso_country = input(str("Syötä maakoodi:"))
hae_tiedot(iso_country)