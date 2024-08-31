# Kirjoita ohjelma, joka kysyy käyttäjältä lukuja siihen saakka, kunnes tämä syöttää tyhjän merkkijonon lopetusmerkiksi.
# Lopuksi ohjelma tulostaa saaduista luvuista pienimmän ja suurimman.

# Eli käytännössä ohjelma jatkuvasti pyytää lukuarvoja, kunnes käyttäjä painaa enter.

print ("Ohjelma valitsee syötetyistä arvoista pienimmän ja suurimman.")
print ("Lopeta ohjelma painamalla enter.")

pienin_numero = None
suurin_numero = None

while True:
    new_number = input ("Syötä uusi numero: ")
    if new_number == "":
        break

    new_number = float(new_number)

    if pienin_numero is None or new_number < pienin_numero:
        pienin_numero = new_number
    if suurin_numero is None or new_number > suurin_numero:
        suurin_numero = new_number

pienin_numero = int(pienin_numero)
suurin_numero = int(suurin_numero)

print ("Numero " + str(pienin_numero) + " oli pienin syöttämäsi numero.")
print ("Numero " + str(suurin_numero) + " oli suurin syöttämäsi numero.")

