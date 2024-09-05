# Kirjoita funktio, joka saa parametrinaan listan kokonaislukuja.
# Ohjelma palauttaa listassa olevien lukujen summan.
# Kirjoita testausta varten pääohjelma, jossa luot listan, kutsut funktiota ja tulostat sen palauttaman summan.


print("Ohjelma palauttaa listassa olevien numeroiden summan.")

numerolista = [5, 11, 2, 18, 24, 19]

def laskekaikki(numerolista):
    summa = 0
    for numero in numerolista:
        summa = summa + numero:
        print("- " + str(numero))
    return summa


laskekaikki()


#
#        numerolista = numerolista +1
#
#    return (numerolista total)
#numerot = int(numerot)
#numerolista.append(numerolista)
#
#numeroidensumma = numerolista
#
#print(numerot)

# täytyy tehdä lista ja kirjoittaa sinne valmiiksi arvoja
# Sitten luoda looppi joka menee listan läpi ja poimii sen arvot  ja laskee summan niille eri
# sitten laskee arvojen summan yhteen ja printtaa sen.
# lisäksi voisin vielä printata näkyviin arvot joiden summan ohejlma on laskenut
# Fun