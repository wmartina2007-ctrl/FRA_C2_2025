#5. Definir una función es_par(numero) que reciba un número y devuelva True si es par y False si
# es impar. Luego, el programa debe pedir un número y mostrar si es par o impar usando la función.

num = int(input("Ingrese un número: "))

def es_par(numero):
    return numero % 2 == 0

if es_par(num):
    print(f"El número {num} es par.")
else:
    print(f"El número {num} es impar.")