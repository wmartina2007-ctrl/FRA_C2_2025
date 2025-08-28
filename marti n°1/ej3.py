#3. Definir una función area_triangulo que reciba la base y la altura de un triángulo y
# devuelva su área. Luego, el programa debe pedir los valores y mostrar el resultado.
# Fórmula: area = (b * h) / 2.

base_triangulo = int(input("Ingrese la base del tríangulo: "))
altura_triangulo = int(input("Ingrese la altura del tríangulo: "))

def area(b:int, h:int):
    area_triangulo = (b * h) / 2
    return area_triangulo

area_triangulo = area(base_triangulo, altura_triangulo)
print(f"El área del triángulo es: {area_triangulo}")