#1
#num = int(input("Ingrese un numero real"))
#if num >= 0:
#    print(f"El numero real {num} es mayor que cero, y es positivo")
#else:
#    print(f"El numero real {num} es menor que cero, y es negativo")
    
#2
#num1 = int(input("Ingrese el primer número: "))
#num2 = int(input("Ingrese el segundo número: "))

#if num1 < num2:
#    print(f"El número {num1} es menor que {num2}")
#elif num1 == num2:
#    print("Ingresaste el mismo número")
#else:
#    print(f"El número {num1} es mayor que {num2}")

#3
#num1 = int(input("Ingrese el primer número: "))
#num2 = int(input("Ingrese el segundo número: "))
#op = input("¿Que operacion desea hacer? + o -: ")

#if op == "+":
#    suma = num1 + num2
#    print(f"La suma es de {num1} con {num2} es de {suma}")
#else:
#    resta = num1 - num2
#    print(f"La resta entre {num1} y {num2} es de {resta}")

#4
#nombre = input("Ingresa un nombre: ")
#opc = input("Ingrese > si es mayor, o < si es menor: ")

#if opc == ">":
#    print(f"{nombre} es mayor de edad")
#else:
#    print(f"{nombre} es menor de edad")


#5
#num = int(input("Ingresa un numero"))

#if num <= 99 and num >= 0:
#        print(f"El numero {num} es un positivo de dos digitos")
#else:
#        print(f"El numero {num} no es un positivo de dos digitos")




#6
#nombre = input("¿Cual es tu nombre?")
#carrera = input("¿Carrera a inscribirse?")
#localidad = input("¿Localidad donde reside?")

#if localidad == "rio cuarto":
#    print(f"Buenos Dias {nombre}, estudiante de {carrera} de la localidad de {localidad}, la cuota mensual quedaria en $100000")
#else:
#    if carrera == "mecatronica" and carrera != "desarrollo":
#            descuento = 100000 * (15 / 100)
#            cuota = 100000 - descuento
#            print(f"Buenos Dias {nombre}, estudiante de {carrera} de la localidad de {localidad}, la cuota mensuak quedaria en {cuota}")
#    elif carrera == "turismo":
#            descuento = 100000 * (5 / 100)
#            cuota = 100000 - descuento
#            print(f"Buenos Dias {nombre}, estudiante de {carrera} de la localidad de {localidad}, la cuota mensual quedaria en {cuota}")
#    else:
#            print(f"Buenos Dias {nombre}, estudiante de {carrera} de la localidad de {localidad}, la cuota mensual quedaria en $100000")


#7

#boleto = 20000
#descuento = boleto * (40/100)

#nombre = input("Ingresa tu nombre")
#edad = int(input("Ingresa tu edad"))

#if edad <= 10 and edad >= 5:
#        boleto = boleto - descuento
#        print(f"{nombre} de {edad} años tenes decuentoi de 40%, el costo del pasaje quedaria en {boleto}")
#elif edad >= 65:
#        boleto = boleto - descuento
#        print(f"{nombre} de {edad} años tenes decuento de 40%, el costo del pasaje quedaria en {boleto}")
#else:
#        print(f"{nombre} de {edad} años no tenes decuento, el costo del pasaje quedaria en {boleto}")

#8
#nombre = input("Ingresa tu nombre: ")
#aus = int(input("Ingrese cant. de dias faltados: "))
#ingreso = int(input("Ingrese año de ingreso: "))
#adicional = 1000000 * (30/100)
#año = 2025

#if aus == 0 and ingreso <= 2020:
#        sueldo = 1000000 + adicional
#        print(f"{nombre}: Ausentismo: {aus} Año de ingreso: {ingreso} Sueldo: {sueldo}")
#else:
#        print(f"{nombre}: Ausentismo: {aus} Año de ingreso: {ingreso} Sueldo: 1000000")


#9

#peso = int(input("Ingresa tu peso: "))
#altura = float(input("Ingresa tu altura: "))

#imc = peso / altura**2

#if imc < 18.5:
#    print("Para tu peso de {peso} y tu altura de {altura} metros tu Índice de Masa Corporal (IMC) es 31.07 que #está en la categoría Peso Bajo")
#elif 18.5 <= imc <= 24.9:
#    print("Para tu peso de {peso} y tu altura de {altura} metros tu Índice de Masa Corporal (IMC) es 31.07 que #está en la categoría Normal")
#elif 25 <= imc <= 29.9:
#    print("Para tu peso de {peso} y tu altura de {altura} metros tu Índice de Masa Corporal (IMC) es 31.07 que #está en la categoría Sobrepeso")
#else:
#    print("Para tu peso de {peso} y tu altura de {altura} metros tu Índice de Masa Corporal (IMC) es 31.07 que #está en la categoría Obesidad")

peso = int(input("Ingrese el peso del paquete en Kg: "))
distancia = int(input("Ingrese la distancia en Km: "))

if 0 <= peso <= 1:
        costo = 150 + (distancia * 10)
        print(f"El costo total de envío de tu paquete de {peso} kg a una distancia de {distancia} km es de ${costo}")
elif 1 < peso <= 5:
        costo = 300 + (distancia * 20)
        print(f"El costo total de envío de tu paquete de {peso} kg a una distancia de {distancia} km es de ${costo}")
elif 5 < peso <= 10:
        costo = 450 + (distancia * 30)
        print(f"El costo total de envío de tu paquete de {peso} kg a una distancia de {distancia} km es de ${costo}")
else:
        print("No enviamos paquetes de 10kg o más")