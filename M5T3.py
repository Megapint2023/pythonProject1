# Kirjoita ohjelma, joka kysyy käyttäjältä kokonaisluvun ja ilmoittaa, onko se alkuluku.
# Tässä tehtävässä alkulukuja ovat luvut, jotka ovat jaollisia vain ykkösellä ja itsellään.
# Esimerkiksi luku 13 on alkuluku, koska se voidaan jakaa vain luvuilla 1 ja 13 siten,
# että jako menee tasan.
# Toisaalta esimerkiksi luku 21 ei ole alkuluku, koska se voidaan jakaa tasan myös luvulla 3 tai luvulla 7.


alkuluku = True

while True:
    luku = input("Syötä luku: ")
    luku = int(luku)
    if luku < 1:
        print("Virheellinen positiivinen kokonaisluku.")
    else:
        break

if luku == 1:
    alkuluku = False
else:
    for x in range(2, luku):
        if luku % x == 0:
            alkuluku = False
            break

if alkuluku:
    print (str(luku) + " on alkuluku!")
else:
    print(str(luku) + " ei ole alkuluku.")
