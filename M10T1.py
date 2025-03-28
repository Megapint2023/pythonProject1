#Kirjoita Hissi-luokka, joka saa alustajaparametreinaan alimman ja ylimmän kerroksen numeron.
# Hissillä on metodit siirry_kerrokseen, kerros_ylös ja kerros_alas.
# Uusi hissi on aina alimmassa kerroksessa.
# Jos tee luodulle hissille h esimerkiksi metodikutsun h.siirry_kerrokseen(5),
# metodi kutsuu joko kerros_ylös- tai kerros_alas-metodia niin monta kertaa,
# että hissi päätyy viidenteen kerrokseen.
# Viimeksi mainitut metodit ajavat hissiä yhden kerroksen ylös- tai alaspäin ja ilmoittavat,
# missä kerroksessa hissi sen jälkeen on. Testaa luokkaa siten,
# että teet pääohjelmassa hissin ja käsket sen siirtymään haluamaasi kerrokseen ja
# sen jälkeen takaisin alimpaan kerrokseen.

class Hissi:
    def __init__(self, alin, ylin, kerros): # alustaja
        # ominaisuudet
        self.kerros = 0
        self.ylin = 5
        self.alin = 0

    def liiku_ylos(self):
        self.kerros = self.kerros + 1

    def h(self): #metodi
        self.kerros = 5

    def liiku(self):
        muutos = random.randint(, 15)
        self.kerros += muutos
        if self.nopeus > self.huippunopeus:
            self.nopeus = self.huippunopeus
        elif self.nopeus < 0:
            self.nopeus = 0

    def kulje(self, aika):
        self.matka += self.nopeus * aika
    def kerros(self):
        self.kerros = (0, 10)
        if self.kerros == 5:
            break
        elif self.kerros >= 10
            self.kerros =ylin

