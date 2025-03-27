#Nyt ohjelmoidaan autokilpailu. Uuden auton kuljettu matka alustetaan automaattisesti nollaksi.
# Tee pääohjelman alussa lista, joka koostuu kymmenestä toistorakenteella luodusta auto-oliosta.
# Jokaisen auton huippunopeus arvotaan 100 km/h ja 200 km/h väliltä.
# Rekisteritunnus luodaan seuraavasti "ABC-1", "ABC-2" jne. Sitten kilpailu alkaa.
# Kilpailun aikana tehdään tunnin välein seuraavat toimenpiteet:

#Jokaisen auton nopeutta muutetaan siten, että nopeuden muutos arvotaan väliltä -10 ja +15 km/h väliltä.
# Tämä tehdään kutsumalla kiihdytä-metodia.
#Kaikkia autoja käsketään liikkumaan yhden tunnin ajan.
# Tämä tehdään kutsumalla kulje-metodia.
#Kilpailu jatkuu, kunnes jokin autoista on edennyt vähintään 10000 kilometriä.
# Lopuksi tulostetaan kunkin auton kaikki ominaisuudet selkeäksi taulukoksi muotoiltuna.

# 19.03.2025

import random

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
        self.nopeus += muutos # nopeus nousee +10km/h per metodin käyttö
        if self.nopeus > self.huippunopeus: # poikkeus huippunopeuteen saavuttaesssa
            self.nopeus = self.huippunopeus
        elif self.nopeus < 0:
            self.nopeus = 0

    def kulje(self, aika):
        self.matka += self.nopeus * aika

def luo_autot():
    autot = []
    for i in range(1, 11):
        name = f"Car-{i}"
        rekisteri = f"ABC-{i}"
        huippunopeus = random.randint(100, 200)
        autot.append(Auto(rekisteri, huippunopeus, name))
    return autot

autot = luo_autot()
kilpailu_jatkuu = False
elapsed_time = 0

while not kilpailu_jatkuu:
    for auto in autot:
        auto.kiihdytys()
        auto.kulje(1)

        if auto.matka >= 10000:
            kilpailu_jatkuu = True
            break

    elapsed_time += 1

autot.sort(key=lambda x: x.matka, reverse=True)

print("\n🏁 Race Results 🏁")
print(f"Total race time: {elapsed_time} hours\n")
print(f"{'Sijoitus:':<10}{'Auto:':<10}{'Rekisteri:':<12}{'Huippunopeus:':<14}{'Lopullinen nopeus':<18}{'Kuljettu matka:':}")
for index, auto in enumerate(autot, start=1):
    print(f"{index:<10}{auto.name:<10}{auto.rekisteri:<12}{auto.huippunopeus:<14}{auto.nopeus:<18}{auto.matka:.2f} km")
