# Kirjoita ohjelma, joka kysyy käyttäjältä käyttäjätunnuksen ja salasanan.
# Jos jompikumpi tai molemmat ovat väärin, tunnus ja salasana kysytään uudelleen.
# Tätä jatketaan kunnes kirjautumistiedot ovat oikein tai väärät tiedot on syötetty viisi kertaa.
# Edellisessä tapauksessa tulostetaan Tervetuloa ja jälkimmäisessä Pääsy evätty.
# (Oikea käyttäjätunnus on python ja salasana rules).

#Tee while silmukka joka tekee 5 kierrosta tai break mikäli tiedot matchää
#Tunnus ja salasana on määritetty valmiiksi.


print ("Kirjaudu sisään tunnuksella ja salasanalla.")

username = "python"
password = "rules"

kirjautumisyritys = 0
while kirjautumisyritys <= 5:
    username_input = input("Syötä käyttäjätunnus:")
    password_input = input("Syötä salasana:")

    if username_input == username and password_input == password:
        print("Great success... commander.")
        break
    else:
        kirjautumisyritys = kirjautumisyritys + 1
        if kirjautumisyritys < 5:
            print("Väärä tunnus tai salasana, yritä uudelleen.")
        else:
            print("Liian monta yritystä.")
