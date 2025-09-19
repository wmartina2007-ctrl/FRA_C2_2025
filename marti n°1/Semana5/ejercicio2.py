#Ejercicio 2: Puntajes de un Torneo
# En un torneo de programación hay 4 equipos que compiten en 5 rondas.
# Cargar en una matriz 4x5 los puntajes obtenidos (enteros). Luego mostrar:
#     El puntaje total de cada equipo.
#     Qué equipo obtuvo el mayor puntaje en total.

puntajes = []

for equipo in range(4):
    fila = []
    print(f"Equipo {equipo+1}: ")
    for ronda in range(5):
        p = int(input(f"Ingrese el puntaje de la ronda {ronda+1}: "))
        fila.append(p)
    puntajes.append(fila)

print("--- Puntaje total de cada equipo ---")

mayor_puntaje = -9999
equipo_ganador = -1

for equipo in range(4):
    total_equipo = 0
    for p in puntajes[equipo]:
        total_equipo += p
    print(f"Equipo {equipo+1}: {total_equipo} puntos")
    if total_equipo  > mayor_puntaje:
        mayor_puntaje = total_equipo
        equipo_ganador = equipo + 1

print("--- Resultado final ---")
print(f"El equipor ganador es el equipo {equipo_ganador} con {mayor_puntaje} puntos.")