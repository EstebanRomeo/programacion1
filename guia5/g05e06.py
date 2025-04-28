texto = "Quiero comer manzanas, solamente manzanas."
grupoTexto = texto.split(" ")
contador = 0
for  i in range(len(grupoTexto)):
    for letra in grupoTexto[i]:
        contador = contador + 1
print(contador)