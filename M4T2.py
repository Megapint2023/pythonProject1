# Kirjoita ohjelma, joka muuntaa tuumia senttimetreiksi niin kauan kunnes käyttäjä antaa negatiivisen tuumamäärän.
# Sen jälkeen ohjelma lopettaa toimintansa. 1 tuuma = 2,54 cm

print ("Muunna tuumat -> senttimetreiksi.")
value = 0
while value >= 0:
    value = float(input("Syötä tuumien määrä: "))
    number = value * 2.54
    print(str(number) + "tuumaa.")
    if value < 0:
        break
# Koodi: Muuttujan alkuarvo = 0 ja toistolause pyörii niin kauan kunnes näin on.
# Sen jälkeen laskukaava sekä printtaus.
# Lopuksi ehto jolla ohjelma pysähtyy, eli mikäli tulostuu negatiivinen arvo.