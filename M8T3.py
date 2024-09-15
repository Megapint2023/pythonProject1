# Kirjoita ohjelma, joka kysyy käyttäjältä kahden lentokentän ICAO-koodit.
# Ohjelma ilmoittaa lentokenttien välisen etäisyyden kilometreinä.
# Laskenta perustuu tietokannasta haettuihin koordinaatteihin.
# Laske etäisyys geopy-kirjaston avulla: https://geopy.readthedocs.io/en/stable/.
# Asenna kirjasto valitsemalla View / Tool Windows / Python Packages.
# Kirjoita hakukenttään geopy ja vie asennus loppuun.


import mysql.connector
from geopy.distance import distance
yhteys = mysql.connector.connect(
         host='127.0.0.1',
         port= 3306,
         database='flight_game',
         user='megapint',
         password='wine',
         autocommit=True
         )

def calculate_distance(icao1, icao2):
    sql = f"SELECT latitude_deg, longitude_deg FROM airport WHERE ident IN ('{icao1}', '{icao2}')"
   # print(sql)
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()

    if len(tulos) != 2:
        print("Virhe, yhtä tai molempiä kenttiä ei löytynyt.")
        return

    lat1, lon1 = tulos[0]
    lat2, lon2 = tulos[1]
    icao1_coords = (lat1, lon1)
    icao2_coords = (lat2, lon2)
    etaisyys = distance(icao1_coords, icao2_coords).kilometers

    print(f"Etäisyys {icao1} ja {icao2} välillä on {etaisyys:.2f} kilometriä.")

print ("Ohjelma laskee kahden lentokentän etäisyyden ICAO koodien aculla.")
icao1 = input("Syötä ensimmäinen ICAO:")
icao2 = input("Syötä toinen ICAO:")

calculate_distance(icao1, icao2)