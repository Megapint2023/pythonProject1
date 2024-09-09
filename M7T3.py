# OHJELMA - LENTOKENTTÄHAKU TAI ASEMAN LISÄYS
# Käyttäjä navigoi kysymyksillä ja siksi voi lopettaa ohjelman koska tahansta painamalla pelkästään enter.

# Ensin käyttäjä saa monivalinta kysymyksen ja sen jälkeen käytännössä 2 pyörivää looppia.
# Loop 1 hakee tietoa valmiista listasta ja Loop 2 tallettaa siihen tietoa.
# Teen kirjasto 'dictionary' listan

# OHJELMA1: Kysyy pelkkiä ICAO- koodeja - lopetus [enter].
# OHJELMA2: Kysyy Kaupungin nimen + ICAO-koodin ja lisää sen listaan.

#Teht ilmeisesti idea itse luoda lista jota hyödyntäen homma toimii. (ei DB:tä täs vaihees vielä?)
# (ICAO-koodi on lentoaseman yksilöivä tunniste. Helsinki-Vantaan lentoaseman ICAO-koodi on EFHK.

lennot = {
    "KATL": "Atlanta",
    "ZBAA": "Beijing",
    "OMDB": "Dubai",
    "KLAX": "Los Angeles",
    "RJTT": "Tokyo",
    "EGLL": "London",
    "KORD": "Chicago",
    "LFPG": "Paris",
    "VHHH": "Hong Kong",
    "EDDF": "Frankfurt",
    "WSSS": "Singapore",
    "EHAM": "Amsterdam",
    "VIDP": "Delhi",
    "ZSPD": "Shanghai",
    "LEMD": "Madrid",
    "CYYZ": "Toronto",
    "YSSY": "Sydney",
    "RKSI": "Seoul",
    "KDFW": "Dallas/Fort Worth",
    "LIRF": "Rome",
    "OTHH": "Doha",
    "VABB": "Mumbai",
    "ZGGG": "Guangzhou",
    "YVR": "Vancouver",
    "EDDM": "Munich",
    "LTFM": "Istanbul",
    "LFPO": "Paris Orly",
    "UUEE": "Moscow Sheremetyevo",
    "LOWW": "Vienna",
    "LGAV": "Athens",
    "LEBL": "Barcelona",
    "NZAA": "Auckland",
    "ZJSY": "Sanya",
    "WMKK": "Kuala Lumpur",
    "SBGR": "São Paulo",
    "FAOR": "Johannesburg",
    "WIII": "Jakarta",
    "RPLL": "Manila",
    "LTBA": "Istanbul Atatürk",
    "LIMC": "Milan",
    "KJFK": "New York John F. Kennedy",
    "LSZH": "Zurich",
    "EGGW": "London Luton",
    "KSEA": "Seattle",
    "CYYC": "Calgary",
    "EIDW": "Dublin",
    "OMAA": "Abu Dhabi",
    "MMMX": "Mexico City",
    "RJAA": "Narita",
    "WADD": "Bali",
    "LSGG": "Geneva",
    "LROP": "Bucharest",
    "ZLLL": "Lanzhou",
    "KPHX": "Phoenix",
    "KBOS": "Boston",
    "KMIA": "Miami",
    "LFML": "Marseille",
    "KDEN": "Denver",
    "ENGM": "Oslo",
    "ESSA": "Stockholm",
    "ZBHH": "Hohhot",
    "ZSSS": "Shanghai Hongqiao",
    "LGKR": "Corfu",
    "ZBTJ": "Tianjin",
    "RJGG": "Nagoya",
    "VIDD": "New Delhi",
    "VNKT": "Kathmandu",
    "HKJK": "Nairobi",
    "OKBK": "Kuwait City",
    "HECA": "Cairo",
    "ZUCK": "Chongqing",
    "EGBB": "Birmingham",
    "LBSF": "Sofia",
    "LFLL": "Lyon",
    "LTAI": "Antalya",
    "OERK": "Riyadh",
    "VOBL": "Bangalore",
    "ZPPP": "Kunming",
    "SBGL": "Rio de Janeiro",
    "OMAD": "Abu Dhabi Al Bateen",
    "LEZL": "Seville",
    "LSZA": "Lugano",
    "GMMN": "Casablanca",
    "LTAC": "Ankara",
    "VTSM": "Samui",
    "KMSP": "Minneapolis",
    "KBWI": "Baltimore",
    "KSFO": "San Francisco",
    "NZWN": "Wellington",
    "MPTO": "Panama City",
    "TNCA": "Aruba",
    "TJSJ": "San Juan",
    "MMUN": "Cancun",
    "EWRL": "Newark",
    "SVMI": "Caracas",
    "SBRJ": "Rio de Janeiro Santos Dumont",
    "SBBR": "Brasilia",
    "DGAA": "Accra",
    "ZWWW": "Urumqi",
    "VDSR": "Siem Reap",
    "DNMM": "Lagos",
    "OOMS": "Muscat"
}

print ("OHJELMA: VALITSE TOIMINTO")
print ("[1] = LENTOKENTTÄHAKU [ICAO-koodi]")
print ("[2] = LISÄÄ PUUUTTUVA LENTOKENTTÄ")
print ("[ENTER] = LOPETA OHJELMA")


while True:
    valinta = input("Syötä valinta:")

    if valinta == "":
        print ("Ohjelma loppu.")
        break

    valinta = int(valinta)

    if valinta == 1:
         valinta = ohjelma1
         print ("Ohjelma1: Hae lentoaseman tiedot. Tarvitset ICAO-koodilla:")

    elif valinta == 2:
         valinta = ohjelma2
         print("Ohjelma2: Uuden lentoaseman määrittäminen:")
    else:
         print("Virheellinen valinta! Syötä luku 1, 2 tai paina enter.")



def ohjelma1(lennot):
    rivi = lennot + 1
    if rivi > 0:
        rivi = 1
    print(f"KAUUKAUSI: {lennot[rivi]}")
    vuodenaika(kknro)
# Tarvitaan ohjelma joka kysyy käyttäjältä yhden ICAO koodin
# ja skannaa  kirjaston läpi ja printtaa vastaaavan arvon

print ("Ohjelma vertaa kummasta pizzasta sait enemmän vastinetta rahoillesi.")

d1 = input("Syötä ensimmäisen pizzan halkaisija senttimetreinä: ")
d1 = float(d1)
hinta1 = input("Syötä ensimmäisen pizzan hinta: ")
hinta1 = float(hinta1)
d2 = input("Syötä toisen pizzan halkaisija senttimetreinä: ")
d2 = float(d2)
hinta2 = input("Syötä toisen pizzan hinta: ")
hinta2 = float(hinta2)

