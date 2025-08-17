###En este se realizaran las creaciones de los creditos, consultas y pagos de los mismos
import json
import os
import Modulos.persistencia as persistencia
from Modulos.persistencia import guardar_cliente, consultar_cliente
from Modulos.persistencia import cargar_db, guardar_db
db = cargar_db()

creditoid = 1


#Funcion para crear credito auto
def credito_auto():
    dia=input("Ingrese el día de creación (1-31): ")
    mes=input("Ingrese el mes de creación (1-12): ")
    año=input("Ingrese el año de creación (e.g., 2025): ")
    fecha=dia + "/" + mes + "/" + año
    global creditoid
    cc = input("Ingrese el número de cédula del cliente: ")
    if not cc.isdigit() or len(cc) < 8:
        print("La cédula debe contener al menos 8 dígitos.")
        return
    cliente = consultar_cliente(cc)
    if cliente is None:
        print("Cliente no encontrado.")
        return
    idCredito = f'CR{creditoid:05d}'
    creditoid += 1
    if idCredito in cliente.get("creditos", {}):
        print("El crédito ya existe.")
        return
    monto= float(input("Ingrese el monto del crédito: "))
    if monto <= 0:
        print("El monto del crédito debe ser mayor a cero.")
        return
    plazo = int(input("Ingrese el plazo del crédito en meses: "))
    if plazo <= 0:
        print("El plazo del crédito debe ser mayor a cero.")
        return
    tasa_interes=0.05
    interes = monto * (tasa_interes * plazo)
    interes = round(interes, 2)
    pago_mensual = round((monto + interes) / plazo, 2)
    pago_total = monto + interes
    print(f"El pago mensual del crédito es: {pago_mensual}")
    print(f"El interés total del crédito es: {interes}")
    new_credito = {
        "id": idCredito,
        "tipo": "AUTO",
        "fecha_creacion": fecha,
        "monto": monto,
        "plazo": plazo,
        "interes": interes,
        "pago_mensual": pago_mensual,
        "movimientos": {
            1: {
                "tipo": "CREACION",
                "fecha": fecha,
                "monto_inicial": monto,
                "plazo_meses": plazo,
                "interes_total": interes,
                "pago_mensual": pago_mensual,
                "pago_total": pago_total
            }
        }
    }
    if "creditos" not in cliente:
        cliente["creditos"] = {}

    cliente["creditos"][idCredito] = new_credito
    guardar_cliente(cc, cliente)

#Funcion para crear credito libre
def credito_libre():
    dia=input("Ingrese el día de creación (1-31): ")
    mes=input("Ingrese el mes de creación (1-12): ")
    año=input("Ingrese el año de creación (e.g., 2025): ")
    fecha=dia + "/" + mes + "/" + año
    global creditoid
    cc = input("Ingrese el número de cédula del cliente: ")
    if not cc.isdigit() or len(cc) < 8:
        print("La cédula debe contener al menos 8 dígitos.")
        return
    cliente = consultar_cliente(cc)
    if cliente is None:
        print("Cliente no encontrado.")
        return
    idCredito = f'CR{creditoid:05d}'
    creditoid += 1
    if idCredito in cliente.get("creditos", {}):
        print("El crédito ya existe.")
        return
    monto= float(input("Ingrese el monto del crédito: "))
    if monto <= 0:
        print("El monto del crédito debe ser mayor a cero.")
        return
    plazo = int(input("Ingrese el plazo del crédito en meses: "))
    if plazo <= 0:
        print("El plazo del crédito debe ser mayor a cero.")
        return
    tasa_interes=0.08
    interes = (monto * tasa_interes) * plazo
    interes = round(interes, 2)
    pago_mensual = round((monto + interes) / plazo, 2)
    pago_total = monto + interes
    print(f"El pago mensual del crédito es: {pago_mensual}")
    new_credito = {
        "id": idCredito,
        "tipo": "Libre Inversion",
        "fecha_creacion": fecha,
        "monto": monto,
        "plazo": plazo,
        "interes": interes,
        "pago_mensual": pago_mensual,
        "movimientos": {
            1: {
                "tipo": "CREACION",
                "fecha": fecha,
                "monto_inicial": monto,
                "plazo_meses": plazo,
                "interes_total": interes,
                "pago_mensual": pago_mensual,
                "pago_total": pago_total

            }
        }
    }
    if "creditos" not in cliente:
        cliente["creditos"] = {}

    cliente["creditos"][idCredito] = new_credito
    guardar_cliente(cc, cliente)

