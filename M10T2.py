# Jatka edellisen tehtävän ohjelmaa siten, että teet Talo-luokan.
# Talon alustajaparametreina annetaan alimman ja ylimmän kerroksen numero sekä hissien lukumäärä.
# Talon luonnin yhteydessä talo luo tarvittavan määrän hissejä.
# Hissien lista tallennetaan talon ominaisuutena. Kirjoita taloon metodi aja_hissiä,
# joka saa parametreinaan hissin numeron ja kohdekerroksen.
# Kirjoita pääohjelmaan lauseet talon luomiseksi ja talon hisseillä ajelemiseksi.

class Hissi:
    def __init__(self, alin, ylin): # alustaja / constructor
        # ominaisuudet / properties
        self.kerros = 0
        self.ylin = ylin
        self.alin = alin

    def liiku_ylos(self): #metodi
        if self.kerros < self.ylin:
            self.kerros += 1
            print(f"Hissi liikkuu ylöspäin.")
            print(f"Saapui kerrokseen: {self.kerros}.")

    def liiku_alas(self): #metodi
        if self.kerros > self.alin:
            self.kerros -= 1
            print(f"Hissi liikkuu alaspäin.")
            print(f"Saapui kerrokseen: {self.kerros}.")

    def siirry_kerrokseen(self, kohdekerros): #metodi
        while self.kerros < kohdekerros:
            self.liiku_ylos()
        while self.kerros > kohdekerros:
            self.liiku_alas()
            print(f"Hissi saapui kerrokseen: {self.kerros}.")

class Talo:
    def __init__(self, hissi_määrä, alin, ylin):
        self.alin = alin
        self.ylin = ylin
        self.hissit = []

        for i in range(hissi_määrä):
            self.hissit.append(Hissi(alin, ylin))

    def aja_hissiä(self, hissi_nro, kohdekerros):
            print(f"Hissi nro. {hissi_nro} lähtee kerrokseen: {kohdekerros}:")
            self.hissit[hissi_nro].siirry_kerrokseen(kohdekerros)

talo = Talo(3, 0, 5)
talo.aja_hissiä(0, 5)
talo.aja_hissiä(1, 4)
talo.aja_hissiä(2, 3)
