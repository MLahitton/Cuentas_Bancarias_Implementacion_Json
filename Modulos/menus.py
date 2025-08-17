from Modulos import creacion_Clientes as creacion 
from Modulos import creacion_Cuentas as cuentas
from Modulos import creditos as creditos
from Modulos.creacion_Clientes import historial



def mostrar_bienvenida():
    mensaje = "BIENVENIDO AL SISTEMA DE GESTIÓN DE CLIENTES DEL BANCO"
    ancho = len(mensaje) + 4  # Espacio para bordes y padding

    print("\n" + "+" + "-" * ancho + "+")
    print("|" + " " * ancho + "|")
    print(f"|  {mensaje}  |")
    print("|" + " " * ancho + "|")
    print("+" + "-" * ancho + "+\n")

mostrar_bienvenida()


#Funcion de menu de tipos de creditos
def menu_tipos_creditos():
    while True:
        accion = input("Seleccione el tipo de crédito:\n1. Crédito de Vivienda\n2. Crédito de Auto\n3. Credito libre inversion\n4. Salir\n")
        match accion:
            case "1":
                creditos.credito_vivienda()
            case "2":
                creditos.credito_auto()
            case "3":
                creditos.credito_libre()
            case "4":
                print("Saliendo del menú de tipos de créditos.")
                menu_creditos()
            case _:
                print("Opción no válida. Por favor, intente de nuevo.")

#Funcion menu de creditos
def menu_creditos():
    accion = input("Seleccione una opción:\n1. Crear crédito\n2. Consultar crédito\n3. Pagar crédito\n4. Salir\n")
    match accion:
        case "1":
            menu_tipos_creditos()
        case "2":
            creditos.mostrar_creditos()
        case "3":
            creditos.pagar_credito()
        case "4":
            print("Saliendo del menú de créditos.")
            menu_principal()
        case _:
            print("Opción no válida. Por favor, intente de nuevo.")

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
        print("7. Créditos")
        print("8. Historial de movimientos")
        print("11. Salir")

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
            case "7":
                menu_creditos()
            case "8":
               historial()
                
            case "11":
                print("Saliendo del sistema. ¡Hasta luego!")
                break
            case _:
                print("Opción no válida. Por favor, intente de nuevo.")


menu_principal()