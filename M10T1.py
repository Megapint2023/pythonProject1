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
        if self.kerros >= 5:
            self.kerros = self.ylin
            print(f"Kerroksessa: {self.kerros}.")


    def liiku_alas(self):
        self.kerros = self.kerros - 1
        if self.kerros <= 0:
            self.kerros = self.alin
            print(f"Kerroksessa: {self.kerros}.")

    def h(self): #metodi
        # tämän metodi täytyy kutsua liiku_ylos metodia 5 kertaa
        # metodin "h" täytyy siis liikuttaa hissiä viidenteen kerrokseen



