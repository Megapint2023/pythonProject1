# Kirjoita funktio, jonka parametrinä on kokonaisluvut
# Ohjelma palauttaa toisen listan, jossa vain parilliset
# Kirjoita pääohjelma + funktiota
# Tulosta molemmat listat


def alikaks():
    print(parilliset)

def aliyks():
    print(kaikkiluvut)
    return alikaks()

print ("Ohjelma tulostaa 2x listaa. Kaikki / vain parittomat numerot.")

kaikkiluvut = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
parilliset = [2,4,6,8,10,12,14,16,18,20]


aliyks()


