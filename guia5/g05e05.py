texto = "Quiero comer manzanas, solamente manzanas."
grupoTexto = texto.split(" ")

for i in range(len(grupoTexto)):
    if grupoTexto[i].strip(".,") == "manzanas":
        grupoTexto[i] = "peras"
print(grupoTexto)