# Kirjoita ohjelma, joka kysyy käyttäjältä kahden lentokentän ICAO-koodit.
# Ohjelma ilmoittaa lentokenttien välisen etäisyyden kilometreinä.
# Laskenta perustuu tietokannasta haettuihin koordinaatteihin.
# Laske etäisyys geopy-kirjaston avulla: https://geopy.readthedocs.io/en/stable/.
# Asenna kirjasto valitsemalla View / Tool Windows / Python Packages.
# Kirjoita hakukenttään geopy ja vie asennus loppuun.


import mysql.connector
# from collections import Counter # LISÄTTY. Python moduuli joka tehty erinäisen datan laskemiseen.
yhteys = mysql.connector.connect(
         host='127.0.0.1',
         port= 3306,
         database='flight_game',
         user='megapint',
         password='wine',
         autocommit=True
         )

def calculate_distance(icao1, icao2):
    sql = f"SELECT latitude_deg, longtitude_deg FROM aiport WHERE ident = '{icao1, icao2}'"
    print(sql)
    kursori = yhteys.cursor()
    kursori.execute(sql)





print()

print ("Ohjelma laskee kahden lentokentän etäisyyden ICAO koodien aculla.")
icao1 = input("Syötä ensimmäisen kentän ICAO:")
icao2 = input("Syötä toisen kentän ICAO:")

calculate_distance()