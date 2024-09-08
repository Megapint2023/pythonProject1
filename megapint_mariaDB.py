import mysql.connector

yhteys = mysql.connector.connect(
         host='127.0.0.1',
         port= 3306,
         database='flight_game',
         user='megapint',
         password='',
         autocommit=True
         )

# hakee ja palauttaa goal taulun sisällön
#def hae_goalit():
#    #SQL-koodi joka halutaan lähettää suoritettavaksi
#    sql_kysely = "select * from goal"
#    #luodann kursori jonka kauttatietokantaa voidaan käyttää
#    kursori = yhteys.cursor()
#    #lähetetään kursori suoritettavaksi
#    kursori.execute(sql_kysely)
#    # haetaan kyselyyn vastaus "tulos"
#    tulos = kursori.fetchall()
#    #käsitellään tulosrivi kerrallaan
#   # if kursori.rowcount > 0:
#   #     for rivi in tulos:
#   #         print(rivi[1])
#    return tulos
#goalit = hae_goalit()
#for g in goalit:
#    print(g)