import json
import os
from typing import Dict, List, Optional
from Modulos.persistencia import guardar_cliente
from Modulos.persistencia import consultar_cliente
db="Modulos/db.json"
clientes={}



def crear_clientes():
    while True:
        cc = input("Ingrese el número de cédula del cliente: ")
        if cc in clientes:
            print("El cliente ya existe.")
        if not cc.isdigit() or len(cc) < 8:
            print("La cédula debe contener al menos 8 dígitos.")
        else:
            break
    
    while True:
        name= input("Ingrese el nombre del cliente: ")
        if not name.isalpha():
            print("El nombre debe contener solo letras.")
        else :
            break

    while True:
        email = input("Ingrese el correo electrónico del cliente: ")
        if '@' not in email or '.' not in email:
            print("El correo electrónico no es válido.")
        else:
            break
    while True:
        age= int(input("Ingrese la edad del cliente: "))
        if age < 18:
            print("El cliente debe ser mayor de edad.")
        else:
            break

    while True:
        try:
            contacto = int(input("¿Qué medio de comunicación prefiere?\n1. Móvil\n2. Fijo\n3. Ambos\n"))
        except ValueError:
            print("Debe ingresar una opción válida (1, 2 o 3).")
            continue
        if contacto not in [1, 2, 3]:
            print("Opción no válida. Por favor, intente de nuevo.")
            continue
        else:
            break

    contacto_telefonico = {}

    if contacto == 1:
        while True:
            telefono = input("Ingrese el número de teléfono móvil: ")
            if not telefono.isdigit() or len(telefono) != 10:
                print("El número de teléfono móvil debe contener 10 dígitos.")
                continue
            contacto_telefonico = {"movil": telefono}
            break

    elif contacto == 2:
        while True:
            telefono = input("Ingrese el número de teléfono fijo: ")
            if not telefono.isdigit() or len(telefono) < 7:
                print("El número de teléfono fijo debe contener al menos 7 dígitos.")
                continue
            contacto_telefonico = {"fijo": telefono}
            break

    elif contacto == 3:
        # Primero pide móvil
        while True:
            telefono_movil = input("Ingrese el número de teléfono móvil: ")
            if not telefono_movil.isdigit() or len(telefono_movil) != 10:
                print("El número de teléfono móvil debe contener 10 dígitos.")
                continue
            break
        # Luego pide fijo
        while True:
            telefono_fijo = input("Ingrese el número de teléfono fijo: ")
            if not telefono_fijo.isdigit() or len(telefono_fijo) < 7:
                print("El número de teléfono fijo debe contener al menos 7 dígitos.")
                continue
            break
        contacto_telefonico = {
            "movil": telefono_movil,
            "fijo": telefono_fijo
        }
    else:
        print("Opción no válida. Debe ser 1, 2 o 3.")
        return
    
    while True:
        pais = input("Ingrese el país del cliente: ")
        if not pais.isalpha():
            print("El país debe contener solo letras.")
        else:
            break
    while True:
        departamento = input("Ingrese el departamento del cliente: ")
        if not departamento.isalpha():
            print("El departamento debe contener solo letras.")
        else:
            break
    while True:
        ciudad = input("Ingrese la ciudad del cliente: ")
        if not ciudad.isalpha():
            print("La ciudad debe contener solo letras.")
        else:
            break
    while True:
        direccion = input("Ingrese la dirección del cliente: ")
        if not direccion:
            print("La dirección no puede estar vacía.")
        else:
            break
    
    # Crear el cliente
    clientes[cc] = {
        "cc": cc,
        "nombre": name,
        "email": email,
        "edad": age,
        "contacto": contacto_telefonico,
        "ubicacion": {"pais": pais, "departamento": departamento, "ciudad": ciudad, "direccion": direccion},
        "cuentas": {},
        "CDT": {},
        "creditos": {}
    }
    print(f'Cliente {name} creado exitosamente.')
    guardar_cliente(cc,clientes[cc])
    

