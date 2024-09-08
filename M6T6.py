# Kirjoita funktio, joka saa parametrinä:
# 1. pizzan halkaisijan senttimetreinä
# 2. Sen hinnan euroina.
# 3. palauttaa pizzan yksikköhinnan euroina per neliömetri.

# Pääohjelma kysyy käyttäjältä: kahden pizzan halkaisijat ja hinnat
# Lopuksi ilmoittaa kummasta saa enemmän vastinetta rahalle.
# Yksikköhintojen laskennassa on hyödynnettävä kirjoitettua funktiota.
# (Ykköshinta = lopullinen hinta)


#ympyrän pinta-ala A = 𝜋 * r²
# d = r + r
# A(pintaala) -< KAAVA: pii (d/2)²
# Laske -> euro per neliömetri pizzaa
# value = A / hinta


import math

def pizza1(d1):
    r1 = d1 / 2# laskee säteen
    A1 = math.pi * r1**2 #ympyrän pinta-ala A = 𝜋 * r²
    value1 = hinta1 / A1 #tällä hetkellä A1 arvo on edelleen centteinä
    # €/cm² -> €/m². cm -> dm -> m eli 2xnollaa per porras. Täytyy kertoa 10000
    value1 = value1 * 10000# €/m²
    print(f"Ensimmäisen pizzan neliömetrihinta on noin: {value1:10.1f}€/m².")
    return value1

def pizza2(d2):
    r2 = d2 / 2
    A2 = math.pi * r2**2
    value2 = hinta2 / A2
    value2 = value2 * 10000
    print(f"Toisen pizzan neliömetrihinta on noin: {value2:10.1f}€/m².")
    return value2

print ("Ohjelma vertaa kummasta pizzasta sait enemmän vastinetta rahoillesi.")

d1 = input("Syötä ensimmäisen pizzan halkaisija senttimetreinä: ")
d1 = float(d1)
hinta1 = input("Syötä ensimmäisen pizzan hinta: ")
hinta1 = float(hinta1)
d2 = input("Syötä toisen pizzan halkaisija senttimetreinä: ")
d2 = float(d2)
hinta2 = input("Syötä toisen pizzan hinta: ")
hinta2 = float(hinta2)

pizza1(d1)
pizza2(d2)