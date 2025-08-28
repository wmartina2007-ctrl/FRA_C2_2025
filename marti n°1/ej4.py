#4. Crear una función buscar_mayor que reciba tres números y devuelva los tres números
# ordenados de mayor a menor. Luego, el programa debe pedir los números y mostrar los números
# ordenados.

num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))
num3 = float(input("Ingrese el tercer número: "))

def buscar_mayor (num1, num2, num3):
    numeros = [num1, num2, num3]
    numeros.sort(reverse=True)
    return numeros

numeros_ordenados = buscar_mayor(num1, num2, num3)

print(f"Los npumeros ordenados de mayor a menor es: {numeros_ordenados}")