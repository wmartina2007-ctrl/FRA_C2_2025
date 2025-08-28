#6. Crear una función convertir_minutos(minutos) que reciba una cantidad de minutos y devuelva
# cuántas horas y minutos sobran.

minutos = int(input("Ingrese la cantidad de minutos: "))

def convertir_minutos(minutos):
    horas = minutos // 60
    minutos_sobran = minutos % 60
    return horas, minutos_sobran

horas, minutos_sobran = convertir_minutos(minutos)
print(f"{minutos} minutos son {horas} horas y {minutos_sobran} minutos.")