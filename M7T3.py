# OHJELMA - TIEDONHAKU JA LISÄÄMINEN
# Käyttäjä navigoi kysymyksillä ja voi lopettaa ohjelman koska tahansta painamalla enter.

# käyttäjä saa valita toiminnon monivalinnalla.
# Loop 1 hakee tietoa valmiista listasta ja Loop 2 tallettaa siihen tietoa.
# Teen kirjasto 'dictionary' listan

# OHJELMA1: Kysyy pelkkiä ICAO- koodeja - lopetus [enter].
# OHJELMA2: Kysyy Kaupungin nimen + ICAO-koodin ja lisää sen listaan.

#Teht ilmeisesti idea itse luoda lista jonka kautta toimii?
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

# HAUT
def aliyks():
    while True:
        icao = input("Syötä nelikirjaiminen ICAO:")
        if icao == "":
            print("Virheellinen koodi. Ohjelma loppu")
            break
        if icao in lennot:
            print(f"{icao} {lennot[icao]}")
        else:
            print(f"Kyseiseklä koodilla: {icao} ei löytynyt tietoja.")


# LISÄÄMINEN
def alikaks():
    while True:
        koodi = input("Syötä uuden kaupungin ICAO: ")
        if koodi == "":
            print("Ohjelma loppu.")
            break

        if koodi in lennot:
            print (f" Koodi: {koodi} löytyy jo. ")
        else:
            kaupunki = input("SSyötä uusi kaupunki: ")


print ("OHJELMA1: VALITSE TOIMINTO:")
print ("[1] = HAE LENTOKENTÄN TIEDOT: ICAO-koodilla")
print ("[2] = LISÄÄ UUSI LENTOKENTTÄ")
print ("[ENTER] = LOPETA OHJELMA")


while True:
    valinta = input("Syötä valinta:")

    if valinta == "":
        print ("Ohjelma loppu.")
        break

    valinta = int(valinta)

    if valinta == 1:
         print("Ohjelma1: Hae haluamasi lentokentän tiedont ICAO-koodillaa:")
         aliyks()

    elif valinta == 2:
         print("Ohjelma2: Lisää uusia Kaupunkeja ICAO koodin avulla:")
         alikaks()

    else:
         print("Virheellinen valinta! Syötä luku 1, 2 tai paina enter.")

