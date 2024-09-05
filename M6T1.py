# Kirjoita parametriton funktio, joka palauttaa paluuarvonaan satunnaisen
# nopan silmäluvun väliltä 1..6.
# Kirjoita pääohjelma, joka heittää noppaa niin kauan kunnes tulee kuutonen.
# Pääohjelma tulostaa kunkin heiton jälkeen saadun silmäluvun.

#parametriton eli ilman numero arvoa
# jos laitan funtkioon muuttujan se ei ole numero arvo
# eli voin tehdä näin ->

def parametriton(noppa):
    numero = noppa
    return numero

parametriton()
import random
noppa = random.randint(1, 6)
print(parametriton)
