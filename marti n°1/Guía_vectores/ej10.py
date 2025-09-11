# 10. Función para buscar la primera aparición de un valor:
# Escribir una función que reciba un array de enteros y un número a buscar. La función debe retornar
# la posición de la primera aparición de ese número o -1 si no se encuentra.

def buscar_valor(array_enteros, numero_buscar):
    for i in range(len(array_enteros)):
        if array_enteros[i] == numero_buscar:
            return i
    return -1

array = [10, 5, 1, 3, 40, 80]
numero_buscado = 10

posicion = buscar_valor(array, numero_buscado)

if posicion != -1:
    print(f"El número {numero_buscado} fue encontrado en la posición {posicion}")
else:
    print(f"El número {numero_buscado} no se encontro en el array")