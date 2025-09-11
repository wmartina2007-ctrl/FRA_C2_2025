def buscar_valor(array_enteros, numero_a_buscar):
  for i in range(len(array_enteros)):
    if array_enteros[i] == numero_a_buscar:
      return i
  return -1

# --- Ejemplo de uso ---

mi_array = [10, 25, 5, 40, 5, 80]
numero_buscado = 5

posicion = buscar_valor(mi_array, numero_buscado)

if posicion != -1:
  print(f"El número {numero_buscado} fue encontrado en la posición: {posicion}")
else:
  print(f"El número {numero_buscado} no se encontró en el array.")