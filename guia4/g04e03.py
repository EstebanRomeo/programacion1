nombres = []
sexos = []

sexo = input("Ingrese el sexo(si no desea ingresar mas ingrese *): ")
while sexo == "*":
    if sexo == "mujer":
        nombre = input("Ingrese el nombre de la mujer: ")
        nombres.append(nombre)
        sexos.append("mujer")
    else:
        nombre = input("Ingrese el nombre del hombre: ")
        nombres.append(nombre)
        sexos.append("hombre")
print(nombres)
print(sexo)


