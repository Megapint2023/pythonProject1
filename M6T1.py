# Kirjoita parametriton funktio, joka palauttaa paluuarvonaan satunnaisen
# nopan silmäluvun väliltä 1..6.
# Kirjoita pääohjelma, joka heittää noppaa niin kauan kunnes tulee kuutonen.
# Pääohjelma tulostaa kunkin heiton jälkeen saadun silmäluvun.

#parametriton eli ilman numero arvoa
# jos laitan funtkioon muuttujan se ei ole numero arvo
# eli voin tehdä näin ->
import random

def parametriton():
    while True:
        nopanheitto = random.randint (1, 6 )

        if nopanheitto == 6:
            print(str(nopanheitto) + " -> Sä osuit!")
            break
        else:
            print ("Heitit: " + str(nopanheitto) + ":n")

parametriton()

