#8. Crear una función llamada calcular_edad(anio_nacimiento) que reciba el año de nacimiento y
# devuelva la edad actual (sin considerar el mes de nacimiento). Luego, el programa debe pedir el
# año de nacimiento del usuario y mostrar la edad calculada.

anio_nacimiento = int(input("Ingrese el año en que usted nació:"))

def calcular_edad(anio_nacimiento):
    return 2025 - anio_nacimiento

print(f"Tienes {calcular_edad(anio_nacimiento)} años" )