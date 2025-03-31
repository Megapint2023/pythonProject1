# Kirjoita aiemmin laatimallesi Auto-luokalle aliluokat Sähköauto ja Polttomoottoriauto.
# Sähköautolla on ominaisuutena akkukapasiteetti kilowattitunteina.
# Polttomoottoriauton ominaisuutena on bensatankin koko litroina.
# Kirjoita aliluokille alustajat.
# Esimerkiksi sähköauton alustaja saa parametreinaan rekisteritunnuksen,
# huippunopeuden ja akkukapasiteetin.
# Se kutsuu yliluokan alustajaa kahden ensin mainitun asettamiseksi
# sekä asettaa oman kapasiteettinsa. Kirjoita pääohjelma,
# jossa luot yhden sähköauton (ABC-15, 180 km/h, 52.5 kWh)
# ja yhden polttomoottoriauton (ACD-123, 165 km/h, 32.3 l).
# Aseta kummallekin autolle haluamasi nopeus,
# käske autoja ajamaan kolmen tunnin verran ja tulosta autojen matkamittarilukemat.


class Auto:
    def __init__(self, rekisteri, huippunopeus):
        self.rekisteri = rekisteri
        self.huippunopeus = huippunopeus

    def tulosta_tiedot(self):
        print(f" - Auton rekisteri: {self.rekisteri}")
        print(f" - Auton huippunopeus: {self.huippunopus} km/h.")

class Sähkö(Auto):
    def __init__(self, rekisteri, huippunopeus, kapasiteetti):
        super().__init__(rekisteri, huippunopeus)
        self.kapasitettti = kapasiteetti # kWh

    def tulosta_tiedot(self):
        super().tulosta_tiedot()
        print(f' - Akun kapasiteetti tyyppi: {self.kapasiteetti}')
        print(f"-")

class Polttomoottori(Auto):
    def __init__(self, rekisteri, huippunopeus, moottorinkoko):
        super().__init__(rekisteri, huippunopeus)
        self.moottorinkoko = moottorinkoko

    def tulosta_tiedot(self):
        super().tulosta_tiedot()
        print(f' - Moottorikoko litraa: {self.moottorinkoko}')

autot = []
autot.append(Sähkö('ABC-15', 180, 52.5))
autot.append(Polttomoottori("ACD-123", 165, 32.3))

for auto in autot:
    auto.tulosta_tiedot()
    print()