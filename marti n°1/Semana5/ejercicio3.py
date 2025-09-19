#Ejercicio 3: Control de Producción
# Una fábrica produce 3 productos y mide la producción durante 4 días.
# Cargar en una matriz 3x4 las cantidades producidas. Mostrar:
#     La producción total de cada producto.
#     La producción total de cada día.
#     Cuál fue el día con mayor producción total.

produccion = []

for producto in range(3):
    fila = []
    print(f"Producto {producto+1}: ")
    for dia in range(4):
        cant = int(input(f"Ingrese cantidad producida en el día {dia+1}: "))
        fila.append(cant)
    produccion.append(fila)

print("--- Producción total por día ---")
mayor_total = -9999
dia_mayor = -1

for dia in range(4):
    total_dia = 0
    for producto in range(3):
        total_dia += produccion[producto][dia]
    print(f"Día {dia+1}: {total_dia} unidades")
    if total_dia  > mayor_total:
        mayor_total = total_dia
        dia_mayor = dia + 1
    
print("--- Resultado ---")
print(f"El día con mayor producción fue el día {dia_mayor} con {mayor_total} unidades.")