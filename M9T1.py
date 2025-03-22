#Kirjoita Auto-luokka, jonka ominaisuuksina ovat rekisteritunnus, huippunopeus,
# tämänhetkinen nopeus ja kuljettu matka.
# Kirjoita luokkaan alustaja,
# joka asettaa ominaisuuksista kaksi ensin mainittua parametreina saatuihin arvoihin.
# Uuden auton nopeus ja kuljetut matka on asetettava automaattisesti nollaksi.
# Kirjoita pääohjelma, jossa luot uuden auton (rekisteritunnus ABC-123, huippunopeus 142 km/h).
# Tulosta pääohjelmassa sen jälkeen luodun auton kaikki ominaisuudet.
# 19.03.2025

# object (olio) / atrtributes (ominaisuudet) / methods (metodit)

class Auto: # tämä class
    def __init__(self, rekisteri, huippunopeus): # tämä alustaja
        # ominaisuudet
        self.rekisteri = rekisteri
        self.huippunopeus = huippunopeus
        self.nopeus = 0
        self.matka = 0

auto = Auto("ABC", 123) # tämä olio

print (f"{auto.rekisteri:s} {auto.huippunopeus:s} {auto.nopeus:d} {auto.matka:d}")  # olien ominaisuuksien tulos
