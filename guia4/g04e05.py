numeros = []
paresMayoresYMenores = []

opc = input("¿Querés ingresar un número? si/no: ")

while opc == "si":
    numero = int(input("Ingrese un número: "))
    numeros.append(numero)
    opc = input("¿Querés ingresar otro número? si/no: ")

for numero in numeros:
    if numero % 2 == 0 and 0 < numero < 31:
        paresMayoresYMenores.append(numero)

print("Numeros ingresados:", numeros)
print("Pares mayores que 0 y menores que 31:", paresMayoresYMenores)
