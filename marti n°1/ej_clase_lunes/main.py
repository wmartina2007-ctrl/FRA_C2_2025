import biblioteca as b 

def menu():
    while True:
        print("---Menú biblioteca---")
        print("1. Cargar tìtulos y ejemplares")
        print("2. Mostrar catálogo")
        print("3. Consultar disponibilidad")
        print("4. Títulos agotados")
        print("5. Agregar nuevo título")
        print("6. Actualizar ejemplares")
        print("7. Salir")

        opcion = input("Elija opción: ")
        if opcion == "1":
            b.cargar_libros()
        elif opcion == "2":
            b.mostrar_catalogo()
        elif opcion == "3":
            b.disponibilidad()
        elif opcion == "4":
            b.agotados()
        elif opcion == "5":
            b.agregar()
        elif opcion == "6":
            b.actualizar()
        elif opcion == "7":
            print("Saliendo.")
            break
        else:
            print("Opción no válida.")

menu()