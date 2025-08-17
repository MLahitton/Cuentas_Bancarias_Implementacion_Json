### Aunque esta linea se llama creacion_Cuentas, esta inlcuido en este la parte de movimientos en cuentas
import json
import os
import Modulos.persistencia as persistencia
from Modulos.persistencia import guardar_cliente, consultar_cliente
from Modulos.persistencia import cargar_db, guardar_db

db = cargar_db()


globalId=1
globalCDT=1


#Funcion para crear cuentas
def crear_cuentas():
    global globalId
    dia=input("Ingrese el día de creación (1-31): ")
    mes=input("Ingrese el mes de creación (1-12): ")
    año=input("Ingrese el año de creación (e.g., 2025): ")
    fecha=dia + "/" + mes + "/" + año
    
    cc = input("Ingrese el número de cédula del cliente: ")
    
    if not cc.isdigit() or len(cc) < 8:
        print("La cédula debe contener al menos 8 dígitos.")
        return
    
    cliente=consultar_cliente(cc)
    if cliente is None:
        print("Cliente no encontrado.")
        return
    idCuenta = f'CU{globalId:05d}'
    globalId += 1

    if idCuenta in cliente.get("cuentas", {}):
        print("La cuenta ya existe.")
        return
    
    tipo = input("Ingrese el tipo de cuenta (Ahorros, Corriente): ").strip().lower()
    if tipo not in ["ahorros", "corriente"]:
        print("Tipo de cuenta no válido. Debe ser Ahorros, Corriente")
        return
    
    new_cuenta = {
        "id": idCuenta,
        "tipo": tipo,
        "fecha_creacion": fecha,
        "saldo": 0.0,
        "movimientos": {
            1: {
                "tipo": "CREACION",
                "fecha": fecha,
                "monto": 0.0,
                "saldo": 0.0
            }
        }
    }
    if "cuentas" not in cliente:
        cliente["cuentas"] = {}

    cliente["cuentas"][idCuenta] = new_cuenta
    guardar_cliente(cc, cliente)
    

    print(f"Cuenta {idCuenta} creada exitosamente para el cliente {cc}.")

#Funcion para realizar un deposito de dinero
def deporsitar_dinero():
    dia=input("Ingrese el día de creación (1-31): ")
    mes=input("Ingrese el mes de creación (1-12): ")
    año=input("Ingrese el año de creación (e.g., 2025): ")
    fecha=dia + "/" + mes + "/" + año
    db=persistencia.cargar_db()
    cc= input("Ingrese el número de cédula del cliente: ")
    if cc not in db["clientes"]:
        print("Cliente no encontrado.")
        return
    if not cc.isdigit() or len(cc) < 8:
        print("La cédula debe contener al menos 8 dígitos.")
        return
    
    idCuenta = input("Ingrese el ID de la cuenta: ")
    if idCuenta not in db["clientes"][cc]['cuentas']:
        print("La cuenta no existe.")
        return
    monto = float(input("Ingrese el monto a depositar: "))
    if monto <= 0:
        print("El monto debe ser mayor que cero.")
        return
    cuenta = db["clientes"][cc]["cuentas"][idCuenta]
    cuenta["saldo"] += monto

    idMov = str(len(cuenta['movimientos']) + 1)
    cuenta['movimientos'][idMov] = {
        "tipo": "DEPOSITO",
        "fecha": fecha,  
        "saldo": cuenta['saldo']
    }

    persistencia.guardar_db(db)
    print(f"Depósito exitoso. Nuevo saldo: {cuenta['saldo']}")

def retirar_Dinero():
    dia=input("Ingrese el día de creación (1-31): ")
    mes=input("Ingrese el mes de creación (1-12): ")
    año=input("Ingrese el año de creación (e.g., 2025): ")
    fecha=dia + "/" + mes + "/" + año
    db=persistencia.cargar_db()
    cc= input("Ingrese el número de cédula del cliente: ")
    if cc not in db["clientes"]:
        print("Cliente no encontrado.")
        return
    if not cc.isdigit() or len(cc) < 8:
        print("La cédula debe contener al menos 8 dígitos.")
        return
    
    idCuenta = input("Ingrese el ID de la cuenta: ")
    if idCuenta not in db["clientes"][cc]['cuentas']:
        print("La cuenta no existe.")
        return
    monto = float(input("Ingrese el monto a retirar: "))
    if monto <= 0:
        print("El monto debe ser mayor que cero.")
        return
    cuenta = db["clientes"][cc]["cuentas"][idCuenta]
    
    if cuenta["saldo"] < monto:
        print("Saldo insuficiente para realizar el retiro.")
        return
    
    cuenta["saldo"] -= monto

    idMov = str(len(cuenta['movimientos']) + 1)
    cuenta['movimientos'][idMov] = {
        "tipo": "RETIRO",
        "fecha": fecha,  
        "monto": monto,
        "saldo": cuenta['saldo']
    }

    persistencia.guardar_db(db)
    print(f"Retiro exitoso. Nuevo saldo: {cuenta['saldo']}")

def creacion_cdt():
    global globalCDT
    dia=input("Ingrese el día de creación (1-31): ")
    mes=input("Ingrese el mes de creación (1-12): ")
    año=input("Ingrese el año de creación (e.g., 2025): ")
    fecha=dia + "/" + mes + "/" + año

    cc = input("Ingrese el número de cédula del cliente: ")
    
    if not cc.isdigit() or len(cc) < 8:
        print("La cédula debe contener al menos 8 dígitos.")
        return
    
    cliente=consultar_cliente(cc)
    if cliente is None:
        print("Cliente no encontrado.")
        return
    idCDT = f'CDT{globalCDT:05d}'
    globalCDT += 1
    if idCDT in cliente.get("cuentas", {}):
        print("La cuenta ya existe.")
        return
    monto = float(input("Ingrese el monto a invertir en el CDT: "))
    print("El cdt tiene una taza de interés del 5% mensual.")
    if monto <= 0:
        print("El monto debe ser mayor que cero.")
        return
    plazo= int(input("Ingrese el plazo del CDT en meses: "))
    if plazo <= 0:
        print("El plazo debe ser mayor que cero.")
        return
    ganancia = monto *(0.5* plazo)
    new_CDT = {
        "id": idCDT,
        "tipo": "CDT",
        "fecha_creacion": fecha,
        "saldo": 0.0,
        "movimientos": {
            1: {
                "tipo": "CREACION",
                "fecha": fecha,
                "monto inicial": monto,
                "plazo": {plazo: "meses"},
                "ganancia": ganancia,

            }
        }
    }
    if "CDT" not in cliente:
        cliente["cuentas"] = {}

    cliente["cuentas"][idCDT] = new_CDT
    guardar_cliente(cc, cliente)
    

    print(f"Cuenta {idCDT} creada exitosamente para el cliente {cc}.")