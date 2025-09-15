titulos = [""] * 20
ejemplares = [0] * 20
cantidad_libros = 0

def cargar_libros():
    global cantidad_libros
    while cantidad_libros < 20:
        titulo = input("Ingrese el tìtulo: ")
        if titulo == "":
            break
        cantidad = int(input("Ingrese ejemplares: "))
        titulos[cantidad_libros] = titulo
        ejemplares[cantidad_libros] = cantidad
        cantidad_libros += 1
    print("Carga lista")

def mostrar_catalogo():
    print("-----Catálogo-----")
    for i in range(cantidad_libros):
        print(f"{titulos[i]} => {ejemplares[i]} copias")
        print()

def disponibilidad():
    titulo = input("Ingrese el título a consultar: ")
    for i in range(cantidad_libros):
        if titulos[i].lower() == titulo.lower():
            print(f"{titulos[i]} tiene {ejemplares[i]} copias.")
            return
        print("No se encontró el libro")

def agotados():
    print("Títulos agotados")
    vacio = True
    for i in range(cantidad_libros):
        if ejemplares[i] == 0:
            print(titulos[i])
            vacio = False
    if vacio:
        print("No hay libros agotados")
    print()

def agregar():
    global cantidad_libros 
    if cantidad_libros < 20:
        titulo = input("Ingrese el nuevo título: ")
        cantidad = int(input("Ingrese la cantidad de ejemplares: "))
        titulos[cantidad_libros] = titulo
        ejemplares[cantidad_libros] = cantidad
        cantidad += 1
        print("Libro añadido")
    else:
        print("No se puede agregar más libros (cantidad máxima 20)")

def actualizar():
    titulo = input("Ingrese el título a actualizar: ")
    for i in range(cantidad_libros):
        if titulos[i].lower() == titulo.lower():
            cambio = int(input("Ingrese cambio"))
            ejemplares[i] += cambio
            if ejemplares[i] < 0:
                ejemplares[i] = 0
            print(f"Nueva cantidad: {ejemplares[i]} copias")
            return
        print("No se encontro el libro")