# 3. Promedio de valores:
# Declarar un array de 6 números reales (floats). Cargarlo por teclado. Calcular y mostrar el promedio
# de los valores.

numeros_ent = [0.0] * 6
print(numeros_ent)

cantidad_numeros = len(numeros_ent)
print(cantidad_numeros)

# Carga números

for nota in range(len(numeros_ent)):

    numeros_ent[nota] = float(input("Ingresar número: "))

# Mostras números

for nota in range (len(numeros_ent)):
    print(f"Número {nota + 1}: {numeros_ent[nota]}")

#Calculo promedio

suma_numeros = 0

for nota in range(len(numeros_ent)):
    suma_numeros += numeros_ent[nota]

promedio_numero = suma_numeros / len(numeros_ent)

print(f"El promedio de los 6 números es: {promedio_numero}")

