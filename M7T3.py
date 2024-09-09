#Kirjoita ohjelma lentoasematietojen hakemiseksi ja tallentamiseksi.
# Ohjelma kysyy käyttäjältä, haluaako tämä syöttää uuden lentoaseman,
# hakea jo syötetyn lentoaseman tiedot vai lopettaa.

# Jos käyttäjä valitsee uuden lentoaseman syöttämisen, ohjelma kysyy käyttäjältä lentoaseman ICAO-koodin ja
# nimen. Jos käyttäjä valitsee haun, ohjelma kysyy ICAO-koodin ja tulostaa sitä vastaavan lentoaseman nimen.
# Jos käyttäjä haluaa lopettaa, ohjelman suoritus päättyy.

# Käyttäjä saa valita uuden toiminnon miten monta kertaa tahansa aina siihen asti,
# kunnes hän haluaa lopettaa. (ICAO-koodi on lentoaseman yksilöivä tunniste.
# Esimerkiksi Helsinki-Vantaan lentoaseman ICAO-koodi on EFHK. Löydät koodeja helposti selaimen avulla.)

# -> Eli inputin sijaan tarttee jonkun monivalinta systeemin?...
("VALITSE SEURAAAVISTA:   LENTOKENTTÄHAKU, PAINA 1. TAI LISÄÄ PUUTTUVA LENTOKENTTÄ -> PAINA 2 ")


# Get Flight info
# Add new ICAO-code

#OHJELMAN OMINAISUUDET:
#1. Lentoasemien tiedon haku.(ICAO-Koodi:lla)  Db?
#2. Tietokantaan lisääminen ohjelman avulla? ->  "Lisää puuttuva lentokenttä".
#3. Lopeta Ohjelma -> ENTER.

# Lisää puuttuva lentokenttäkoodi:
airport = input("Valintse toiminto: Lentokettähaku -> paina 'H'.  ")
