cadena = "Curso de Programacion en Python "

contador = 0

for letra in cadena:
    if letra == "o":
        contador = contador + 1
print(f"La letra o aparece {contador} veces")