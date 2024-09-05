# Kirjoita funktio, joka saa parametrinaan bensiinin määrän Yhdysvaltain nestegallonoina
# ja palauttaa paluuarvonaan vastaavan litramäärän.
# Kirjoita pääohjelma, joka kysyy gallonamäärän käyttäjältä ja muuntaa sen litroiksi.
# Muunnos on tehtävä aliohjelmaa hyödyntäen. Muuntamista jatketaan siihen saakka,
# kunnes käyttäjä syöttää negatiivisen gallonamäärän.
# Yksi gallona on 3,785 litraa.

print ("Ohjelma muuttaa gallonit litroiksi.")
print ("Saat lopetettua ohjelman antamalla negatiivisen arvon.")

def galloneistlitroiks(gallons):
    return gallons * 3.785

def (paaohjelma):
    while True:
       gallons = float(input("Nontako gallonia muutetaan litroiksi"))
       if gallons < 0:
           print ("Syötit negatiivisen arvon -> ohjelma loppu.")
           break
       else:
           litra = galloneistlitroiks(gallons)
           print (str(gallons) + " gallonia on = " + str(litra) + " litraa."))


paaohjelma()