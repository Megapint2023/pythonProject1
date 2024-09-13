import mysql.connector

def hae_icao(icao):
    sql = f"SELECT Numero, Sukunimi, Etunimi, Palkka FROM Työntekijä where Sukunimi='{icao}'"
    print(sql)
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()
    if kursori.rowcount >0 :
        for rivi in tulos:
            print(f"Päivää! Olen {rivi[2]} {rivi[1]}. Palkkani on {rivi[3]} euroa kuussa.")
    return