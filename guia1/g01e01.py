print("Hola Pablo ¿Como estas?")
print("--------------------------------------------"
"Comenzando a aprender a programar en Python!"
"--------------------------------------------")

nombre = input("¿Como te llamas?")
print(f"Hola {nombre}, ¿Como te va?")

nombre = input("Ingresa tu nombre: ")
edad = input("Ingresa tu edad: ")
altura = input("Ingresa tu altura: ")

print(f"Hola {nombre}, tenes {edad} años y medis {altura}")

num1 = int(input("Ingresa primer numero: "))
num2 = int(input("Ingresa segundo numero: "))
suma = num1 + num2
print(f"El resultado de tu suma es: {suma}")


nota1 = int(input("Ingresa primer nota: "))
nota2 = int(input("Ingresa segunda nota: "))
nota3 = int(input("Ingresa tercera nota: "))
nota4 = int(input("Ingresa cuarta nota: "))

suma = nota1 + nota2 + nota3 + nota4
promedio = suma / 4
print(f"Tu promedio es: {promedio}")


peso = int(input("Ingresa tu peso: "))
altura = float(input("Ingresa tu altura: "))

imc = peso / altura**2
print(f"Para tu peso de {peso}kg y tu altura de {altura} metros, tu indice de Masa Corporal (IMC) es de {imc}")

celsius = int(input("Ingresa los grados celsius"))
fahrenheit = (celsius * 1.8) + 32

print(f"Para {celsius}C equivalen {fahrenheit}F")



producto = input("Ingresa tu producto: ")
precio = int(input("Ingresa el precio original: "))
descuento = int(input("ingresa el porcentaje de descuento: "))

descuento2 = precio * (descuento/100)
precioDescuento = precio - descuento2

print(f"Hola! Tu producto {producto} de ${precio} te queda en ${precioDescuento} con el {descuento}% de descuento")

consumoDia = 2.5
precioInfinia = 1459
precioSuper = 1216

diaInfinia = 2.5 * 1459
diaSuper = 2.5 * 1216
añoInfinia = diaInfinia * 365
añoSuper = diaSuper * 365

ahorro = añoInfinia - añoSuper

print(f"Para los datos referidos de consumo (2.5 litros de nafta por dia) y los precios de los tipos de nafta, tu ahorro anual, suponiendo precios estables, sera de ${ahorro}")
