# OHJELMA - LENTOKENTTÄHAKU TAI LISÄYS -

# Ohjelma kysyy käyttäjältä, haluaako tämä syöttää uuden lentoaseman,
# hakea jo syötetyn lentoaseman tiedot vai lopettaa.

# Jos käyttäjä valitsee uuden lentoaseman syöttämisen, ohjelma kysyy käyttäjältä lentoaseman ICAO-koodin ja
# nimen. Jos käyttäjä valitsee haun, ohjelma kysyy ICAO-koodin ja tulostaa sitä vastaavan lentoaseman nimen.
# Jos käyttäjä haluaa lopettaa, ohjelman suoritus päättyy.

# Käyttäjä saa valita uuden toiminnon miten monta kertaa tahansa aina siihen asti,
# kunnes hän haluaa lopettaa. (ICAO-koodi on lentoaseman yksilöivä tunniste.
# Esimerkiksi Helsinki-Vantaan lentoaseman ICAO-koodi on EFHK. Löydät koodeja helposti selaimen avulla.)


# -> Eli inputin sijaan tarttee jonkun monivalinta systeemin?...
print ("OHJELMA: VALITSE TOIMINTO")
print ("[1] = LENTOKENTTÄHAKU [ICAO-koodi]")
print ("[2] = LISÄÄ PUUUTTUVA LENTOKENTTÄ")
print ("[ENTER] = LOPETA OHJELMA")

while True:
    uus = 0
    valinta = input("Syötä valinta:")
    if valinta == "":
        print ("Ohjelma loppu.")
        break
    if valinta == 1:
       valinta = int(haku)
       print("*LENTOKENTTÄHAKU*")
    if valinta == 2:
       valinta = int(lisa)
  else:
       print("Virheellinen valinta! Syötä luku 1, 2 tai paina pelkästään enteriä.")
       return = uus




# Get Flight info
# Add new ICAO-code

#OHJELMAN OMINAISUUDET:
#1. Lentoasemien tiedon haku.(ICAO-Koodi:lla)  Db?
#2. Tietokantaan lisääminen ohjelman avulla? ->  "Lisää puuttuva lentokenttä".
#3. Lopeta Ohjelma -> ENTER.

# Lisää puuttuva lentokenttäkoodi:

