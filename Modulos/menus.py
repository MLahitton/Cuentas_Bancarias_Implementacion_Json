from Modulos import creacion_Clientes as creacion 


print("Bienvenido al sistema de gestión de clientes del banco.")

#Funcion para mostrar el menú principal
def menu_principal():
    
    while True:
        print("\nMenú de opciones:")
        print("1. Crear cliente")
        print("2. Consultar cliente")
        print("3. Salir")

        accion = input("Seleccione una opción: ")

        match accion:
            case "1":
                creacion.crear_clientes()
            case "2":
                
                creacion.consultar_clientes()
            case "3":
                print("Saliendo del sistema. ¡Hasta luego!")
                break
            case _:
                print("Opción no válida. Por favor, intente de nuevo.")