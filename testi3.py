class Koira:
    def __init__(self, nimi, syntymävuosi, age, info):
        self.nimi = nimi
        self.syntymävuosi = syntymävuosi
        self.age = age
        self.info = info

koira = Koira("Rekku", 2022, 18, "Tuntomerkit: *punainen kaularengas*.")

print (f"{koira.nimi:s} on syntynyt vuonna {koira.syntymävuosi:d}. Hänen ikä on {koira.age:d} vuotta. {koira.info:s}" )