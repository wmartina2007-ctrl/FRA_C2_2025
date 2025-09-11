# 5. Buscar un valor:
# Cargar un array de 10 enteros. Solicitar al usuario un número y verificar si se encuentra en el array.
# Informar la posición en caso afirmativo, o indicar que no se encuentra.



# Cargar un array de números (lo hacemos fijo para simplificar)
numeros = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
print("El array de números es:", numeros)

# Pedir un número al usuario
numero_buscar = int(input("Ingresa un número para buscar en el array: "))

# Variable para saber si encontramos el número
encontrado = False
posicion = 0

# Buscar el número en el array
for i in range(len(numeros)):
    if numeros[i] == numero_buscar:
        encontrado = True
        posicion = i
        break

# Mostrar el resultado
if encontrado == True:
    print(f"El número {numero_buscar} se encuentra en la posición {posicion} del array.")
else:
    print(f"El número {numero_buscar} no se encuentra en el array.")