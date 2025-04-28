numero = input("Ingrese un número: ")


invertido = numero[::-1]

resultado = ""
contador = 0

for digito in invertido:
    if contador != 0 and contador % 3 == 0:
        resultado += "."
    resultado += digito
    contador += 1

resultadoFinal = resultado[::-1]

print("Numero con puntos:", resultadoFinal)