#Funcion para crear credito vivienda
def credito_vivienda():
    dia=input("Ingrese el día de creación (1-31): ")
    mes=input("Ingrese el mes de creación (1-12): ")
    año=input("Ingrese el año de creación (e.g., 2025): ")
    fecha=dia + "/" + mes + "/" + año
    global creditoid
    cc = input("Ingrese el número de cédula del cliente: ")
    if not cc.isdigit() or len(cc) < 8:
        print("La cédula debe contener al menos 8 dígitos.")
        return
    cliente = consultar_cliente(cc)
    if cliente is None:
        print("Cliente no encontrado.")
        return
    idCredito = f'CR{creditoid:05d}'
    creditoid += 1
    if idCredito in cliente.get("creditos", {}):
        print("El crédito ya existe.")
        return
    monto= float(input("Ingrese el monto del crédito: "))
    if monto <= 0:
        print("El monto del crédito debe ser mayor a cero.")
        return
    plazo = int(input("Ingrese el plazo del crédito en meses: "))
    if plazo <= 0:
        print("El plazo del crédito debe ser mayor a cero.")
        return
    tasa_interes=0.01
    interes =( monto * tasa_interes) * plazo
    interest = round(interes, 2)  
    pago_mensual = round((monto + interes) / plazo, 2)
    pago_total = monto + interest
    print(f"El pago mensual del crédito es: {pago_mensual}")
    print(f"El interés total del crédito es: {interest}")

    new_credito = {
        "id": idCredito,
        "tipo": "Vivienda",
        "fecha_creacion": fecha,
        "monto": monto,
        "plazo": plazo,
        "interes": interes,
        "pago_mensual": pago_mensual,
        "movimientos": {
            1: {
                "tipo": "CREACION",
                "fecha": fecha,
                "monto_inicial": monto,
                "plazo_meses": plazo,
                "interes_total": interest,
                "pago_mensual": pago_mensual,
                "pago_total": pago_total

            }
        }
    }
    if "creditos" not in cliente:
        cliente["creditos"] = {}

    cliente["creditos"][idCredito] = new_credito
    guardar_cliente(cc, cliente)

#Funcion para pagar credito
def pagar_credito():
    dia=input("Ingrese el día de pago (1-31): ")
    mes=input("Ingrese el mes de pago (1-12): ")
    año=input("Ingrese el año de pago (e.g., 2025): ")
    fecha=dia + "/" + mes + "/" + año
    cc = input("Ingrese el número de cédula del cliente: ")
    if not cc.isdigit() or len(cc) < 8:
        print("La cédula debe contener al menos 8 dígitos.")
        return
    cliente = consultar_cliente(cc)
    if cliente is None:
        print("Cliente no encontrado.")
        return
    if "creditos" not in cliente or not cliente["creditos"]:
        print("El cliente no tiene créditos.")
        return
    print("Créditos disponibles:")
    for credito_id, credito in cliente["creditos"].items():
        print(f'ID: {credito_id}, Tipo: {credito["tipo"]}, Monto: {credito["monto"]}, Plazo: {credito["plazo"]} meses, Interés: {credito["interes"]}')
    idCredito = input("Ingrese el ID del crédito a pagar: ")
    if idCredito not in cliente["creditos"]:
        print("Crédito no encontrado.")
        return
    credito = cliente["creditos"][idCredito]
    monto_pago = float(input("Ingrese el monto a pagar: "))
    if monto_pago <= 0:
        print("El monto a pagar debe ser mayor a cero.")
        return
    if monto_pago > credito["monto"] + credito["interes"]:
        print("El monto a pagar excede el saldo del crédito.")
        return
    credito["monto"] -= monto_pago
    if credito["monto"] < 0:
        credito["monto"] = 0
    movimiento_id = len(credito["movimientos"]) + 1
    credito["movimientos"][movimiento_id] = {
        "tipo": "PAGO",
        "fecha": fecha,
        "monto_pagado": monto_pago
    }
    guardar_cliente(cc, cliente)
    print(f'Pago de {monto_pago} realizado exitosamente. Nuevo saldo del crédito: {credito["monto"]}')

def mostrar_creditos():
    cc = input("Ingrese el número de cédula del cliente: ")
    if not cc.isdigit() or len(cc) < 8:
        print("La cédula debe contener al menos 8 dígitos.")
        return

    cliente = consultar_cliente(cc)
    if cliente is None:
        print("Cliente no encontrado.")
        return

    creditos = cliente.get("creditos", {})
    if not creditos:
        print("El cliente no tiene créditos.")
        return

    # Ordenar por ID de crédito (alfabéticamente)
    creditos_ordenados = dict(sorted(creditos.items()))

    print("\nCréditos del cliente:")
    for id_credito, datos in creditos_ordenados.items():
        print(f"ID: {id_credito}")
        print(f"  Tipo: {datos['tipo']}")
        print(f"  Fecha de creación: {datos['fecha_creacion']}")
        print(f"  Monto: {datos['monto']}")
        print(f"  Plazo: {datos['plazo']} meses")
        print(f"  Interés total: {datos['interes']}")
        print(f"  Pago mensual: {datos.get('pago_mensual', 'No definido')}")
        print("-" * 40)
