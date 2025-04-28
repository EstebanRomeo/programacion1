resp = "si"
sumaSueldos = 0

while resp == "si":
    sueldo = int(input("Ingrese sueldo: "))
    print(sueldo)
    sumaSueldos = sumaSueldos + sueldo
    resp = input("Queres seguir ingresando sueldos? si/no")
print(f"La suma de todos los sueldos es: {sumaSueldos}")