def consultar_clientes():
    cc = input("Ingrese el número de cédula del cliente a consultar: ").strip()
    cliente = consultar_cliente(cc)

    if not cliente:
        print(f"No se encontró ningún cliente con cédula {cc}.")
        return

    nombre = cliente.get("nombre", "No registrado")
    print("\n" + "=" * 60)
    print(f"{'RESUMEN DEL CLIENTE':^60}")
    print("=" * 60)
    print(f"{'Nombre':<15}: {nombre}")
    print(f"{'Cédula':<15}: {cc}")
    print("-" * 60)

    # Cuentas
    cuentas = cliente.get("cuentas", {})
    print(f"{'CUENTAS':<60}")
    if cuentas:
        print(f"{'ID':<20}{'Saldo':>20}")
        print("-" * 40)
        for cid, datos in cuentas.items():
            saldo = datos.get("saldo", 0.0)
            print(f"{cid:<20}{f'$ {saldo:,.2f}':>20}")
    else:
        print("No hay cuentas registradas.")
    print("-" * 60)

    # Créditos
    creditos = cliente.get("creditos", {})
    print(f"{'CRÉDITOS':<60}")
    if creditos:
        print(f"{'ID':<20}{'Deuda total':>20}")
        print("-" * 40)
        for cid, datos in creditos.items():
            monto = datos.get("monto", 0.0)
            interes = datos.get("interes", 0.0)
            deuda = monto + interes
            print(f"{cid:<20}{f'$ {deuda:,.2f}':>20}")
    else:
        print("No hay créditos registrados.")
    print("-" * 60)


    # CDTs
    cdts = cliente.get("CDT", {})
    print(f"{'CDTs':<60}")
    if cdts:
        print(f"{'ID':<12}{'Fecha':<15}{'Monto':>10}{'Plazo':>10}{'Ganancia':>12}{'Total':>12}")
        print("-" * 60)
        for cid, datos in cdts.items():
            fecha = datos.get("fecha_creacion", "Desconocida")
            mov = datos.get("movimientos", {}).get("1", {})
            monto = mov.get("monto inicial", 0.0)
            plazo_dict = mov.get("plazo", {})
            plazo = list(plazo_dict.keys())[0] if plazo_dict else 0
            ganancia = mov.get("ganancia", 0.0)
            total = mov.get("total_ganancia", 0.0)
            print(f"{cid:<12}{fecha:<15}{f'$ {monto:,.2f}':>10}{f'{plazo}m':>10}{f'$ {ganancia:,.2f}':>12}{f'$ {total:,.2f}':>12}")
    else:
        print("No hay CDTs registrados.")
    print("=" * 60)
    print("\n" + "=" * 60)
    print(f"{'FIN DEL RESUMEN':^60}")
    print("=" * 60)

#Con esta función se puede consultar el historial de movimientos de un cliente
def mostrar_historial(cliente):
    print("=" * 60)
    print(f"{'HISTORIAL DE MOVIMIENTOS':^60}")
    print("=" * 60)

    # Cuentas
    cuentas = cliente.get("cuentas", {})
    for cid, datos in cuentas.items():
        print(f"\nCuenta: {cid}")
        movimientos = datos.get("movimientos", {})
        for mid, mov in movimientos.items():
            print(f"  [{mov.get('fecha', 'Sin fecha')}] {mov.get('tipo', 'Sin tipo')} - Monto: $ {mov.get('monto', 0.0):,.2f}")

    # Créditos
    creditos = cliente.get("creditos", {})
    for cid, datos in creditos.items():
        print(f"\nCrédito: {cid}")
        movimientos = datos.get("movimientos", {})
        for mid, mov in movimientos.items():
            print(f"  [{mov.get('fecha', 'Sin fecha')}] {mov.get('tipo', 'Sin tipo')} - Monto: $ {mov.get('monto', 0.0):,.2f}")

    # CDTs
    cdts = cliente.get("CDT", {})
    for cid, datos in cdts.items():
        print(f"\nCDT: {cid}")
        movimientos = datos.get("movimientos", {})
        for mid, mov in movimientos.items():
            monto = mov.get("monto inicial", mov.get("monto", 0.0))
            print(f"  [{mov.get('fecha', 'Sin fecha')}] {mov.get('tipo', 'Sin tipo')} - Monto: $ {monto:,.2f}")

    print("\n" + "=" * 60)
    print(f"{'FIN DEL HISTORIAL':^60}")
    print("=" * 60)


def historial():
    cc = input("Ingrese el número de cédula del cliente: ")
    if not cc.isdigit() or len(cc) < 8:
        print("La cédula debe contener al menos 8 dígitos.")
        return
    cliente = consultar_cliente(cc)
    if cliente is None:
        print("Cliente no encontrado.")
        return
    mostrar_historial(cliente)
