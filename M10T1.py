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
    def __init__(self, alin, ylin): # alustaja
        # ominaisuudet
        self.kerros = 0
        self.ylin = ylin
        self.alin = alin

    def liiku_ylos(self): #metodi
        if self.kerros < self.ylin:
            self.kerros += 1
            print(f"Kerroksessa: {self.kerros}.")

    def liiku_alas(self): #metodi
        if self.kerros > self.alin:
            self.kerros -= 1
            print(f"Kerroksessa: {self.kerros}.")

    def h(self): #metodi
        while self.kerros < self.ylin:
            self.liiku_ylos()
        while self.kerros > self.alin:
            self.liiku_alas()

hissi = Hissi(0, 5)
hissi.h()


