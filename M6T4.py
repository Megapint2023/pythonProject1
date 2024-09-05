# Kirjoita funktio, joka saa parametrinaan listan kokonaislukuja.
# Ohjelma palauttaa listassa olevien lukujen summan.
# Kirjoita testausta varten pääohjelma, jossa luot listan, kutsut funktiota ja tulostat sen palauttaman summan.


print("Ohjelma listan numerot yhteen.")

numerolista = [5, 11, 2, 18, 24, 19]

def laskekaikki(numerolista): # funktio näkee koko listan ja kiakki sen arvot
    summa = 0
    for i in numerolista: # python automaattisesti menee numerolistan läpi
        summa = summa + i
        print("- " + str(i))
    return summa

yht = laskekaikki(numerolista)
print("Listassa olevien numeroiden summa on: ", yht)


# täytyy tehdä lista ja kirjoittaa sinne valmiiksi arvoja
# Sitten luoda looppi joka menee listan läpi ja poimii sen arvot  ja laskee summan niille eri
# sitten laskee arvojen summan yhteen ja printtaa sen.
# lisäksi voisin vielä printata näkyviin arvot joiden summan ohejlma on laskenut
# Fun