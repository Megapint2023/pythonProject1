# 1.
# Toteutetaan algoritmi piin (π) likiarvon laskemiseksi.
# Oletetaan, että A on yksikköympyrä eli ympyrä, jonka keskipiste on origossa ja jonka säde on yksi.
# Sen ympärille piirretään pienin mahdollinen neliö B siten, että ympyrä A jää kokonaan neliön sisäpuolelle.
# Neliön nurkkapisteet ovat tällöin (-1,-1), (1,-1), (1,1) ja (-1,1).

# 2.
# Jos neliön sisälle arvotaan satunnaisesti suuri määrä pisteitä,
# osuu niistä myös ympyrän sisälle.
# Likimain osuus ympyrän pinta-ala:sta verrattuna neliön pinta-alaan on πr^2/4,
# Kaava sievenee muotoon ->  π/4.

#3.
# Tästä saadaan yksinkertainen menetelmä piin likiarvon laskemiseksi:
# Arvotaan neliön B sisälle suuri määrä satunnaisissa kohdissa olevia pisteitä, esimerkiksi miljoona.
# Olkoon N tämä pisteiden kokonaismäärä. Jokaisesta neliön sisään arvotusta pisteestä testataan vuorollaan,
# jääkö se myös yksikköympyrän sisälle.
# Olkoon osuma =  n (ympyrän sisälle jäävien pisteiden kokonaismäärä).
# Nyt pätee n/N≈π/4, josta saadaan π≈4n/N.
# KAAVA = π≈4n/N

#4.
# Kirjoita ohjelma, joka kysyy arvottavien pisteiden määrän käyttäjältä
# ja toteuttaa PII:n likiarvon laskennan edellä kuvatulla menetelmällä.
# Lopuksi ohjelma tulostaa PII:n likiarvon käyttäjälle.
# (Huomaa, että jokaisesta arvotusta pisteestä (x,y) on helppoa testata onko se yksikköympyrän sisällä:
# epäyhtälön avulla. Testaus epäyhtälöllä: x^2+y^2<1

# -> Eli kirjoita ohjelma joka kysyy (eli montako pistettä arvotaan)
# ja laskee annetun kaavan avalla osumat, jonka jälkeen printtaa PII:n likiarvon.
# ========================================
# N = input
# n = osuma
# pisteet (-1,-1), (1,-1), (1,1) ja (-1,1)
# nelio_A = 2 * 2
# mpyra_A = πr ^ 2
# n = x^2+y^2<1
# ========================================


print ("Ohjelma laskee π:n likiarvon generoimien satunnaispisteiden avulla.")
while True:
    shots = input("Syötä pisteiden määrä: ")
    N = int(shots)  # pisteet
    if N < 1 or N > 10000000:
        print("Virheellinen luku, syötä arvo 1 ja 10 milj. välillä.")
    else:
        break
# While True loop: pitää huolen että numero on 1-10milj välillä toimivuuden takaamiseksi.
# N = int(shots) muuttaa syötetyn arvon pythonille ymmerrättäväksi kokonaisluvuksi

n = 0 # osumat
import random
for pisteet in range(N): # range funtio eli listan läpikäynti
    x = random.uniform(-1, 1) #sattumanvarainen murtoluku -1  ja 1 väliltä
    y = random.uniform(-1, 1) #sattumanvarainen murtoluku -1  ja 1 väliltä

    if x**2 + y**2 < 1: # TESTIKAAVA: Jos toteutuu ypäyhtälö x^2+y^2<1 = kyseessä on osuma
        n = n + 1 # Mikäli osuma -> muuttuja "n" arvoa nostetaan +1:llä

likiarvo = 4 * n / N # Kaava likiarvon laskemiseen = π≈4n/N
likiarvo = float(likiarvo)
print ("Pii:n likiarvo: " + str(likiarvo))
