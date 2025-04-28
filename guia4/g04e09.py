nombres = ["Marcos", "Juan", "Aurelio", "Locomotora", "Pablo", "Sebastian", "Mauricio"]
sueldos = [2500000, 2890000, 1500000, 2000000, 1700000, 3150000, 2851000]


print("Personas que ganan mas de $2850000:")
for i in range(len(nombres)):
    if sueldos[i] > 2850000:
        print(f"{nombres[i]} - ${sueldos[i]:,}")
