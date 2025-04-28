texto = "Quiero comer manzanas, solamente manzanas."
grupoTexto = texto.split(" ")
contador = 0

palabra = "manzanas"
posicion = texto.find(palabra)
lon = len(palabra)
man = texto[posicion:posicion+lon]


for palabra in grupoTexto:
    if palabra.strip(".,") == "manzanas":
        contador = contador + 1
print(f"La palabra MANZANA aparece {contador} veces")

"""
palabra.strip elimina caracteres al inicio y al final de una cadena
"""

print(grupoTexto)
print(posicion)
print(texto[posicion:posicion+lon])
print(man)


