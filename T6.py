#Kirjoita ohjelma, joka arpoo ja tulostaa kaksi erilaista numerolukon koodia:
#kolmenumeroisen koodin, jonka kukin numeromerkki on väliltä 0..9.
#nelinumeroisen koodin, jonka kukin numeromerkki on väliltä 1..6.
#Vihje: tutustu random.randint()-funktion käyttöön.

print("Arpajaiset - Ohjelma arpoo kolminumeroisen ja nelinumeroisen luvun.")

#import random
#print(random.randint(1, 999))

#import random
#print(random.randint(1, 9999))

import random

luku1 = random.randint(0, 9)
luku2 = random.randint(0, 9)
luku3 = random.randint(0, 9)

threedig = int(f"{luku1}{luku2}{luku3}")

print(threedig)


import random

numero1 = random.randint(0, 6)
numero2 = random.randint(0, 6)
numero3 = random.randint(0, 6)
numero4 = random.randint(0, 6)

fourdig = int(f"{numero1}{numero2}{numero3}{numero4}")

print(fourdig)