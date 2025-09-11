# 6. Mayor y su posición:
# Cargar un array de 7 números enteros. Determinar el valor más alto y en qué posición se
# encuentra.

numeros = []
for i in range(7):
    numero = int(input(f"ingrese el número {i+1} : "))
    numeros.append(numero)

mayor =numeros[0]
for i in range(1, len(numeros)):
    if numeros[i] > mayor:
        mayor = numeros[i]


print("Los números son: " , numeros)
print("El número más grande es: " , mayor)