#7. Escribir una función verificar_acceso(edad) que reciba la edad de una persona y determine si
# es mayor de edad (18 años o más) devolviendo un booleano. Luego, el programa debe pedir la
# edad al usuario y mostrar un mensaje apropiado.

edad_persona = int(input("Ingrese su edad: "))

def verificar_acceso (edad_persona):
    return edad_persona >= 18

if verificar_acceso (edad_persona):
    print("Eres mayor de edad, puedes ingresar.")
else:
    print("Eres menor de edad, no puedes ingresar.")