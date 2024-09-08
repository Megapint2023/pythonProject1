#Kirjoita ohjelma, joka kysyy käyttäjältä massan keskiaikaisten mittojen mukaan leivisköinä, nauloina ja luoteina.
#Ohjelma muuntaa syötteen täysiksi kilogrammoiksi ja grammoiksi sekä ilmoittaa tuloksen käyttäjälle.

#Yksi leiviskä on 20 naulaa.
#Yksi naula on 32 luotia.
#Yksi luoti on 13,3 grammaa.
#Esimerkki ohjelman toiminnasta:

#Anna leiviskät.
#3
#Anna naulat.
#9
#Anna luodit.
#13.5
#Massa nykymittojen mukaan:
#29 kilogrammaa ja 545.95 grammaa.

#Ohjelma pyytää siis käyttäjältä 3 arvoa ja laskee paljonko tavara painaa?

# leiviskä = x = 20y
# naula = y = 32b
# luoti = b = 13.3g

print ("Syötä leivisköjen, naulojen ja luotien määrä.")
value1 = float(input("Leivisköjen kpl määrä: "))
value2 = float(input("Naulojen kpl määrä: "))
value3 = float(input("Luotien kpl määrä: "))

b = 13.3
y = 32 * b
x = 20 * y

leivi = value1 * x
naula = value2 * y
luoti = value3 * b
total = leivi + naula + luoti

# tiedosto testi.py mallina käyttäen -> print(f"Kolmion ala on: {total:10.2f}")
# muokkasin -> 10.1f

print (f"Leivisköjen massa on: + {leivi:10.1f}" + "g")
print (f"Naulojen massa on: + {naula:10.1f}" + "g")
print (f"Luotien massa on: + {luoti:10.1f}" + "g")
# print (f"Massa yht on:  + {total:10.2f}" + "g")
# kg + g ilmoittamisessa ongelmia, ainoa ratkaisu jonka löysin ->
kilograms = int(total // 1000)
grams = total % 1000
print(f"Massa yht on: {kilograms} kg ja {grams:.1f}g")
