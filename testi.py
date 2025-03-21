#class Koira:
#    pass
#
#koira = Koira()
#koira.nimi = "Rekku"
#koira.syntymavuosi = 2022
#
#print (f"{koira.nimi:s} on syntynyt vuonna {koira.syntymavuosi:d}.")

class Koira:
    def __init__(self, nimi, syntymävuosi):
        self.nimi = nimi
        self.syntymävuosi = syntymävuosi

koira = Koira("Rekku", 2022)

print (f"{koira.nimi:s} on syntynyt vuonna {koira.syntymävuosi:d}." )
