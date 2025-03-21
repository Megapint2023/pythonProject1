class Koira:
    def __init__(self, nimi, syntymävuosi, haukahdus="Vuh-vuh"):
        self.nimi = nimi
        self.syntymävuosi = syntymävuosi
        self.haukahdus = haukahdus

    def hauku(self, kerrat):
        for i in range(kerrat):
            print(self.nimi + " haukkuu: " + self.haukahdus)
        return


class Hoitola:
    def __init__(self, nimi):
        self.nimi = nimi
        self.koirat = []

    def koira_sisään(self, koira):
        self.koirat.append(koira)
        print(f"Koira {koira.nimi} kirjattu sisään")
        return

    def koira_ulos(self, koira):
        self.koirat.remove(koira)
        print(koira.nimi + " kirjattu ulos")
        return

    def tervehdi_koiria(self):
        for koira in self.koirat:
            koira.hauku(1)


iines = Koira('Iines', 2025)

reiskan_hoitola = Hoitola('Reiskan koirat')
reiskan_hoitola.koira_sisään(iines)
reiskan_hoitola.koira_sisään(Koira('Minn', 2020))
reiskan_hoitola.koira_sisään(Koira('Pepi', 2018))
reiskan_hoitola.listaa_koira()
