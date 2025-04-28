nombres = []

opc = input("Desea ingresar un nombre?: si/no")

while opc == "si":
    nombre = input("Ingrese un nombre: ")
    nombres.append(nombre)
    opc = input("Querés ingresar otro nombre? si/no: ")
    
    
buscar = input("Que nombre desea buscar: ")

if buscar in nombres:
    print(f"{buscar} esta en la posicion {nombres.index(buscar)}")