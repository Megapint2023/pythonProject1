# Toteuta seuraava luokkahierarkia Python-kielellä: Julkaisu voi olla kirja tai lehti.
# Jokaisella julkaisulla on nimi. Kirjalla on lisäksi kirjoittaja ja sivumäärä,
# kun taas lehdellä on päätoimittaja. Kirjoita luokkiin myös tarvittavat alustajat.
# Tee aliluokkiin metodi tulosta_tiedot, joka tudostaa kyseisen julkaisun kaikki tiedot.
# Luo pääohjelmassa julkaisut Aku Ankka (päätoimittaja Aki Hyyppä) ja Hytti n:o 6 (kirjailija Rosa Liksom, 200 sivua).
# Tulosta molempien julkaisujen kaikki tiedot toteuttamiesi metodien avulla.



class Julkaisut:

    julkaisujen_lukumäärä = 0

    def __init__(self, etunimi, sukunimi, julkaisun_nimi, julkaisun_tyyppi, sivumäärä):
        Julkaisut.julkaisujen_lukumäärä += 1
        self.etunimi = etunimi
        self.sukunimi = sukunimi
        self.julkaisun_nimi = julkaisun_nimi
        self.julkaisun_tyyppi = julkaisun_tyyppi
        self.sivumäärä = sivumäärä

    def tulosta_tiedot(self):
        print(f"{self.etunimi} {self.sukunimi} {self.julkaisun_nimi} {self.julkaisun_tyyppi} {self.sivumäärä}")

class Julkaise_kirja(Julkaisut):
    def __init__(self, etunimi, sukunimi, julkaisun_nimi, julkaisun_tyyppi, sivumäärä):
        super().__init__(etunimi, sukunimi, julkaisun_nimi, julkaisun_tyyppi, sivumäärä)

    def tulosta_tiedot(self):
        super().tulosta_tiedot()
        print(f' - Tuntipalkka on {self.tuntipalkka}')

class Julkaise_Lehti(Julkaisut):
    def __init__(self, etunimi, sukunimi, kuukausipalkka):
        super().__init__(etunimi, sukunimi)
        self.kuukausipalkka = kuukausipalkka

    def tulosta_tiedot(self):
        super().tulosta_tiedot()
        print(f' - Kuukausipalkka on {self.kuukausipalkka}')




työntekijät = []
työntekijät.append(Työntekijä("Viivi", "Virta"))
työntekijät.append(Työntekijä("Ahmed", "Habib"))

työntekijät.append(Tuntipalkkainen('Pertti', 'Kaski', 50.0))
työntekijät.append(Kuukausipalkkainen('Iina', 'Kekkiläinen', 5000.0))

for t in työntekijät:
    t.tulosta_tiedot()



#class Julkaisu:
#    def __init__(self, tyyppi, nimi, tuottaja, sivumäärä):
#        self.tyyppi = tyyppi
#        self.nimi = nimi
#        self.tuottaja = tuottaja
#        self.sivumäärä = sivumäärä
#
#    def generate(self):
#        print(f"{Julkaisu.tyyppi()}, {Julkaisu.nimi()}, {Julkaisu.tuottaja()}, {Julkaisu.sivumäärä()}.")
#
#
#julkaisu1.generate("Kirja", "Meikäläiset", "Ella Bella", 135)
