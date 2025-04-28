lista = ["Marcos", "Aurelio", "Juan", "Zorro"]


print(lista)
eliminar = input("Que desea eliminar?")

if eliminar in lista:
    lista.remove(eliminar)
    print(f"Se elimino {eliminar} de la lista")
    print(lista)
else:
    print(f"No se encontro {eliminar} en la lista")
