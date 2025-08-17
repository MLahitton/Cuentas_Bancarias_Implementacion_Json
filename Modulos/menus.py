from Modulos import creacion_Clientes as creacion 
from Modulos import creacion_Cuentas as cuentas


print("Bienvenido al sistema de gestión de clientes del banco.")

#Funcion para mostrar el menú principal
def menu_principal():
    
    while True:
        print("\nMenú de opciones:")
        print("1. Crear cliente")
        print("2. Consultar cliente")
        print("3. Crear cuenta")
        print("4. Depositar dinero")
        print("5. Retirar dinero")
        print("6. Creacion CDT")
        print(". Salir")

        accion = input("Seleccione una opción: ")

        match accion:
            case "1":
                creacion.crear_clientes()
            case "2":  
                creacion.consultar_clientes()
            case "3":
                cuentas.crear_cuentas()
            case "4":
                cuentas.deporsitar_dinero()
            case "5":
                cuentas.retirar_Dinero()
            case "6":
                cuentas.creacion_cdt()
            case "11":
                print("Saliendo del sistema. ¡Hasta luego!")
                break
            case _:
                print("Opción no válida. Por favor, intente de nuevo.")