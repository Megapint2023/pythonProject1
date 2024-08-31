# Kirjoita ohjelma, joka kysyy käyttäjältä käyttäjätunnuksen ja salasanan.
# Jos jompikumpi tai molemmat ovat väärin, tunnus ja salasana kysytään uudelleen.
# Tätä jatketaan kunnes kirjautumistiedot ovat oikein tai väärät tiedot on syötetty viisi kertaa.
# Edellisessä tapauksessa tulostetaan Tervetuloa ja jälkimmäisessä Pääsy evätty.
# (Oikea käyttäjätunnus on python ja salasana rules).
from ctypes import pythonapi

#Tee while silmukka joka tekee 5 kierrosta tai break mikäli tiedot matchää
#Tunnus ja salasana on määritetty valmiiksi.

print ("Kirjaudu oikeilla tiedoilla.")

u_name = "python"
u_pass = "rules"