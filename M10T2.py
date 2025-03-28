# Jatka edellisen tehtävän ohjelmaa siten, että teet Talo-luokan.
# Talon alustajaparametreina annetaan alimman ja ylimmän kerroksen numero sekä hissien lukumäärä.
# Talon luonnin yhteydessä talo luo tarvittavan määrän hissejä.
# Hissien lista tallennetaan talon ominaisuutena. Kirjoita taloon metodi aja_hissiä,
# joka saa parametreinaan hissin numeron ja kohdekerroksen.
# Kirjoita pääohjelmaan lauseet talon luomiseksi ja talon hisseillä ajelemiseksi.

class Hissi:
    def __init__(self, alin, ylin): # alustaja
        # ominaisuudet
        self.kerros = 0
        self.ylin = ylin
        self.alin = alin

    def liiku_ylos(self): #metodi
        if self.kerros < self.ylin:
            self.kerros += 1
            print(f"Hissi liikkui ylöspäin.")
            print(f"Saavui kerrokseen: {self.kerros}.")

    def liiku_alas(self): #metodi
        if self.kerros > self.alin:
            self.kerros -= 1
            print(f"Hissi liikkui alaspäin.")
            print(f"Saavui kerrokseen: {self.kerros}.")

    def h(self): #metodi
        while self.kerros < self.ylin:
            self.liiku_ylos()
        while self.kerros > self.alin:
            self.liiku_alas()

hissi = Hissi(0, 5)
hissi.h()