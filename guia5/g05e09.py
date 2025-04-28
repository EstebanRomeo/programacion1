texto = "Quiero comer manzanas, solamente manzanas."
grupoTexto = texto.split(" ")

for i in range(len(grupoTexto)):
    cant = len(grupoTexto[i].strip(".,"))
    
print(cant)