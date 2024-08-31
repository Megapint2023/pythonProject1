# Kirjoita peli, jossa tietokone arpoo kokonaisluvun väliltä 1..10.
# Kone arvuuttelee lukua pelaajalta siihen asti, kunnes tämä arvaa oikein.
# Kunkin arvauksen jälkeen ohjelma tulostaa tekstin Liian suuri arvaus, Liian pieni arvaus tai Oikein.
# Huomaa, että tietokone ei saa vaihtaa lukuaan arvauskertojen välissä.

print ("Arvaa numero väliltä 1-10")
import random
secret_number = random.randint(1, 10)

while True:
    arvaus = input("Syötä uusi numero: ")
    arvaus = int(arvaus)

    if arvaus == secret_number:
        print ("Oikein!")
        break

    elif arvaus < secret_number:
        print ("Väärin, luku on suurempi. Arvaa uudestaan!")
    elif arvaus > secret_number:
        print ("Väärin, luku on pienempi. Arvaa uudestaan!")
