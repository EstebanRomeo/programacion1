numeros = []
suma = 0

num1 = int(input("Ingrese primer numero: "))
numeros.append(num1)
num2 = int(input("Ingrese segundo numero: "))
numeros.append(num2)
num3 = int(input("Ingrese tercer numero: "))
numeros.append(num3)
num4 = int(input("Ingrese cuarto numero: "))
numeros.append(num4)
num5 = int(input("Ingrese quinto numero: "))
numeros.append(num5)

print(numeros)

for numero in numeros:
    if numero >= 23:
        suma = suma + numero
        print(f"La suma de los numeros mayores a 23 es: {suma}")
    else:
        print("Error")
