# Kirjoita ohjelma, joka kysyy käyttäjältä lukuja siihen saakka, kunnes tämä syöttää tyhjän merkkijonon lopetusmerkiksi.
# Lopuksi ohjelma tulostaa saaduista luvuista pienimmän ja suurimman.

# Eli käytännössä ohjelma jatkuvasti pyytää lukuarvoja, kunnes käyttäjä painaa enter.

print ("Ohjelma valitsee syötetyistä arvoista pienimmän ja suurimman.")
print ("Lopeta ohjelma painamalla enter.")

pienin = None
suurin = None

while True:
    number = float (input ("Syö tä uusi luku: "))
    if number == "":
        break
    if number < pienin:
        pienin = number
    if number > suurin:
        suurin = number

print (str(pienin))
print (str(suurin))

