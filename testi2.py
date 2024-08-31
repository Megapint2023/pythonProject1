# ohjelma kysyy 5 nimeä ja tulostaa ne
# != means "not equal to"


#===========================
# print ("Syötä 5 nimeä")

#nimet = []

#nimi = input("Anna ensimmäinen nimi tai lopeta painamalla Enter: ")
#while nimi!="":
  #  nimet.append(nimi)
 #   nimi = input("Anna seuraava nimi tai lopeta painamalla Enter: ")

#print(nimet)
#===========================

kaverit = []

lkm = int(input("Montako kaveria?"))

for x in range(lkm):
    nimi = input ("Anna nimi:")
    kaverit.append(nimi)

print("Nimilista:")
for kaveri in kaverit:
    print (kaveri)