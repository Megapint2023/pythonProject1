# Kirjoita ohjelma, joka kysyy käyttäjältä lentoaseman ICAO-koodin.
# Ohjelma hakee ja tulostaa koodia vastaavan lentokentän nimen ja
# sen sijaintikunnan kurssilla käytettävästä lentokenttätietokannasta.
# ICAO-koodi on tallennettuna airport-taulun ident-sarakkeeseen.



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
