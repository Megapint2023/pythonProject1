#Kirjoita ohjelma, joka kysyy käyttäjältä laivan hyttiluokan (LUX, A, B, C) ja
# tulostaa sen sanallisen kuvauksen alla olevan luettelon mukaisesti.
# Tehtävässä on käytettävä if/elif/else-toistorakennetta.

#LUX on parvekkeellinen hytti yläkannella.
#A on ikkunallinen hytti autokannen yläpuolella.
#B on ikkunaton hytti autokannen yläpuolella.
#C on ikkunaton hytti autokannen alapuolella.
#Jos käyttäjä syöttää kelvottoman hyttiluokan, ohjelma tulostaa Virheellinen hyttiluokka.

print ("Laivan hyttiluokat: (LUX/A/B/C)")
luokka = (input("Tarkista hyttisi sijainti syöttämällä hyttiluokkasi: "))

if luokka == "LUX":
    print ("Parvekkeellinen hytti eläkannella.")

elif luokka == "A":
    print("Ikkunallinen hytti autokannen yläpuolella.")

elif luokka == "B":
    print("Ikkunaton hytti autokannen yläpuolella.")

elif luokka == "C":
    print("Ikkunaton hytti autokannen alapuolella.")

else:
    print("Virheellinen hyttiluokka.")

# HUOM.  ->
    # 1 Pythonissa on käytettävä == merkkejä tarkistaakseen "vastaako arvoa", koska pelkkä = käytetään arvojen laatimiseen.
    # 2 "" on lisättävä Pythonissa, jotta se osaa lukea ne stringeinä.