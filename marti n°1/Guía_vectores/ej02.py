# 2. Sumar todos los elementos:
# Declarar un array de 10 enteros. Cargarlo por teclado. Calcular y mostrar la suma de todos los
# elementos.

numeros_ent = [0.0] * 10
print(numeros_ent)

cantidad_numeros = len(numeros_ent)
print(cantidad_numeros)

# Carga números

for nota in range(len(numeros_ent)):

    numeros_ent[nota] = float(input("Ingresar número: "))

# Mostras números

for nota in range (len(numeros_ent)):
    print(f"Número {nota + 1}: {numeros_ent[nota]}")

#Calculo suma

suma_numeros = 0

for nota in range(len(numeros_ent)):
    suma_numeros += numeros_ent[nota]

print(f"La suma de los 10 números es: {suma_numeros}")