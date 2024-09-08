# OHJELMA kysyy käyttäjältä kuukauden "numeron".
# Sen jälkeen tulostaa vuodenajan (kevät, kesä, syksy, talvi).
# Kuukausia vastaavat vuodenajat !!!!merkkijonoina monikkotietorakenteeseen!!!!.
#
# Parametri 3kk X4 vuodenaikaa
# Joulukuu oltava = "1"

#kk = ("joulukuu", "tammikuu", "helmikuu", "maaliskuu", "huhtikuu", "toukokuu", "kesäkuu",
 #             "heinakuu", "elokuu", "syyskuu", "lokakuu", "marraskuu")

print("Ohjema ilmoittaa kk vastaavan vuodenajan.")

kkinfo = {
    1: "Joulukuu",
    2: "Tammikuu",
    3: "Helmikuu",
    4: "Maaliskuu",
    5:   "Huhtikuu",
    6:   "Toukokuu",
    7:   "Kesäkuu",
    8:   "Heinäkuu",
    9:   "Elokuu",
    10:  "Syyskuu",
    11:   "Lokakuu",
    12:   "Marraskuu",
}

# tällä funktiolla korjaan "koodissa" kk järj
def kuukausi(kknro):
    rivi = kknro + 1
    if rivi > 12:
        rivi = 1
    elif:
        print(f"Syöttämäsi kuukausi oli: {kkinfo[rivi]} .")
    vuodenaika(kknro)

# tässä kerrotaan käyttäjälle vuodenajan lisäksi muut kuukaudet jotka siihen kuuluvat
def vuodenaika(kknro):
    if kknro == 1 or 2 or 3:
         print ("Vuodenaika: Talvi - joulukuu, tammikuu ja maaliskuu")
    elif kknro == 4 or 5 or 6:
         print ("Vuodenaika: Kevät -  huhtikuu, toukokuu ja kesäkuu")
    elif kknro == 7 or 8 or 9:
         print ("Vuodenaika: Kesä -  heinäkuu, elokuu ja syyskuu")
    elif kknro == 10 or 11 or 12:
         print ("Vuodenaika: Syksy - joulukuu, tammikuu ja maaliskuu")
         return kknro

kknro = input("Syötä kuukauden numero 1-12: ") # käyttäjänhän ei tarvitse tietää, että joulukuu = "1"
kknro = int(kknro)

kuukausi(kknro)
vuodenaika(kknro)










