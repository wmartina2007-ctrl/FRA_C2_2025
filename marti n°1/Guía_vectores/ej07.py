# 7. Invertir orden:
# Cargar un array de 6 enteros y mostrarlo invertido, es decir, desde el último al primero.

numeros = []
for i in range(6):
    numero = int(input(f"ingrese el número {i+1} : "))
    numeros.append(numero)

menor = numeros[0]
for i in range(1, len(numeros)):
    if numeros[i] < menor:
        menor = numeros[i]


print("Los números son: " , numeros)
print("El número más chico es: " , menor)