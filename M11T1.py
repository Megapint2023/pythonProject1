# Toteuta seuraava luokkahierarkia Python-kielellä: Julkaisu voi olla kirja tai lehti.
# Jokaisella julkaisulla on nimi. Kirjalla on lisäksi kirjoittaja ja sivumäärä,
# kun taas lehdellä on päätoimittaja. Kirjoita luokkiin myös tarvittavat alustajat.
# Tee aliluokkiin metodi tulosta_tiedot, joka tudostaa kyseisen julkaisun kaikki tiedot.
# Luo pääohjelmassa julkaisut Aku Ankka (päätoimittaja Aki Hyyppä) ja Hytti n:o 6 (kirjailija Rosa Liksom, 200 sivua).
# Tulosta molempien julkaisujen kaikki tiedot toteuttamiesi metodien avulla.

class Julkaisu:

    julkaisujen_lukumäärä = 0

    def __init__(self, julkaisun_nimi):
        Julkaisu.julkaisujen_lukumäärä += 1
        self.julkaisun_nimi = julkaisun_nimi

    def tulosta_tiedot(self):
        print(f"{self.julkaisun_nimi}")

class Julkaise_kirja(Julkaisu):
    def __init__(self, etunimi, sukunimi, julkaisun_nimi, sivumäärä):
        super().__init__(julkaisun_nimi)
        self.sivumäärä = sivumäärä
        self.etunimi = etunimi
        self.sukunimi = sukunimi

    def tulosta_tiedot(self):
        super().tulosta_tiedot()
        print(f' - Kirjailija: {self.etunimi}, {self.sukunimi}')
        print(f' - Sivumäärä: {self.sivumäärä}')

class Julkaise_lehti(Julkaisu):
    def __init__(self, julkaisun_nimi, päätoimittaja):
        super().__init__(julkaisun_nimi)
        self.päätoimittaja = päätoimittaja

    def tulosta_tiedot(self):
        super().tulosta_tiedot()
        print(f' - Päätoimittaja: {self.lehti}')


julkaisut = []
julkaisut.append(Julkaise_kirja('Rosa', 'Liksom', "Hytti n:o 6", "Kirja", 200))
julkaisut.append(Julkaise_lehti("Aki", "Hyyppä", "Aku Ankka","Lehti:", 0))

for j in julkaisut:
    j.tulosta_tiedot()

