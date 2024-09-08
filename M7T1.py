# OHJELMA kysyy käyttäjältä kuukauden "numeron".
# Sen jälkeen tulostaa vastaavan vuodenajan (kevät, kesä, syksy, talvi).

# Kuukausia vastaavat vuodenajat !!!!merkkijonoina monikkotietorakenteeseen!!!!.
# Parametri 3kk X4 vuodenaikaa
# Joulukuu oltava = "1" kk
# käyttäjänhän ei tarvitse tietää, että joulukuu = 1 kk,
# koska toimivuus perustuu vuodenajan määrittämiseen

print("Ohjema ilmoittaa kk vastaavan vuodenajan.")

kuukausi = ("joulukuu", "tammikuu", "helmikuu", "maaliskuu", "huhtikuu", "toukokuu", "kesäkuu", "heinakuu", "elokuu", "syyskuu", "lokakuu", "marraskuu")
kknro = input("Syötä kuukauden numero 1-12: ")
kknro = int(kknro)
kuukausi = kuukausi[kknro]
# print (kuukausi) - disabled
# Nyt tämän printin sijaan tehdään aliohjelma joka,
# muuttujan "kuukausi[kknro]":n arvon perusteella määrittääja tulostaa vuodenajan

vuodenaika(hae)


kevat = 4, 5, 6
kesa = 7, 8, 9
syksy = 10, 11, 12
talvi = 1, 2, 3