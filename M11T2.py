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
    def __init__(self, nimi):
        self.nimi = nimi

    def tulosta_tiedot(self, tyyppi):
        self.tyyppi = tyyppi
        print(f" - Auton tyyppi: {self.tyyppi}")

class sähkö(Auto):
    def __init__(self, rekisteri, huippunopeus):
        super().__init__(Auto)
        self.rekisteri = rekisteri
        self.huippunopeus = huippunopeus
        self.kapasitettti = 0 #kWh

    def tulosta_tiedot(self):
        super().tulosta_tiedot()
        print(f' - Auton tyyppi: {self.tyyppi}, {self.sukunimi}')
        print(f' - Auton kulutus: {self.kulutus}')
        print(f"-")


class polttomoottori(Auto):
    def __init__(self, rekisteri, huippunopeus):
        super().__init__(Auto)
        self.rekisteri = rekisteri
        self.huippunopeus = huippunopeus
        self.moottorinkoko = 0 #litraa

    def tulosta_tiedot(self):
        super().tulosta_tiedot()
        print(f' - Litran moottori: {self.moottorinkoko}')


autot = []
autot.append(Auto_sähkö('ABC-15', 180, 52.5))
autot.append(Auto_polttomoottori("ACD-123", 165, 32.3))

for j in autot:
    j.tulosta_tiedot()