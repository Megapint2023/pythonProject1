#class Koira:
#    def __init__(self, nimi, syntymävuosi, age, info):
#        self.nimi = nimi
#        self.syntymävuosi = syntymävuosi
#        self.age = age
#        self.info = info
#
#    def hauku (self, kerrat):
#        for i in range(kerrat):
#            print(self.haukahdus)
#        return
#
#
#koira = Koira("Rekku", 2022, 18, "Tuntomerkit: *punainen kaularengas*.")
#
#print (f"{koira.nimi:s} on syntynyt vuonna {koira.syntymävuosi:d}. Hänen ikä on {koira.age:d} vuotta. {koira.info:s}" )

class Koira:
    tehty = 0
    def __init__(self, nimi, syntymävuosi, haukahdus="Woof woof!"):
        self.nimi = nimi
        self.syntymävuosi = syntymävuosi
        self.haukahdus = haukahdus
        Koira.tehty = Koira.tehty + 1

    def hauku(self, kerrat):
        print(f"{self.nimi} wuff!")
        for i in range(kerrat):
            print(f"{self.haukahdus} {i+1}. kerran")
        return
    def annaNimi(self):
        return self.nimi

    def asetaNimi(self, nimi):
        self.nimi = nimi


koira1 = Koira("Muro", 2018)
koira2 = Koira("Rekku", 2022, "Hou!")
koira3 = Koira("Beibi", 2010, "Hau!")

print(f"{koira1.annaNimi()} on syntynyt {koira1.syntymävuosi}.")
koira1.hauku(2)
koira2.hauku(5)
koira3.hauku(4)


print(koira1.annaNimi())
koira1.asetaNimi("Leidi")
print(koira1.annaNimi())
koira1.nimi = "Peka"
print(koira1.nimi)

print(koira2.annaNimi())
koira2.nimi = "Yeha"
print(koira2.nimi)

print(koira3.annaNimi())
koira3.nimi = "Kel"
print(koira3.nimi)

print(koira1.nimi)
koira1.asetaNimi(f"Koiria on nyt {Koira.tehty}.")
print(koira1.annaNimi())
del koira1