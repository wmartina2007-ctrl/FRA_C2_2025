#2. Escribir una función operaciones(num1, num2) que reciba dos números y muestre su suma,
# resta y multiplicación. Luego, el programa debe pedir dos números al usuario y llamar a la
# función.

numero_1 = int(input("Número 1: "))
numero_2 = int(input("Número 2: "))

def suma(a:int, b:int):
    resultado_Suma = (a + b)
    return resultado_Suma

def resta(a:int, b:int):
    resultado_resta = (a - b)
    return resultado_resta

def division(a:int, b:int):
    resultado_division = (a / b)
    return resultado_division



resultado_Suma = suma(numero_1, numero_2)
print(f"La suma de ambos números es: {resultado_Suma}")

resultado_resta = resta(numero_1, numero_2)
print(f"La resta entre ambos números es: {resultado_resta}")

resultado_division = division(numero_1, numero_2)
print(f"La divisíon entre ambos números es: {resultado_division} ")