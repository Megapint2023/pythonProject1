#Kirjoita ohjelma, joka kysyy kalastajalta kuhan pituuden senttimetreinä.
# Jos kuha on alamittainen, ohjelma käskee laskea kuhan takaisin järveen ilmoittaen samalla käyttäjälle,
# montako senttiä alimmasta sallitusta pyyntimitasta puuttuu. Kuha on alamittainen,
# jos sen pituus on alle 37 cm.


kuhasize = float(input("Syötä kuhan pituus (cm):"))

if kuhasize < 37:
    alipaino = int (37 - kuhasize)
    print ("Alle 37cm pituinen kuha on alamittainen, joten laske se takaisin.")
    print ("Kuhasi on " + str(alipaino) + "cm liian lyhyt")

if kuhasize >= 37:
    print ("Kuhan voi nostaa!")