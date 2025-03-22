#Jatka ohjelmaa kirjoittamalla Auto-luokkaan kiihdytä-metodi,
# joka saa parametrinaan nopeuden muutoksen (km/h).
# Jos nopeuden muutos on negatiivinen, auto hidastaa.
# Metodin on muutettava auto-olion nopeus-ominaisuuden arvoa.
# Auton nopeus ei saa kasvaa huippunopeutta suuremmaksi eikä alentua nollaa pienemmäksi.
# Jatka pääohjelmaa siten, että auton nopeutta nostetaan ensin +30 km/h, sitten +70 km/h ja lopuksi +50 km/h.
# Tulosta tämän jälkeen auton nopeus.
# Tee sitten hätäjarrutus määräämällä nopeuden muutos -200 km/h ja tulosta uusi nopeus.
# Kuljettua matkaa ei tarvitse vielä päivittää.
# 19.03.2025

class Auto: # tämä class
    def __init__(self, rekisteri, huippunopeus): # tämä alustaja
        # ominaisuudet
        self.rekisteri = rekisteri
        self.huippunopeus = huippunopeus
        self.nopeus = 0
        self.matka = 0

    def kiihdytys(self):
        for i in range(10):
            self.nopeus += 10
            if self.nopeus > self.huippunopeus:
                self.nopeus = self.huippunopeus
            elif self.nopeus < 0:
                self.nopeus = 0
            print(f"Nopeus: {self.nopeus} km/h")

auto = Auto("ABC-123", 142) # tämä on olio/object
print (f"Auton tiedot -> Rekisterinumero: {auto.rekisteri}, Huippunopeus {auto.huippunopeus} km/h, Nopeus nyt: {auto.nopeus} km/h.")  # olien ominaisuuksien tulos

print (f"Auto kiihdyttää...")
for i in range(3):
    auto.kiihdytys()
