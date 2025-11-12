# Toteuta taustapalvelu, joka palauttaa annettua lentokentän ICAO-koodia vastaavan lentokentän nimen
# ja kaupungin JSON-muodossa.
# Tiedot haetaan opintojaksolla käytetystä lentokenttätietokannasta.
# Esimerkiksi EFHK-koodia vastaava GET-pyyntö annetaan muodossa: http://127.0.0.1:3000/kenttä/EFHK.
# Vastauksen on oltava muodossa: {"ICAO":"EFHK", "Name":"Helsinki Vantaa Airport", "Municipality":"Helsinki"}.

# mysql -u megapint -p
# wine
# DB: flight_game
# TABLES: airport / country / game / goal / goal_reached
# USE DB: airport
# DESCRIPTION: id / ident / type / name / keywords / latitude_deg / longitude_Deg / elevation_ft / continent /
# iso_country / iso_region / municipality / scheduled_service / gps_code / iata_code / local_code /home link
# ICAO = ident !!!
# airport name = name !!!

# PLAN: KÄYTÄ MODUULI 8 T1 koodia apuna:

# import mysql.connector
# yhteys = mysql.connector.connect(
#          host='127.0.0.1',
#          port= 3306,
#          database='flight_game',
#          user='megapint',
#          password='wine',
#          autocommit=True
#          )
#
# def hae_tiedot(icao):
#     sql = f"SELECT name, municipality FROM airport WHERE ident = '{icao}'"
#     print(sql)
#     kursori = yhteys.cursor()
#     kursori.execute(sql)
#     tulos = kursori.fetchall()
#     if kursori.rowcount >0 :
#         for rivi in tulos:
#             print(f"KAUPUNKI: {rivi[0]}, KUNTA: {rivi[1]}")
#     else:
#         print("Kyseisellä ICAO-koodilla ei löytynyt tietoja.")
#     kursori.close()
#
# print ("Ohjelma hakee ICAO-koodilla lentokentän tiedot.")
# icao = input(str("ICAO koodi:"))
# hae_tiedot(icao)

#

from flask import Flask, Response
import json
import mysql.connector

app = Flask(__name__)

yhteys = mysql.connector.connect(
         host='123.0.0.1',
         port= 3306,
         database='flight_game',
         user='megapint',
         password='wine',
         autocommit=True
         )

@app.route('/airport/<icao>')
def hae_tiedot(icao):
    kursori = yhteys.cursor()
    kursori.execute("SELECT name, municipality FROM airport WHERE ident = '{icao}'")
    tulos = kursori.fetchall()

    if tulos:
        vastaus = {
            "ICAO:": icao,
            "LENTOKENTTÄ:": tulos[1],
            "KAUPUNKI:": tulos[2]
        }
        tilakoodi = 200
    else:
        vastaus = {
            "status": 404,
            "teksti": "Virheellinen ICAO-koodi."
        }
        tilakoodi = 404

    kursori.close()

    jsonvast = json.dumps(vastaus)
    return Response(response=jsonvast, status=tilakoodi, mimetype="application/json")

@app.errorhandler(404)
def page_not_found(virhekoodi):
    vastaus = {
        "status": 404,
        "teksti": "Virheellinen päätepiste."
    }
    jsonvast = json.dumps(vastaus)
    return Response(response=jsonvast, status=404, mimetype="application/json")

if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=3000)


#    if kursori.rowcount >0 :
#        for rivi in tulos:
#            print(f"KAUPUNKI: {rivi[0]}, KUNTA: {rivi[1]}")
#    else:
#        print("Kyseisellä ICAO-koodilla ei löytynyt tietoja.")
# print ("Ohjelma hakee ICAO-koodilla lentokentän tiedot.")
# icao = input(str("ICAO koodi:"))

