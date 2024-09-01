# Kirjoita ohjelma, joka kysyy käyttäjältä arpakuutioiden lukumäärän.
# Ohjelma heittää kerran kaikkia arpakuutioita ja tulostaa silmälukujen summan.
# Käytä for-toistorakennetta.

while True:
    arpakuutio = input("Arpakuutioden lukumäärä: ")
    arpakuutio = int(arpakuutio)
    if arpakuutio < 1 or arpakuutio > 1000:
        print("Virheellinen luku, syötä arvo 1 ja 1000. välillä.")
    else:
        break

numbers = []

import random
for x in range(arpakuutio): # x on loopin toimivuutta varten
    number = random.randint(1, 6)
    numbers.append(number)

total = sum(numbers)
print (numbers)
print ("Numeroiden summa yht: " + str(total))

