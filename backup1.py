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

COLORS = [
    "\033[91m",  # Red
    "\033[92m",  # Green
    "\033[93m",  # Yellow
    "\033[94m",  # Blue
    "\033[95m",  # Magenta
    "\033[96m",  # Cyan
    "\033[97m",  # White
]
RESET = "\033[0m"  # Reset color to default

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
        self.nopeus = 100 # alkunopeutta nostettu toimivuuden vuoksi, jotkut autoista jos saavat esim neg arvon kolmesti, ne eivät muka liiku 30h aikana... ei järkeä
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
        huippunopeus = random.randint(150, 200)
        autot.append(Auto(rekisteri, huippunopeus, name))
    return autot

autot = luo_autot()
kilpailu = Kilpailu("Suuri Romuralli", 8000, autot)
kilpailu_jatkuu = True
aikaa_kulunut = 0

previous_positions = {auto: i for i, auto in enumerate(kilpailu.autot)}

while kilpailu_jatkuu:
    for auto in kilpailu.autot:
        auto.kiihdytys()
        auto.kulje(1)
        if auto.matka >= 8000:
            kilpailu_jatkuu = False
            break
    aikaa_kulunut += 1

    if aikaa_kulunut % 10 == 0:
        kilpailu.autot.sort(key=lambda x: x.matka, reverse=True)
        print("🔥🔥🔥 Suuri Romuralli 🔥🔥🔥")
        print(f"⏳Tilanne {aikaa_kulunut} tunnin kohdalla...")
        print(f"{'Sijoitus:':<10}{'Auto:':<13}{'Rekisteri:':<12}{'Huippunopeus:':<14}{'Nopeus:':<15}{'Kuljettu matka:'}")
        previous_positions = {auto: i for i, auto in enumerate(kilpailu.autot)}
        for index, auto in enumerate(kilpailu.autot, start=1):
            car_color = COLORS[index % len(COLORS)]
            print(f"{car_color}{index:<10}{auto.name:<13}{auto.rekisteri:<12}{auto.huippunopeus:<14}{auto.nopeus:<15}{auto.matka:.2f} km{RESET}")


kilpailu.autot.sort(key=lambda x: x.matka, reverse=True)

print("\n🏁🏁🏁 Sijoitukset! 🏁🏁🏁")
print(f"Kilpailuun kulunut aika: {aikaa_kulunut} tuntia.\n")
print(f"{'Sijoitus:':<10}{'Auto:':<13}{'Rekisteri:':<12}{'Huippunopeus:':<14}{'Nopeus:':<15}{'Kuljettu matka:':}")
for index, auto in enumerate(kilpailu.autot, start=1):
    car_color = COLORS[index % len(COLORS)]
    print(f"{car_color}{index:<10}{auto.name:<13}{auto.rekisteri:<12}{auto.huippunopeus:<14}{auto.nopeus:<15}{auto.matka:.2f} km{RESET}")
#for index, auto in enumerate(kilpailu.autot, start=1):
#    print(f"{index:<10}{auto.name:<13}{auto.rekisteri:<12}{auto.huippunopeus:<14}{auto.nopeus:<20}{auto.matka:.2f} km")