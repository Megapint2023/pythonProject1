#Kirjoita ohjelma, joka kysyy vuosiluvun ja ilmoittaa, onko annettu vuosi karkausvuosi.
# Vuosi on karkausvuosi, jos se on jaollinen neljällä.
# Sadalla jaolliset vuodet ovat karkausvuosia vain jos ne ovat jaollisia myös neljälläsadalla.



# % on modulus operaattori pythonissa. Modulus operttorin tarkoitus on laskea "yli jäävä arvo"  kun luku jaetaan.
# Karkausvuoden voi laskea sen avulla -> mikäli se saa rvoksi tasan 0 käyttäen kahta ehtosääntöä
# karkusvuoden ehdot
# 1. luku on jaettavissa 4
# 2. luku on jaettavissa 100 se ei ole karkausvuosi pitsi -> jos jaettavissa 400:lla
# 3. luku on jaettavissa 400:lla -> on karkausvuosi
# Eli krkausvuosi = jaettaviss 4 ja 400:lla, muttei 100
# kaava: year = int (year % 4)


year = int(input("Syötä vuosiluku: "))
if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print("Syöttäväsi vuosiluku: " + str(year) + " on karkausvuosi")

else:
    print(str(year) + " ei ole karkausvuosi.")