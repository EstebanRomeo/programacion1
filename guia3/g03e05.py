personas = int(input("Cuantas personas van a ingresar: "))
sumaEdad = 0
promedio = 0
contador = 0

while contador < personas:
    edad = int(input("Ingrese la edad: "))
    sumaEdad = sumaEdad + edad
    promedio = sumaEdad / personas
    contador = contador + 1
print(f"Ingresaste {personas} personas, y el promedio de las edades es: {promedio}")


