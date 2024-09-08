#Kirjoita ohjelma, joka kysyy kolme kokonaislukua.
#Ohjelma tulostaa lukujen summan, tulon ja keskiarvon.

print ("Syötä kolme kokonaislukua.")
value1 = float(input("Luku1: "))
value2 = float(input("Luku2: "))
value3 = float(input("Luku3: "))

summa = value1 + value2 + value3
multi = value1 * value2 * value3
average = value1 + value2 + value3 / 3

print ("Lukujen summa on: " + str(summa))
print ("Lukujen tulo on: " + str(multi))
print ("Lukujen keskiarvo on: " + str(average))