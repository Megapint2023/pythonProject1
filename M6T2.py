# Muokkaa edellistä funktiota siten, että funktio saa parametrinaan nopan tahkojen yhteismäärän.
# Muokatun funktion avulla voit heitellä esimerkiksi 21-tahkoista roolipelinoppaa.
# Edellisestä tehtävästä poiketen nopan heittelyä jatketaan pääohjelmassa kunnes saadaan nopan maksimisilmäluku,
# joka kysytään käyttäjältä ohjelman suorituksen alussa.

# TAHKO = nopansivu, esim 6 tahkoinen noppa = 1-6 arvoa sisältävä
#

import random

def parametriton():
 #!!!!! tämä "eka" while loop lisäsin, jotta tahkomäärä on järkevä eli max 100 !!!!
    while True:
        tahkot = input("Syötä kuinka monta tahkoa (eli sivua) nopalla on: ")
        tahkot = int(tahkot)
        if tahkot < 1 or tahkot > 100:
            print ("Älä keuli... Syötä järkevä arvo 1-100 välillä: ")
        else:
            break

    while True:
        nopanheitto = random.randint (1, tahkot )
        if nopanheitto == tahkot:
            print(str(nopanheitto) + " -> Osuit maksimiin!")
            break
        else:
            print ("Heitit: " + str(nopanheitto) + ":n")

parametriton()

