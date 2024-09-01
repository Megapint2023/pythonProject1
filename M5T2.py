# Kirjoita ohjelma, joka kysyy käyttäjältä lukuja siihen saakka,
# kunnes tämä syöttää tyhjän merkkijonon lopetusmerkiksi.
# Lopuksi ohjelma tulostaa saaduista luvuista viisi suurinta suuruusjärjestyksessä suurimmasta alkaen.
# Vihje: listan alkioiden lajittelujärjestyksen voi kääntää antamalla sort-metodille argumentiksi reverse=True.


numerolista = []

while True:
    numero = input("Syötä uusi numero: ")
    if numero == "":
        break
    else:
        numero = int(numero)
        numerolista.append(numero) # nostaa ja tallentaa numeron numerolistaan

numerolista.sort(reverse=True)

print (numerolista)
print ("Viisi suurinta numeroa olivat: " + str(numerolista[:5]))