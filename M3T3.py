#Kirjoita ohjelma, joka kysyy käyttäjän biologisen sukupuolen ja hemoglobiiniarvon (g/l).
# Ohjelma ilmoittaa, onko hemoglobiiniarvo alhainen, normaali vai korkea.

#Naisen normaali hemoglobiiniarvo on välillä 117-175 g/l.
#Miehen normaali hemoglobiiniarvo on välillä 134-195 g/l.

print ("Tarkista onko hemoglobiinisi normaali / korkea ->")
genre = input("Syötä sukupuolesi (kirjain) M/N (mies/nainen): ")
hemoglobine = float(input("Syötä hemoglobiiniarvo arvo väliltä -> 117-175(nainen) tai 134-195 (mies): "))

if genre == "M" and hemoglobine > 134 and hemoglobine < 195:
    print ("Normaali hemoglobiiniarvo.")
elif genre == "M" and hemoglobine > 195:
    print("Korkea homeglobiini!")
elif genre == "M" and hemoglobine < 134:
    print("Virhe, tarkista syötetty arvo.")
elif genre == "N" and hemoglobine > 117 and hemoglobine < 175:
    print ("Normaali hemoglobiiniarvo.")
elif genre == "N" and hemoglobine > 175:
    print("Korkea homeglobiini!")
elif genre == "N" and hemoglobine < 117:
    print("Virhe, tarkista syötetty arvo.")