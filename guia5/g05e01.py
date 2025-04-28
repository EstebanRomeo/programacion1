cadena = "Curso de Python"
agregado = "Programación en"

# Cortar la cadena original en partes
lista = cadena.split(" ")  # ["Curso", "de", "Python"]

# Insertar "Programación en" antes de "Python"
lista.insert(2, agregado)

# Unir todo nuevamente en una sola cadena
nueva_cadena = " ".join(lista)

print(nueva_cadena)
