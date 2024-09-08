#Kirjoita ohjelma, joka kysyy suorakulmion kannan ja korkeuden.
#Ohjelma tulostaa suorakulmion piirin ja pinta-alan.
#Suorakulmion piiri tarkoittaa sen neljän sivun yhteispituutta.

# suorakulmio = rectangle
# kanta = base
# korkeus = height
# piiri = perimeter -> formula = 2 x (length + width)
# A = pinta-ala = area -> formula = length x width

print ("Ohjelma laskee suorakulmion piirin ja pinta-alan.")
length = float(input("Suorakulmion kanta:"))
width = float(input("Suorakulmion korkeus: "))
perimeter = 2 * (length +  width)
area = length * width

print ("Suorakulmion piiri: " + str(perimeter))
print ("Suorakulmion pinta-ala: " + str(area))

