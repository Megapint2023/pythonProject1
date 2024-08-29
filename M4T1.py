# Kirjoita while-toistorakennetta käyttävä ohjelma, joka tulostaa kolmella jaolliset luvut väliltä 1..1000.
# Tässä täytyy käyttää modulus operaattoria.
# Eli number % == 0 (tämä jos toteutuu on se 3:lla jaollinen)


number = 1
while number <= 1000:
   if number % 3 == 0:
       print(number)
   number = number + 1

   # Koodi: Numeron arvo alka 1:stä. "While" toistolause jatkaa, kunnes numeron arvo savuttaa 1000.
   # Lisäksi toistolauseen sisällä erillinen sääntö "jos arvo on 3:lla jaollinen -> printtaa numero.
   # Ketjun lopussa muuttujan arvo nousee aina +1:llä.