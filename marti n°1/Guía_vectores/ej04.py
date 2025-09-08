# 4. Contar mayores a un valor:
# Cargar un array de 8 enteros. Contar cuántos son mayores al valor 100 e informar el resultado.

numeros_ent = [0.0] * 8
print(numeros_ent)

cantidad_numeros = len(numeros_ent)
print(cantidad_numeros)

# Carga números

for nota in range(len(numeros_ent)):

    numeros_ent[nota] = float(input("Ingresar número: "))

# Mostras números

for nota in range (len(numeros_ent)):
    print(f"Número {nota + 1}: {numeros_ent[nota]}")

# Mayores a 100
mayores = []

for nota in range(len(numeros_ent)):
    if numeros_ent[nota] > 100:
        mayores.append(numeros_ent[nota])
print(f"Los números mayores a 100 son: {mayores}")
