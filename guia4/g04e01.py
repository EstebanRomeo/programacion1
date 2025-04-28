numeros = []
mayoresA23 = []
contador = 0

for i in range(10):
    num = int(input("Ingrese un numero: "))
    numeros.append(num)
    if num > 23:
        contador = contador + 1
        mayoresA23.append(num)
print("Tus numeros son: ")
print(numeros)
print(f"Los numeros mayores a 23 son {contador}, y son: ")
print(mayoresA23)

