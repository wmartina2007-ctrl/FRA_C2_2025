#Ejercicio 1: Registro de Temperaturas
# Una estación meteorológica registra las temperaturas diarias de una semana (7 días) en 3 horarios (mañana, tarde y noche).
# Cargar en una matriz 7x3 las temperaturas (números enteros) y mostrar:
#     El promedio de temperatura de cada día.
#     El promedio general de toda la semana.

temperaturas = []

for dia in range(7):
    fila = []
    print(f"Dìa {dia+1}: ")
    for turno in ["Mañana", "Tarde", "Noche"]:
        temp= int(input(f"Ingrese temperatura del turno {turno}: "))
        fila.append(temp)
    temperaturas.append(fila)

print("--- Promedio de cada dìa ---")
suma_general = 0
cant_datos = 0

for dia in range(7):
    total_dia = 0
    for t in temperaturas[dia]:
        total_dia += t
    promedio_dia = total_dia / 3
    print(f"Dìa {dia+1}: {promedio_dia: .2f} °C")

suma_general += total_dia
cant_datos += 3

promedio_general = suma_general / cant_datos
print("--- Promedio general de la semaana ---")
print(f"{promedio_general: .2f} °C")

