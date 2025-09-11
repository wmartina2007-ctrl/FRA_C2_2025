# 8. Comparar dos arrays:
# Cargar dos arrays de 5 elementos cada uno. Comparar si ambos son iguales elemento a elemento
# y mostrar un mensaje indicando si son o no iguales.

array_1 = []
array_2 = []

print("Cargue el primer array:")
for i in range(5):
    numero = int(input(f"Ingrese el número {i+1}: "))
    array_1.append(numero)

print("\nCargue el segundo array:")
for i in range(5):
    numero = int(input(f"Ingrese el número {i+1}: "))
    array_2.append(numero)

iguales = True
for i in range(5):
    if array_1[i] != array_2[i]:
        iguales = False
        break  

if iguales:
    print("\nLos arrays son iguales.")
else:
    print("\nLos arrays no son iguales.")