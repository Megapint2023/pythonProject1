# Toteuta seuraava luokkahierarkia Python-kielellä: Julkaisu voi olla kirja tai lehti.
# Jokaisella julkaisulla on nimi. Kirjalla on lisäksi kirjoittaja ja sivumäärä,
# kun taas lehdellä on päätoimittaja. Kirjoita luokkiin myös tarvittavat alustajat.
# Tee aliluokkiin metodi tulosta_tiedot, joka tudostaa kyseisen julkaisun kaikki tiedot.
# Luo pääohjelmassa julkaisut Aku Ankka (päätoimittaja Aki Hyyppä) ja Hytti n:o 6 (kirjailija Rosa Liksom, 200 sivua).
# Tulosta molempien julkaisujen kaikki tiedot toteuttamiesi metodien avulla.

class Julkaisu:
    def __init__(self, tyyppi, nimi, tuottaja, sivumäärä):
        self.tyyppi = tyyppi
        self.nimi = nimi
        self.tuottaja = tuottaja
        self.sivumäärä = sivumäärä


julkaisu1 = Julkaisu("Kirja", "Meikäläiset", "Ella Bella", 135)
print(f"{Julkaisu.tyyppi()}, {Julkaisu.nimi()}, {Julkaisu.tuottaja()}, {Julkaisu.sivumäärä()}.")
