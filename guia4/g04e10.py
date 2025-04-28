dias = ["Lunes", "Martes", "Miercoles", "Jueves", "Viernes", "Sábado", "Domingo"]
milimetros = []
total = 0


for i in range(7):
    cantidad = int(input(f"Ingrese la cantidad que llovió el día {dias[i]}: "))
    milimetros.append(cantidad)
    total += cantidad


mayorLluvia = max(milimetros) #Dia que mas llovio
indiceMayor = milimetros.index(mayorLluvia) #Indice del dia que mas llovio
diaMayorLluvia = dias[indiceMayor] #En base al indice, busca el indice de la lista correspondiente a los dias de la semana

# Mostrar resultados
print(f"Llovió en total {total} milímetros.")
print(f"El día que más llovió fue {diaMayorLluvia}, con {mayorLluvia} milímetros.")


"""
for i in range(len(dias)):
    print(f"El {dias[i]} llovio: {milimetros[i]}")
print(f"Llovio en total {total} milimetros")
"""
