nombres = ["Mauro", "Joaquin", "Roberto", "Cañuelas", "Pedro", "Sandra", "Jorge", "Mauricio"]
fechaNac = ["12/02/1999", "22/12/1998", "29/09/1990", "01/07/1989", "12/02/2003", "28/12/2002", "03/09/2000", "29/11/2010"]

# Fecha actual fija (podés cambiarla si querés que funcione en otra época)
anioActual = 2025
mesActual = 4
diaActual = 17

print("Mayores de edad:")

for i in range(len(nombres)):
    # Separar día, mes y año de la fecha de nacimiento
    dia, mes, anio = map(int, fechaNac[i].split("/"))

    edad = anioActual - anio

    # Si todavía no cumplió años este año, restamos 1
    if (mesActual, diaActual) < (mes, dia):
        edad -= 1

    if edad >= 18:
        print(f"{nombres[i]} - {edad} años")
