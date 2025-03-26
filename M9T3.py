# Laajenna ohjelmaa siten, että mukana on kulje-metodi, joka saa parametrinaan tuntimäärän.
# Metodi kasvattaa kuljettua matkaa sen verran kuin auto on tasaisella vauhdilla annetussa tuntimäärässä edennyt.
# Esimerkki: auto-olion tämänhetkinen kuljettu matka on 2000 km. Nopeus on 60 km/h.
# Metodikutsu auto.kulje(1.5) kasvattaa kuljetun matkan lukemaan 2090 km.
# 19.03.2025

class Auto: # tämä class
    def __init__(self, rekisteri, huippunopeus): # tämä alustaja
        # ominaisuudet
        self.rekisteri = rekisteri
        self.huippunopeus = huippunopeus
        self.nopeus = 60
        self.matka = 2000

    #def kiihdytys(self):
    #    self.nopeus += 10 # nopeus nousee +10km/h per metodin käyttö
    #    if self.nopeus > self.huippunopeus: # poikkeus huippunopeuteen saavuttaesssa
    #        self.nopeus = self.huippunopeus
    #    elif self.nopeus < 0:
    #        self.nopeus = 0
    #        print(f"Nopeus: {self.nopeus} km/h")
#
    #def jarrutus(self):
    #    self.nopeus -= 10
    #    if self.nopeus < 0:
    #        self.nopeus = 0

    def kulje(self, matka, aika):
        self.matka = matka
        self.aika = aika

auto = Auto("ABC-123", 142) # tämä on olio/object
print (f"Auton tiedot -> Rekisterinumero: {auto.rekisteri}, Huippunopeus {auto.huippunopeus} km/h, Nopeus nyt: {auto.nopeus} km/h.")  # olien ominaisuuksien tulos

print (f"Auton kilometrilukema: {auto.matka} km.")

print(f"Auton uusi nopeus: {auto.nopeus} km/h.")

print (f"Matkan jälkeen uusi kilometrilukema on.")



