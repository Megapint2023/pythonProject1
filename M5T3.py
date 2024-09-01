# Kirjoita ohjelma, joka kysyy käyttäjältä kokonaisluvun ja ilmoittaa, onko se alkuluku.
# Tässä tehtävässä alkulukuja ovat luvut, jotka ovat jaollisia vain ykkösellä ja itsellään.
# Esimerkiksi luku 13 on alkuluku, koska se voidaan jakaa vain luvuilla 1 ja 13 siten,
# että jako menee tasan.
# Toisaalta esimerkiksi luku 21 ei ole alkuluku, koska se voidaan jakaa tasan myös luvulla 3 tai luvulla 7.


alkuluku = None

while True:
    luku = input("Syötä luku: ")
    luku = int(luku)
    if luku < 1:
        print("Virheellinen positiivinen kokonaisluku.")
    else:
        break

if luku == luku and luku % 1 == 0:
    luku = alkuluku
    print (str(alkuluku) + " on alkuluku!")
