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
    print(f"KAUUKAUSI: {kkinfo[rivi]}")
    vuodenaika(kknro)

# tässä kerrotaan käyttäjälle vuodenajan lisäksi muut kuukaudet jotka siihen kuuluvat
def vuodenaika(kknro):
    if kknro > 0 and kknro <= 3:
        print ("Vuodenaika:Talvi (joulukuu, tammikuu ja helmikuu)")
    elif kknro >= 4 and kknro <= 6:
        print ("Vuodenaika:Kevät (maaliskuu, huhtikuu ja toukokuu)")
    elif kknro >= 7 and kknro <= 9:
        print ("Vuodenaika:Kesä  (kesäkuu, heinäkuu ja elokuu)")
    elif kknro >= 10 and kknro <= 12:
        print ("Vuodenaika:Syksy (syyskuu, lokakuu ja marraskuu)")

kknro = int(input("Syötä kuukauden numero 1-12: ")) # käyttäjänhän ei tarvitse tietää, että joulukuu = "1"
kknro = int(kknro)

kuukausi(kknro)









