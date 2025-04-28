texto = "Quiero comer manzanas, solamente manzanas."
vocales = ["a","e","i","o","u"]
numVocales = []
a = 0
e = 0
i = 0
o = 0
u = 0

for letra in texto:
    if letra == "a":
        a = a + 1
    elif letra == "e":
        e = e + 1
    elif letra == "i":
        i = i + 1
    elif letra == "o":
        o = o + 1
    elif letra == "u":
        u = u + 1

numVocales.append(a)
numVocales.append(e)
numVocales.append(i)
numVocales.append(o)
numVocales.append(u)

maxVocales = max(numVocales)
indice = numVocales.index(maxVocales)
vocalMasRep = vocales[indice]

print(numVocales)
print(maxVocales)
print(f"La vocal mas repetida es la {vocalMasRep}")