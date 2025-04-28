precio = 1
contador = 0

while precio != 0:
    precio = int(input("Ingrese el precio del auto: "))
    if 27460000 < precio < 33850000:
        contador = contador + 1

print(f"Hay {contador} autos que valen entre $27460000 y 33850000")
    
