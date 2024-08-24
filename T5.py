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

x = 20 * y
y = 32 * b
b = 13.3

print ("Syötä leivisköjen, naulojen ja luotien määrä.")
x = float(input("Leivisköjen kpl määrä: "))
y = float(input("Naulojen kpl määrä: "))
b = float(input("Luotien kpl määrä: "))


