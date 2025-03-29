# Tehtävä on jatkoa aiemmalle autokilpailutehtävälle.
# Kirjoita Kilpailu-luokka, jolla on ominaisuuksina kilpailun nimi,
# pituus kilometreinä ja osallistuvien autojen lista. Luokassa on alustaja,
# joka saa parametreinaan nimen, kilometrimäärän ja autolistan ja asettaa ne ominaisuuksille arvoiksi.
# Luokassa on seuraavat metodit:
#tunti_kuluu, joka toteuttaa aiemmassa autokilpailutehtävässä mainitut tunnin välein
# tehtävät toimenpiteet eli arpoo kunkin auton nopeuden muutoksen
# ja kutsuu kullekin autolle kulje-metodia.
# tulosta_tilanne, joka tulostaa kaikkien autojen sen hetkiset tiedot selkeäksi taulukoksi muotoiltuna.
# kilpailu_ohi, joka palauttaa True,
# jos jokin autoista on maalissa eli se on ajanut vähintään kilpailun kokonaiskilometrimäärän.
# Muussa tapauksessa palautetaan False.

# Kirjoita pääohjelma, joka luo 8000 kilometrin kilpailun nimeltä "Suuri romuralli".
# Luotavalle kilpailulle annetaan kymmenen auton lista samaan tapaan kuin aiemmassa tehtävässä.
# Pääohjelma simuloi kilpailun etenemistä kutsumalla toistorakenteessa tunti_kuluu-metodia,
# jonka jälkeen aina tarkistetaan kilpailu_ohi-metodin avulla, onko kilpailu ohi.
# Ajantasainen tilanne tulostetaan tulosta tilanne-metodin avulla kymmenen tunnin välein
# sekä kertaalleen sen jälkeen, kun kilpailu on päättynyt.

import random

class Kilpailu:
    def __init__(self, nimi, pituus, autot):
        self.nimi = nimi
        self.pituus = pituus
        self.autot = autot
        self.osallistujat = []

class Auto: # tämä class
    def __init__(self, rekisteri, huippunopeus, name): # tämä alustaja
        # ominaisuudet
        self.name = name
        self.rekisteri = rekisteri
        self.huippunopeus = huippunopeus
        self.nopeus = 0
        self.matka = 0

    def kiihdytys(self):
        muutos = random.randint(-10, 15)
        self.nopeus += muutos
        if self.nopeus > self.huippunopeus:
            self.nopeus = self.huippunopeus
        elif self.nopeus < 0:
            self.nopeus = 0

    def kulje(self, aika):
        self.matka += self.nopeus * aika

def luo_autot():
    autot = []
    merkit = ["Toyota", "Mercedes", "BMW", "Audi", "Ford", "Chevrolet", "Honda", "Nissan", "Porsche", "Volkswagen"]
    for i in range(1, 11):
        name = random.choice(merkit)
        merkit.remove(name)
        rekisteri = f"ABC-{i}"
        huippunopeus = random.randint(100, 200)
        autot.append(Auto(rekisteri, huippunopeus, name))
    return autot

autot = luo_autot()
kilpailu_jatkuu = True
aikaa_kulunut = 0

while kilpailu_jatkuu:
    for auto in autot:
        auto.kiihdytys()
        auto.kulje(1)

        if auto.matka >= 8000:
            kilpailu_jatkuu = False
            break

    aikaa_kulunut += 1

autot.sort(key=lambda x: x.matka, reverse=True)

print("\n🏁 Sijoitukset! 🏁")
print(f"Kilpailuun kulunut aika: {aikaa_kulunut} tuntia.\n")
print(f"{'Sijoitus:':<10}{'Auto:':<13}{'Rekisteri:':<12}{'Huippunopeus:':<14}{'Lopullinen nopeus:':<20}{'Kuljettu matka:':}")
for index, auto in enumerate(autot, start=1):
    print(f"{index:<10}{auto.name:<13}{auto.rekisteri:<12}{auto.huippunopeus:<14}{auto.nopeus:<20}{auto.matka:.2f} km")