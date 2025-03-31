# Toteuta seuraava luokkahierarkia Python-kielellä: Julkaisu voi olla kirja tai lehti.
# Jokaisella julkaisulla on nimi. Kirjalla on lisäksi kirjoittaja ja sivumäärä,
# kun taas lehdellä on päätoimittaja. Kirjoita luokkiin myös tarvittavat alustajat.
# Tee aliluokkiin metodi tulosta_tiedot, joka tudostaa kyseisen julkaisun kaikki tiedot.
# Luo pääohjelmassa julkaisut Aku Ankka (päätoimittaja Aki Hyyppä) ja Hytti n:o 6 (kirjailija Rosa Liksom, 200 sivua).
# Tulosta molempien julkaisujen kaikki tiedot toteuttamiesi metodien avulla.



class Julkaisu:

    julkaisujen_lukumäärä = 0

    def __init__(self, etunimi, sukunimi, julkaisun_nimi, julkaisun_tyyppi, sivumäärä):
        Julkaisu.julkaisujen_lukumäärä += 1
        self.etunimi = etunimi
        self.sukunimi = sukunimi
        self.julkaisun_nimi = julkaisun_nimi
        self.julkaisun_tyyppi = julkaisun_tyyppi
        self.sivumäärä = sivumäärä

    def tulosta_tiedot(self):
        print(f"{self.etunimi} {self.sukunimi} {self.julkaisun_nimi} {self.julkaisun_tyyppi} {self.sivumäärä}")

class Julkaise_kirja(Julkaisu):
    def __init__(self, etunimi, sukunimi, julkaisun_nimi, julkaisun_tyyppi, sivumäärä):
        super().__init__(etunimi, sukunimi, julkaisun_nimi, julkaisun_tyyppi, sivumäärä)

    def tulosta_tiedot(self):
        super().tulosta_tiedot()
        print(f' - Julkaistu kirja: {self.kirja}')

class Julkaise_lehti(Julkaisu):
    def __init__(self, etunimi, sukunimi, julkaisun_nimi, julkaisun_tyyppi, sivumäärä):
        super().__init__(etunimi, sukunimi, julkaisun_nimi, julkaisun_tyyppi, sivumäärä)

    def tulosta_tiedot(self):
        super().tulosta_tiedot()
        print(f' - Julkaistu lehti: {self.lehti}')


julkaisut = []
julkaisut.append(Julkaisu("Viivi", "Virta"))
julkaisut.append(Julkaisu("Ahmed", "Habib"))

julkaisut.append(Julkaise_kirja('Pertti', 'Kaski', 50.0))
julkaisut.append(Julkaise_lehti('Iina', 'Kekkiläinen', 5000.0))

for j in julkaisut:
    j.tulosta_tiedot()



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
