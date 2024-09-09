# Kirjoita ohjelma, joka kysyy käyttäjältä nimiä siihen saakka,
# kunnes käyttäjä syöttää tyhjän merkkijonon.
# Kunkin nimen syöttämisen jälkeen ohjelma tulostaa joko tekstin Uusi nimi tai Aiemmin syötetty nimi sen mukaan,
# syötettiinkö nimi ensimmäistä kertaa.
# Lopuksi ohjelma printtaa sisällön sattumanvaraisesti ->
# Käytä joukkotietorakennetta nimien tallentamiseen.

#joukkotietorakenne
# Python: "set" =
# Tallentaa tietoa kuten muutkin listat listat, mutta


 jemma = set()

 while True:
     nimi = input("Lisää uusi nimi: (lopeta painamalla 'enter':")
     if nimi == "":
        break
     if nimi in jemma:
         print(f"Virhe! {nimi} löytyy jo!  .")
     else:
         jemma.add(nimi)
         print(f"Uusi nimi: -{nimi}-->  nimi lisätty jemmaan!")

print(jemma)



#minisetti = {"nimi1", "nimi2", "nimi3"}
#print(minisetti)
#
#minisetti.add("Dominion")
#print(minisetti)
#
#minisetti.remove("Shakki")
#print(minisetti)
#
#minisetti.add("Cluedo")
#print(minisetti)
#
#for p in minisetti:
#    print(p)
#

