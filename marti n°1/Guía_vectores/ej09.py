# 9. Intercambiar elementos pares por ceros:
# Cargar un array de 10 enteros. Reemplazar todos los elementos pares por cero y mostrar el array
# resultante.

numeros = []

print("Ingrese 10 números enteros: ")
for i in range(10):
    numero = int(input(f"Ingrese el número {i+1}: "))
    numeros.append(numero)

for i in range(len(numeros)):
    if numeros[i] % 2 == 0:
        numeros[i] = 0

print("La lista de números reemplazados por 0 es", numeros)