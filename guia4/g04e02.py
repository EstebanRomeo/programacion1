vocales = ["a","e","i","o","u"]
grupoVocales = []
contador = 0
letras = []

letra = input("Ingrese  una letra: ")
while letra != "*" :
    letra = input("Ingrese  una letra: ")
    letras.append(letra)
    for vocal in vocales:
        if letra == vocal:
            contador = contador + 1
            grupoVocales.append(letra)
print(f"Tu lista de letras es:" )
print(letras)
print(f"Tu vocales son {contador}, y son estas: ")
print(grupoVocales)
