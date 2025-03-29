#Jatka edellisen tehtävän ohjelmaa siten,
# että Talo-luokassa on parametriton metodi palohälytys,
# joka käskee kaikki hissit pohjakerrokseen. Jatka pääohjelmaa siten,
# että talossasi tulee palohälytys.

class Hissi:
    def __init__(self, alin, ylin): # alustaja / constructor
        # ominaisuudet / properties
        self.kerros = 0
        self.ylin = ylin
        self.alin = alin

    def liiku_ylos(self): #metodi
        if self.kerros < self.ylin:
            self.kerros += 1
            print(f"Siirtyy ylöspäin...")
            print(f"Kerros: {self.kerros}.")

    def liiku_alas(self): #metodi
        if self.kerros > self.alin:
            self.kerros -= 1
            print(f"Siirtyy alaspäin...")
            print(f"Kerros: {self.kerros}.")

    def siirry_kerrokseen(self, kohdekerros): #metodi
        while self.kerros < kohdekerros:
            self.liiku_ylos()
        while self.kerros > kohdekerros:
            self.liiku_alas()

class Talo:
    def __init__(self, hissi_määrä, alin, ylin):
        self.alin = alin
        self.ylin = ylin
        self.hissit = []

        for i in range(hissi_määrä):
            self.hissit.append(Hissi(alin, ylin))

    def aja_hissiä(self, hissi_nro, kohdekerros):
            print(f"Hissi nro. {hissi_nro} lähtee kerrokseen: {kohdekerros}")
            self.hissit[hissi_nro].siirry_kerrokseen(kohdekerros)

    def palohälytys(self):
        print(f"PALOHÄLYTYS! 🔥🔥🔥") # emojit voi myös kirjoittaa {fire}
        for i, hissi in enumerate(self.hissit): # enumerate on funktio joka lisää indexing listan jokaiselle itemille
            print(f"Hissi nro. {i} ")
            hissi.siirry_kerrokseen(0)

talo = Talo(4, 0, 5)
talo.aja_hissiä(1, 5)
talo.aja_hissiä(2, 4)
talo.aja_hissiä(3, 3)
talo.palohälytys()